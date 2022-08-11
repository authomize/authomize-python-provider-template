from logging import basicConfig
from os import getenv

from base_provider.configuration.application_configuration import ApplicationConfiguration
from base_provider.configuration.authomize_api_configuration import AuthomizeApiConfiguration
from secret__server_provider.configuration.client_configuration import SecretServerConfiguration
from secret__server_provider.configuration.shared_configuration import SecretServerSharedConfiguration
from secret__server_provider.workflows.health_checker import SecretServerHealthChecker
from secret__server_provider.workflows.runner import SecretServerRunner
from plugins.configuration import Configuration

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
        app_id='59971200755',
    )
    
    '''
    TODO : should not be hard coded token - fix later
    client_id=getenv("SECRET_SERVER_CLIENT_ID"),
    client_secret=getenv("SECRET_SERVER_CLIENT_SECRET"),
    '''
    shared_configuration = SecretServerSharedConfiguration()
    client_configuration = SecretServerConfiguration(configuration=Configuration(host = "https://integrations.secretservercloud.com//api",
                                                                                 api_key = {'BearerToken': ''}))

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
   # health_checker.raise_unhealthy()
    workflow_run.run()


example()
