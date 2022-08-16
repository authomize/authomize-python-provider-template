from base_provider.configuration.application_configuration import ApplicationConfiguration
from base_provider.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from onelogin_provider.configuration.client_configuration import OneloginClientConfiguration
from onelogin_provider.configuration.shared_configuration import OneloginSharedConfiguration
from onelogin_provider.workflows.health_checker import OneloginHealthChecker
from onelogin_provider.workflows.runner import OneloginRunner


def example():
    authomize_api_configuration = AuthomizeApiConfiguration()
    application_configuration = ApplicationConfiguration()
    client_configuration = OneloginClientConfiguration()
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
