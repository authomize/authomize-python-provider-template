from base_provider.configuration.application_configuration import ApplicationConfiguration
from base_provider.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from jumpcloud_provider.configuration.client_configuration import JumpcloudClientConfiguration
from jumpcloud_provider.configuration.shared_configuration import JumpcloudSharedConfiguration
from jumpcloud_provider.workflows.health_checker import JumpcloudHealthChecker
from jumpcloud_provider.workflows.runner import JumpcloudRunner


def example():
    authomize_api_configuration = AuthomizeApiConfiguration()
    application_configuration = ApplicationConfiguration()
    client_configuration = JumpcloudClientConfiguration()
    shared_configuration = JumpcloudSharedConfiguration(client_configuration=client_configuration)
    health_checker = JumpcloudHealthChecker(
        authomize_api_configuration=authomize_api_configuration,
        client_configuration=client_configuration,
    )
    health_checker.raise_unhealthy()
    workflow_run = JumpcloudRunner(
        authomize_api_configuration=authomize_api_configuration,
        client_configuration=client_configuration,
        application_configuration=application_configuration,
        shared_configuration=shared_configuration,
    )
    workflow_run.run()


example()

