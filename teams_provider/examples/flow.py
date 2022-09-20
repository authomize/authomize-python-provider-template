from base_provider.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from teams_provider.configuration.client_configuration import MicrosoftClientConfiguration
from teams_provider.workflows.health_checker import MicrosoftHealthChecker


def example():
    authomize_api_configuration = AuthomizeApiConfiguration(
        auth_token='123',
        api_url='https://api.authomize.com',
    )
    client_configuration = MicrosoftClientConfiguration()
    health_checker = MicrosoftHealthChecker(
        authomize_api_configuration=authomize_api_configuration,
        client_configuration=client_configuration,
    )
    health_checker.can_connect_to_data_provider()


example()
