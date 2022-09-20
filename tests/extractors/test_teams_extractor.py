"""Tests for extractors"""
from hamcrest import assert_that

from extractors.testing_client import create_microsoft_client
from mock_provider.configuration.shared_configuration import MockProviderSharedConfiguration
from teams_provider.extractors.teams_extractor import TeamsExtractor
from teams_provider.models.shared_memory import TeamsProviderSharedMemory


def _create_extractor(files_to_extract: int = 10) -> TeamsExtractor:
    """'Create a NON MOCKED EXTRACTOR for manual testing"""
    client = create_microsoft_client()

    return TeamsExtractor(
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
    assert_that(len(extractor.shared_memory.team_ids) > 0)
