from base_provider.configuration.base_client_configuration import BaseClientConfiguration
from plugins.configuration import Configuration
from plugins.api import users_api,groups_api,roles_api
from plugins.model.current_user_model import CurrentUserModel 
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse



class SecretServerConfiguration(BaseClientConfiguration):
    configuration : Configuration
 