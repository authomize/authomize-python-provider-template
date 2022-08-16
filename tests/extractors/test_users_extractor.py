"""Tests for extractors"""
from hamcrest import assert_that

from extractors.testing_client import create_microsoft_client
from mock_provider.configuration.shared_configuration import MockProviderSharedConfiguration
from teams_provider.extractors.users_extractor import UsersExtractor
from teams_provider.models.shared_memory import TeamsProviderSharedMemory


def _create_extractor(files_to_extract: int = 10) -> UsersExtractor:
    """Create a NON MOCKED EXTRACTOR for testing"""
    client = create_microsoft_client()

    return UsersExtractor(
        client,
        shared_memory=TeamsProviderSharedMemory(),
        shared_configuration=MockProviderSharedConfiguration(
            extractor_logs_every_n_raw_items=3,
            files_to_extract=files_to_extract,
        ),
    )


def test_users_extractor():
    extractor = _create_extractor()
    print(list(extractor.extract_raw()))
    assert_that(1 == 1)
