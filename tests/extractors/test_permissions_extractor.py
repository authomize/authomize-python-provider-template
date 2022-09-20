"""Tests for extractors"""

from extractors.testing_client import create_microsoft_client
from mock_provider.configuration.shared_configuration import MockProviderSharedConfiguration
from teams_provider.extractors.permissions_extractor import PermissionsExtractor
from teams_provider.models.shared_memory import TeamsProviderSharedMemory


def _create_extractor(files_to_extract: int = 10) -> PermissionsExtractor:
    """'Create a NON MOCKED EXTRACTOR for manual testing"""
    client = create_microsoft_client()
    shared_memory = TeamsProviderSharedMemory()
    shared_memory.team_ids.extend(['29696c03-336f-4cbc-b5af-34460786a955', 'daf1d88d-f80a-45e4-8f5e-d2afb9d7f4f4'])
    return PermissionsExtractor(
        client,
        shared_memory=shared_memory,
        shared_configuration=MockProviderSharedConfiguration(
            extractor_logs_every_n_raw_items=3,
            files_to_extract=files_to_extract,
        ),
    )


def test_permissions_extractor():
    extractor = _create_extractor()
    print(list(extractor.extract_raw()))
