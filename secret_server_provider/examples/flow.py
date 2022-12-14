from logging import basicConfig

from base_provider.configuration.application_configuration import ApplicationConfiguration
from base_provider.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from secret_server_provider.configuration.client_configuration import SecretServerConfiguration
from secret_server_provider.configuration.shared_configuration import (
    SecretServerSharedConfiguration,
)
from secret_server_provider.workflows.health_checker import SecretServerHealthChecker
from secret_server_provider.workflows.runner import SecretServerRunner


def example():
    basicConfig(
        level='INFO',
        format='%(asctime)s - %(levelname)s - %(message)s %(params)s',
    )

    authomize_api_configuration = AuthomizeApiConfiguration()
    application_configuration = ApplicationConfiguration()
    client_configuration = SecretServerConfiguration()
    shared_configuration = SecretServerSharedConfiguration()
    health_checker = SecretServerHealthChecker(
        authomize_api_configuration=authomize_api_configuration,
        client_configuration=client_configuration,
    )
    workflow_run = SecretServerRunner(
        authomize_api_configuration=authomize_api_configuration,
        client_configuration=client_configuration,
        application_configuration=application_configuration,
        shared_configuration=shared_configuration,
    )
    health_checker.raise_unhealthy()
    workflow_run.run()


example()
