"""Tests for extractors"""

from extractors.testing_client import create_microsoft_client
from mock_provider.configuration.shared_configuration import MockProviderSharedConfiguration
from teams_provider.extractors.roles_extractor import RolesExtractor
from teams_provider.models.shared_memory import TeamsProviderSharedMemory


def _create_extractor(files_to_extract: int = 10) -> RolesExtractor:
    """'Create a NON MOCKED EXTRACTOR for manual testing"""
    client = create_microsoft_client()
    shared_memory = TeamsProviderSharedMemory()
    shared_memory.team_ids.extend(['29696c03-336f-4cbc-b5af-34460786a955', 'daf1d88d-f80a-45e4-8f5e-d2afb9d7f4f4'])
    shared_memory.team_id_to_channel_ids['29696c03-336f-4cbc-b5af-34460786a955'] = [
        '19:7ac84b4dba4d47e4a60ec8b1d125292e@thread.tacv2', '19:bf259689ccd54cb3bc47a3ab0b6744f8@thread.tacv2',
        '19:UMw5hLDZ8TKw9-3jJoSX40aAtPZzh3muMlQ2jiXNqfs1@thread.tacv2'
    ]
    shared_memory.team_id_to_channel_ids['daf1d88d-f80a-45e4-8f5e-d2afb9d7f4f4'] = [
        '19:3b54e5f8127c4912a6d4c9757f1310d1@thread.tacv2']
    return RolesExtractor(
        client,
        shared_memory=shared_memory,
        shared_configuration=MockProviderSharedConfiguration(
            extractor_logs_every_n_raw_items=3,
            files_to_extract=files_to_extract,
        ),
    )


def test_roles_extractor():
    extractor = _create_extractor()
    print(list(extractor.extract_raw()))
