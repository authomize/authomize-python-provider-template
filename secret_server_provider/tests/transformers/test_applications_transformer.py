from types import NoneType

from authomize.rest_api_client.generated.schemas import (
    NewAssetRequestSchema,
    NewUserRequestSchema,
    UserStatus,
)
from hamcrest import assert_that, equal_to, is_
from secret_server_openapiclient.model.multifactor_authentication_provider_types import (
    MultifactorAuthenticationProviderTypes,
)
from secret_server_openapiclient.model.user_summary import UserSummary

from secret_server_provider.configuration.shared_configuration import (
    SecretServerSharedConfiguration,
)
from secret_server_provider.models.shared_memory import SecretServerProviderSharedMemory
from secret_server_provider.transformers.users_transformer import UsersTransformer

# positive test with none two factor
MOCK_RAW_ITEM = UserSummary(
    id=15.0,
    user_name="AuthomizeSE_App",
    last_login="0001-01-01T00:00:00",
    display_name="AuthomizeSE_App",
    enabled=True,
    two_factor_method=MultifactorAuthenticationProviderTypes('None'),
    email_address = "AuthomizeSE_App1@something.com",
)

def mock_shared_memory() -> SecretServerProviderSharedMemory:
    return SecretServerProviderSharedMemory()


def mock_shared_configuration() -> SecretServerSharedConfiguration:
    return SecretServerSharedConfiguration()


def create_transformer() -> UsersTransformer:
    return UsersTransformer(
        shared_memory=mock_shared_memory(),
        shared_configuration=mock_shared_configuration(),
    )


def test_validate_item_schema():
    transformer = create_transformer()
    mock_raw_item = dict()
    assert_that(
        transformer.validate_item_schema(mock_raw_item),
        is_(True),
    )


def test_transform_model():
    transformer = create_transformer()
    expected_result = UsersTransformer.create_bundle(
        new_users=[
            NewUserRequestSchema(
                uniqueId="15",
                name="AuthomizeSE_App",
                display_name="AuthomizeSE App",
                status = UserStatus.Enabled,
                hasMFA = False,
                email = "AuthomizeSE_App1@something.com",
                lastLoginAt = "0001-01-01T00:00:00",
            ),
        ],
    )
    assert_that(
        transformer.transform_model(MOCK_RAW_ITEM),
        is_(equal_to(
            expected_result.dict(),
        )),
    )
