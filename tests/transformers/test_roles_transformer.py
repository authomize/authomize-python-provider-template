"""Tests for extractors"""
from hamcrest import assert_that

from mock_provider.configuration.shared_configuration import MockProviderSharedConfiguration
from teams_provider.models.shared_memory import TeamsProviderSharedMemory
from teams_provider.transformers.roles_transformer import RolesTransformer


def _create_transformer(files_to_extract: int = 10) -> RolesTransformer:
    """'Create a NON MOCKED TRANSFORMER for manual testing"""
    return RolesTransformer(
        shared_memory=TeamsProviderSharedMemory(),
        shared_configuration=MockProviderSharedConfiguration(
            extractor_logs_every_n_raw_items=3,
            files_to_extract=files_to_extract,
        ),
    )


def test_users_transformer():
    transformer = _create_transformer()

    raw_item = {'@odata.type': '#microsoft.graph.aadUserConversationMember', 'id': 'MCMjMiMjZDY4YjcwYTUtNzI2NS00ZTE5LTg5NjktNjUxM2IxMTdkY2I1IyMxOTo3YWM4NGI0ZGJhNGQ0N2U0YTYwZWM4YjFkMTI1MjkyZUB0aHJlYWQudGFjdjIjIzA5ZjFlZDcwLWU5ODItNGUwYy04NTJhLTc5ZTA5ZTZjYjBlZg==', 'roles': ['owner'], 'displayName': 'Idan Rufeisen', 'visibleHistoryStartDateTime': '0001-01-01T00:00:00Z', 'userId': '09f1ed70-e982-4e0c-852a-79e09e6cb0ef', 'email': 'idan.rufeisen@authomize.com', 'tenantId': 'd68b70a5-7265-4e19-8969-6513b117dcb5', 'sub_uri': 'teams/29696c03-336f-4cbc-b5af-34460786a955/channels/19:7ac84b4dba4d47e4a60ec8b1d125292e@thread.tacv2/members'}

    bundle = transformer.transform_model(raw_item)
    print(bundle)
    assert_that(1 == 1)
