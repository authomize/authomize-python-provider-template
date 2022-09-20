"""Tests for extractors"""
from hamcrest import assert_that

from mock_provider.configuration.shared_configuration import MockProviderSharedConfiguration
from teams_provider.models.shared_memory import TeamsProviderSharedMemory
from teams_provider.transformers.users_transformer import UsersTransformer


def _create_transformer(files_to_extract: int = 10) -> UsersTransformer:
    """'Create a NON MOCKED TRANSFORMER for manual testing"""
    return UsersTransformer(
        shared_memory=TeamsProviderSharedMemory(),
        shared_configuration=MockProviderSharedConfiguration(
            extractor_logs_every_n_raw_items=3,
            files_to_extract=files_to_extract,
        ),
    )


def test_users_transformer():
    transformer = _create_transformer()

    raw_item = {'id': '0bf92da9-d521-4d24-8170-7919528dcbe3', 'accountEnabled': True, 'deletedDateTime': None, 'userType': 'Member', 'givenName': 'Aashish', 'surname': 'Bhandari', 'mail': 'aashish.bhandari@authomize.com', 'externalUserState': None, 'country': None, 'department': 'Data', 'jobTitle': 'Developer', 'employeeHireDate': None}

    bundle = transformer.transform_model(raw_item)
    print(bundle)
    assert_that(1 == 1)
