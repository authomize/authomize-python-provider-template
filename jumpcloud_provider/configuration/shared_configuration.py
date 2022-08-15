from base_provider.configuration.base_shared_configuration import BaseSharedConfiguration
from jumpcloud_provider.configuration.client_configuration import JumpcloudClientConfiguration


class JumpcloudSharedConfiguration(BaseSharedConfiguration):
    client_configuration: JumpcloudClientConfiguration

    def __int__(self, client_configuration: JumpcloudClientConfiguration):
        super().__init__()
        self.client_configuration = client_configuration




