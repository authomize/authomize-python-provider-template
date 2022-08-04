from provider_base.configuration.application_configuration import ApplicationConfiguration
from provider_base.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from provider_base.configuration.general_configuration import GeneralConfiguration
from provider_name.configuration.data_provider_configuration import DataProviderConfiguration
from provider_name.workflows.health_check import ProviderNameHelathChecker
from provider_name.workflows.run import RunWorkflow


def example():
    authomize_api_configuration = AuthomizeApiConfiguration(
        auth_token='123',
        api_url='https://api.authomize.com',
    )
    data_provider_configuration = DataProviderConfiguration(
        base_url='https://data.authomize.com',
        domain='mycompany',
        token='123',
    )
    application_configuration = ApplicationConfiguration(
        app_id='1234',
    )
    general_configuration = GeneralConfiguration()
    health_checker = ProviderNameHelathChecker(
        authomize_api_configuration=authomize_api_configuration,
        data_provider_configuration=data_provider_configuration,
    )
    workflow_run = RunWorkflow(
        authomize_api_configuration=authomize_api_configuration,
        data_provider_configuration=data_provider_configuration,
        application_configuration=application_configuration,
        general_configuration=general_configuration,
    )
    health_checker.raise_unhealthy()
    workflow_run.run()
