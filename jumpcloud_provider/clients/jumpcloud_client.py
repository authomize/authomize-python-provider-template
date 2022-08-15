from typing import cast

import jcapiv1
import jcapiv2

from base_provider.clients.base_client import BaseClient
from jumpcloud_provider.configuration.client_configuration import JumpcloudClientConfiguration


class JumpcloudClient(BaseClient):
    def __init__(
        self,
        client_configuration: JumpcloudClientConfiguration,
    ) -> None:
        super().__init__(client_configuration=client_configuration)
        jumpcloud_v1_configuration = self.resolve_v1_configuration(client_configuration)
        jumpcloud_v2_configuration = self.resolve_v2_configuration(client_configuration)
        self.client_v1 = jcapiv1.ApiClient(jumpcloud_v1_configuration)
        self.client_v2 = jcapiv2.ApiClient(jumpcloud_v2_configuration)

    def resolve_v1_configuration(self, client_configuration: JumpcloudClientConfiguration) -> jcapiv1.Configuration:
        return cast(jcapiv1.Configuration, self._resolve_configuration(client_configuration, jcapiv1))

    def resolve_v2_configuration(self, client_configuration: JumpcloudClientConfiguration) -> jcapiv2.Configuration:
        return cast(jcapiv2.Configuration, self._resolve_configuration(client_configuration, jcapiv2))

    def _resolve_configuration(self, client_configuration: JumpcloudClientConfiguration, namespace) -> object:
        jumpcloud_configuration = namespace.Configuration()
        jumpcloud_configuration.api_key['x-api-key'] = client_configuration.api_key
        return jumpcloud_configuration
