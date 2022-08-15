from typing import Iterable, Callable

from jcapiv1 import ApplicationsApi, Application

from jumpcloud_provider.extractors.jumpcloud_extractor import JumpcloudExtractor
from jumpcloud_provider.extractors.jumpcloud_pagination import JumpcloudPagination


class ApplicationsExtractor(JumpcloudExtractor):
    """
    Gets a list of Apps in a jumpcloud account.

    See https://docs.jumpcloud.com/api/1.0/index.html#tag/Applications
        https://github.com/TheJumpCloud/jcapi-python/blob/master/jcapiv1/jcapiv1/api/applications_api.py
    """

    def extract_raw(self) -> Iterable[Application]:
        applications_client = ApplicationsApi(self.jumpcloud_client.client_v1)
        pagination_api = self._call_applications_api(applications_client)
        return self.extract_with_pagination(pagination_api)

    def _call_applications_api(self, applications_client: ApplicationsApi) -> Callable[[int], JumpcloudPagination]:
        client_configuration = self.client_configuration
        return lambda skip: applications_client.applications_list(
            skip=skip,
            limit=client_configuration.limit,
            accept=client_configuration.accept,
            content_type=client_configuration.content_type
        )
