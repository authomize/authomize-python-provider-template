from typing import cast

import jcapiv1
from jcapiv2.rest import ApiException

from base_provider.workflows.base_health_checker import BaseProviderHealthChecker
from jumpcloud_provider.clients.jumpcloud_client import JumpcloudClient
from jumpcloud_provider.configuration.client_configuration import JumpcloudClientConfiguration


class JumpcloudHealthChecker(BaseProviderHealthChecker):
    def can_connect_to_data_provider(self) -> bool:
        return self.can_read_from_data_provider()

    def can_read_from_data_provider(self) -> bool:
        client_configuration = cast(JumpcloudClientConfiguration, self.client_configuration)
        client_v1 = JumpcloudClient(client_configuration=client_configuration).client_v1

        try:
            jcapiv1.SystemusersApi(client_v1).systemusers_list(
                limit=1,
                accept=client_configuration.accept,
                content_type=client_configuration.content_type
            )
            return True
        except ApiException:
            return False
