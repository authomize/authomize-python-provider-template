from pydantic import Field

from base_provider.configuration.base_client_configuration import BaseClientConfiguration


class MicrosoftClientConfiguration(BaseClientConfiguration):
    # TODO: not sure why it doesn't work with the "Field"
    tenant_id: str = 'asd'  # Field(..., env="MICROSOFT_TENANT_ID")
    client_id: str = 'asd'  # Field(..., env="MICROSOFT_CLIENT_ID")
    client_secret: str = 'asd'  # Field(..., env="MICROSOFT_CLIENT_SECRET")
