from bamboohr_provider.configuration.client_configuration import BamboohrClientConfiguration
from bamboohr_provider.configuration.shared_configuration import BamboohrSharedConfiguration
from bamboohr_provider.workflows.health_checker import BamboohrHealthChecker
from bamboohr_provider.workflows.runner import BamboohrRunner
from base_provider.configuration.application_configuration import ApplicationConfiguration
from base_provider.configuration.authomize_api_configuration import AuthomizeApiConfiguration


def example():
    authomize_api_configuration = AuthomizeApiConfiguration()
    application_configuration = ApplicationConfiguration()
    client_configuration = BamboohrClientConfiguration()
    shared_configuration = BamboohrSharedConfiguration()
    health_checker = BamboohrHealthChecker(
        authomize_api_configuration=authomize_api_configuration,
        client_configuration=client_configuration,
    )
    workflow_run = BamboohrRunner(
        authomize_api_configuration=authomize_api_configuration,
        client_configuration=client_configuration,
        application_configuration=application_configuration,
        shared_configuration=shared_configuration,
    )
    health_checker.raise_unhealthy()
    workflow_run.run()


example()
