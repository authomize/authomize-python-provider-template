from base_provider.configuration.base_client_configuration import BaseClientConfiguration
from plugins.configuration import Configuration
from plugins.api import users_api,groups_api,roles_api
from plugins.model.current_user_model import CurrentUserModel 
from plugins.model.internal_server_error_response import InternalServerErrorResponse
from plugins.model.authentication_failed_response import AuthenticationFailedResponse
from plugins.model.bad_request_response import BadRequestResponse


class SecretServerConfiguration(BaseClientConfiguration):
    def __init__(self):
        super().__init__()
        self.configuration = Configuration(host = "https://integrations.secretservercloud.com//api")
        # TODO remove hardcoded token 
        self.configuration.api_key['BearerToken']='bearer AgIfnV_2OEqnWPleeq57MgELfDZMOE9jzyL8W5H7hauYyEw8JlRMVUCA9wLYeFCpo-ZD6uah54Ve2a01gy9v2TXJDkwn2ZOqwNY3gRlutdUKB9qNpFaJZuBOHRRddXSgPbt5WTSLmZ8yl4_7ExTDHGpaEBx0cT6PvsN6S0dcTlNbeiEINpgIHLlQ9wuztIqisSXk2YY3dFBKlJ0AUL1fRNFXlEkXCB1cSuu9s-DXq7ZJtj07cPMTudTD2RWnK5HqngiXlpkROB9FrE-_SzLt45xkS67X2_G8mHFPNGX60sGGAzidr4RDkuilxcBvF5FC-xVTmtHkD8_8-tzvur54UHNA2W8dnFYfVE2_i2ZhZaMHXeETcwr2_YojS4dNBe6sEJEYo-Okf1qbrBvWenJGdvgk3vyplTlFfca7VmOu7_EReIlZtLNiTae8hJeT_wsm6NG1hsQs7R_0JCEXGD_b6qNvRJkgh9hfzrhq-OxudsWLMRtbNeboNloYkyEOMxN3HCtnnPIH1bN7rkGWr25TRX1uQoVVF-7tcY8s5RhG-R9qCDxlgXsdaEUVc2yNvisV65pE4c5L0CRB9C_egVC5yF5S'
