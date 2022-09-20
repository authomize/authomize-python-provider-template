from typing import Iterator, Dict

from authomize.core.concurrent import ConcurrentTaskRunner

from base_provider.extractors.base_extractor import BaseExtractor
from teams_provider.exceptions import InvalidStateException


class RolesExtractor(BaseExtractor):
    """
    Gets a list of Role resources. Roles tell us whether a user is a member or an admin of
        a channel or a team.
        Example result from Microsoft Graph
        {
            "@odata.type": "#microsoft.graph.aadUserConversationMember",
            "id": "MmFiOWM3OTYtMjkwMi00NWY4LWI3MTItN2M1YTYzY2Y0MWM0IyNiMzI0NmY0NC1jMDkxLTQ2MjctOTZjNi0yNWIxOGZhMmM5MTA=",
            "roles": [
                "owner"
            ],
            "displayName": "Ace John",
            "userId": "b3246f44-c091-4627-96c6-25b18fa2c910",
            "email": "ajohn@teamsip.onmicrosoft.com"
        }
        The data doesn't contain the team/channel that was requested so it is added from the
        request by our Microsoft client.
    """

    def extract_raw(self) -> Iterator[Dict]:
        data_provider_client: MicrosoftClient = self.data_provider_client  # type: ignore
        shared_memory: TeamsProviderSharedMemory = self.shared_memory  # type: ignore
        teams = shared_memory.team_ids
        team_to_channels = shared_memory.team_id_to_channel_ids

        if not teams or not team_to_channels:
            raise InvalidStateException("Teams and channels extractors need be run first")

        # Get all team and channel memberships data in parallel, for speed.
        # get_all_items tags the results with the URI from the request so each result can later
        # be traced back to the request, as the result doesn't contain which team/channel it's
        # about.
        task_runner = ConcurrentTaskRunner(max_workers=10)
        team_task_results = task_runner.task_map(
            data_provider_client.client.get_all_items,
            ['teams/{}/members'.format(team) for team in teams],
        )
        channel_task_results = task_runner.task_map(
            data_provider_client.client.get_all_items,
            ['teams/{}/channels/{}/members'.format(team, channel)
             for team in teams for channel in team_to_channels[team]]
        )
        for result in team_task_results:
            yield from result
        for result in channel_task_results:
            yield from result
