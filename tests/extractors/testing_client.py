from teams_provider.clients import microsoft_client
from teams_provider.configuration.client_configuration import MicrosoftClientConfiguration


def create_microsoft_client():
    client_configuration = MicrosoftClientConfiguration(
            tenant_id='d68b70a5-7265-4e19-8969-6513b117dcb5',
            client_id='0901bf5b-f310-4c52-b07f-aece104c3556',
            client_secret='nUT7Q~qylG.hFFxLV9GmE3g9135x0hihYWiv9'
        )
    return microsoft_client.MicrosoftClient(client_configuration)