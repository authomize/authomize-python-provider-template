from base_provider.configuration.application_configuration import ApplicationConfiguration
from base_provider.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from base_provider.configuration.general_configuration import GeneralConfiguration
from onelogin_provider.configuration.onelogin_configuration import OneloginConfiguration
from onelogin_provider.workflows.health_check import OneloginHealthChecker
from onelogin_provider.workflows.run import OneloginRunWorkflow


def example():
    authomize_api_configuration = AuthomizeApiConfiguration(
        auth_token='==',
        api_url='https://api.authomize.com',
    )
    data_provider_configuration = OneloginConfiguration(
        client_id='',
        client_secret='',
    )
    application_configuration = ApplicationConfiguration(
        app_id='',
    )
    general_configuration = GeneralConfiguration()
    health_checker = OneloginHealthChecker(
        authomize_api_configuration=authomize_api_configuration,
        data_provider_configuration=data_provider_configuration,
    )
    workflow_run = OneloginRunWorkflow(
        authomize_api_configuration=authomize_api_configuration,
        data_provider_configuration=data_provider_configuration,
        application_configuration=application_configuration,
        general_configuration=general_configuration,
    )
    health_checker.raise_unhealthy()
    workflow_run.run()


example()
