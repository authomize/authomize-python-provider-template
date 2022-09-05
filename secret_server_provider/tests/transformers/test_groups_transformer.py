from authomize.rest_api_client.generated.schemas import GroupingType, NewGroupingRequestSchema
from hamcrest import assert_that, equal_to, is_
from secret_server_openapiclient.model.group_model import GroupModel

from secret_server_provider.configuration.shared_configuration import (
    SecretServerSharedConfiguration,
)
from secret_server_provider.models.shared_memory import SecretServerProviderSharedMemory
from secret_server_provider.transformers.groups_transformer import GroupsTransformer

# positive test with none two factor
MOCK_RAW_ITEM = GroupModel(
    id=10.0,
    name="Authomize",
    enabled=True,
)


def mock_shared_memory() -> SecretServerProviderSharedMemory:
    return SecretServerProviderSharedMemory()


def mock_shared_configuration() -> SecretServerSharedConfiguration:
    return SecretServerSharedConfiguration()


def create_transformer() -> GroupsTransformer:
    return GroupsTransformer(
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
    expected_result = GroupsTransformer.create_bundle(
        new_groupings=[
            NewGroupingRequestSchema(
                uniqueId="10",
                name="Authomize",
                type=GroupingType.Group,
                isRole=False,
            ),
        ],
    )
    assert_that(
        transformer.transform_model(MOCK_RAW_ITEM),
        is_(equal_to(
            expected_result.dict(),
        )),
    )
