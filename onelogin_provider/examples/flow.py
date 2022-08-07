from base_provider import ApplicationConfiguration, AuthomizeApiConfiguration
from onelogin_provider.configuration.client_configuration import OneloginClientConfiguration
from onelogin_provider.configuration.shared_configuration import OneloginSharedConfiguration
from onelogin_provider.workflows.health_check import OneloginHealthChecker
from onelogin_provider.workflows.run import OneloginRunWorkflow


def example():
    authomize_api_configuration = AuthomizeApiConfiguration(
        auth_token='==',
        api_url='https://api.authomize.com',
    )
    data_provider_client_configuration = OneloginClientConfiguration(
        client_id='',
        client_secret='',
    )
    application_configuration = ApplicationConfiguration(
        app_id='',
    )
    general_configuration = OneloginSharedConfiguration()
    health_checker = OneloginHealthChecker(
        authomize_api_configuration=authomize_api_configuration,
        data_provider_client_configuration=data_provider_client_configuration,
    )
    workflow_run = OneloginRunWorkflow(
        authomize_api_configuration=authomize_api_configuration,
        data_provider_client_configuration=data_provider_client_configuration,
        application_configuration=application_configuration,
        general_configuration=general_configuration,
    )
    health_checker.raise_unhealthy()
    workflow_run.run()


example()
