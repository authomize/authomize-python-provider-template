from authomize.rest_api_client.generated.schemas import NewAssetsRequestSchema
from hamcrest import assert_that, equal_to, is_
from onelogin.api.models.app import App

from onelogin_provider.transformers.applications_transformer import ApplicationsTransformer

MOCK_RAW_ITEM = App(dict(
    id='mock-app-id',
    name='mock-app-name',
))


def test_validate_item_schema():
    transformer = ApplicationsTransformer(shared_memory=None)
    mock_raw_item = App(dict())
    assert_that(
        transformer.validate_item_schema(mock_raw_item),
        is_(True),
    )


def test_transform_model():
    transformer = ApplicationsTransformer(shared_memory=None)
    expected_result = ApplicationsTransformer.create_bundle(
        new_assets=[
            NewAssetsRequestSchema(
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
