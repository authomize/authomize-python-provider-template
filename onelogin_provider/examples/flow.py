from logging import basicConfig
from os import getenv

from base_provider import ApplicationConfiguration, AuthomizeApiConfiguration
from onelogin_provider.configuration.client_configuration import OneloginClientConfiguration
from onelogin_provider.configuration.shared_configuration import OneloginSharedConfiguration
from onelogin_provider.workflows.health_checker import OneloginHealthChecker
from onelogin_provider.workflows.runner import OneloginRunner


def example():
    basicConfig(
        level='INFO',
        format='%(asctime)s - %(levelname)s - %(message)s %(params)s',
    )

    authomize_api_configuration = AuthomizeApiConfiguration(
        auth_token=getenv("AUTHOMIZE_API_TOKEN"),
        api_url=getenv("AUTHOMIZE_API_URL"),
    )
    application_configuration = ApplicationConfiguration(
        app_id=getenv("AUTHOMIZE_API_APP_ID"),
    )
    client_configuration = OneloginClientConfiguration(
        client_id=getenv("ONELOGIN_CLIENT_ID"),
        client_secret=getenv("ONELOGIN_CLIENT_SECRET"),
    )
    shared_configuration = OneloginSharedConfiguration()
    health_checker = OneloginHealthChecker(
        authomize_api_configuration=authomize_api_configuration,
        client_configuration=client_configuration,
    )
    workflow_run = OneloginRunner(
        authomize_api_configuration=authomize_api_configuration,
        client_configuration=client_configuration,
        application_configuration=application_configuration,
        shared_configuration=shared_configuration,
    )
    health_checker.raise_unhealthy()
    workflow_run.run()


example()
