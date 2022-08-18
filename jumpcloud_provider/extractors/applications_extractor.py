from typing import Iterable, cast

import jcapiv2
from jcapiv1 import ApplicationsApi, Application
from jcapiv2 import GraphConnection

from jumpcloud_provider.extractors import JumpcloudApiResult
from jumpcloud_provider.extractors.jumpcloud_extractor import JumpcloudExtractor
from jumpcloud_provider.models.application_associations import ApplicationAssociations
from jumpcloud_provider.models.user_association import UserAssociation
from jumpcloud_provider.models.user_group_association import UserGroupAssociation


class ApplicationsExtractor(JumpcloudExtractor):
    """
    Gets a list of Apps in a jumpcloud account.
    See https://docs.jumpcloud.com/api/1.0/index.html#tag/Applications
        https://github.com/TheJumpCloud/jcapi-python/blob/master/jcapiv1/jcapiv1/api/applications_api.py
    """

    def extract_raw(self) -> Iterable[ApplicationAssociations]:
        applications = self._get_applications()
        return self._create_application_associations(applications)

    def _get_applications(self) -> Iterable[Application]:
        applications_client = ApplicationsApi(self.jumpcloud_client.client_v1)
        pagination_api = self._call_applications_api(applications_client)
        applications = self.extract_with_pagination(pagination_api)
        return cast(Iterable[Application], applications)

    def _call_applications_api(self, api: ApplicationsApi) -> JumpcloudApiResult:
        client_configuration = self.client_configuration
        return lambda skip: api.applications_list(
            skip=skip,
            limit=client_configuration.limit,
            accept=client_configuration.accept,
            content_type=client_configuration.content_type
        )

    def _call_user_groups_association(self, application_id: str, api: jcapiv2.ApplicationsApi) -> JumpcloudApiResult:
        client_configuration = self.client_configuration
        return lambda skip: api.graph_application_associations_list(
            skip=skip,
            targets=["user_group"],
            application_id=application_id,
            limit=client_configuration.limit,
            accept=client_configuration.accept,
            content_type=client_configuration.content_type
        )

    def _call_users_associations(self, application_id: str, api: jcapiv2.ApplicationsApi) -> JumpcloudApiResult:
        client_configuration = self.client_configuration
        return lambda skip: api.graph_application_associations_list(
            skip=skip,
            targets=["user"],
            application_id=application_id,
            limit=client_configuration.limit,
            accept=client_configuration.accept,
            content_type=client_configuration.content_type
        )

    def _create_application_associations(self, apps: Iterable[Application]) -> Iterable[ApplicationAssociations]:
        application_api = jcapiv2.ApplicationsApi(self.jumpcloud_client.client_v2)
        for application in apps:
            users_api = self._call_users_associations(application.id, application_api)
            user_groups_api = self._call_user_groups_association(application.id, application_api)
            user_connections = cast(Iterable[GraphConnection], self.extract_with_pagination(users_api))
            user_group_connections = cast(Iterable[GraphConnection], self.extract_with_pagination(user_groups_api))
            user_associations = [UserAssociation(user_id=user.to.id) for user in user_connections]
            user_group_associations = [UserGroupAssociation(group_id=group.to.id) for group in user_group_connections]
            yield ApplicationAssociations(
                id=application.id,
                name=application.name,
                user_associations=user_associations,
                user_group_associations=user_group_associations
            )
