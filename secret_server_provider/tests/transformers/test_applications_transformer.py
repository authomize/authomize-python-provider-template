from authomize.rest_api_client.generated.schemas import NewAssetRequestSchema
from hamcrest import assert_that, equal_to, is_
from onelogin.api.models.app import App
from onelogin_provider.configuration.shared_configuration import OneloginSharedConfiguration
from onelogin_provider.models.shared_memory import OneloginProviderSharedMemory
from onelogin_provider.transformers.applications_transformer import ApplicationsTransformer

MOCK_RAW_ITEM = App(dict(
    id='mock-app-id',
    name='mock-app-name',
))


def mock_shared_memory() -> OneloginProviderSharedMemory:
    return OneloginProviderSharedMemory()


def mock_shared_configuration() -> OneloginSharedConfiguration:
    return OneloginSharedConfiguration()


def create_transformer() -> ApplicationsTransformer:
    return ApplicationsTransformer(
        shared_memory=mock_shared_memory(),
        shared_configuration=mock_shared_configuration(),
    )


def test_validate_item_schema():
    transformer = create_transformer()
    mock_raw_item = App(dict())
    assert_that(
        transformer.validate_item_schema(mock_raw_item),
        is_(True),
    )


def test_transform_model():
    transformer = create_transformer()
    expected_result = ApplicationsTransformer.create_bundle(
        new_assets=[
            NewAssetRequestSchema(
                id=MOCK_RAW_ITEM.id,
                name=MOCK_RAW_ITEM.name,
            ),
        ],
    )
    assert_that(
        transformer.transform_model(MOCK_RAW_ITEM),
        is_(equal_to(
            expected_result.dict(),
        )),
    )
