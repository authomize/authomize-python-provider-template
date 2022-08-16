"""Tests for extractors"""
from hamcrest import assert_that

from extractors.testing_client import create_microsoft_client
from mock_provider.configuration.shared_configuration import MockProviderSharedConfiguration
from mock_provider.models.shared_memory import MockProviderSharedMemory
from teams_provider.extractors.groups_extractor import GroupsExtractor
from teams_provider.models.shared_memory import TeamsProviderSharedMemory


def _create_extractor(files_to_extract: int = 10) -> GroupsExtractor:
    """Create a NON MOCKED EXTRACTOR for testing"""
    client = create_microsoft_client()

    return GroupsExtractor(
        client,
        shared_memory=TeamsProviderSharedMemory(),
        shared_configuration=MockProviderSharedConfiguration(
            extractor_logs_every_n_raw_items=3,
            files_to_extract=files_to_extract,
        ),
    )


def test_groups_extractor():
    extractor = _create_extractor()
    print(list(extractor.extract_raw()))
    assert_that(len(extractor.shared_memory.teams) > 0)
