"""Tests for extractors"""
from unittest.mock import MagicMock, patch

from hamcrest import assert_that, equal_to, is_

from mock_provider.clients.client import MockProviderClient
from mock_provider.configuration.client_configuration import MockProviderClientConfiguration
from mock_provider.configuration.shared_configuration import MockProviderSharedConfiguration
from mock_provider.extractors.files_extractor import FilesExtactor
from mock_provider.models.shared_memory import MockProviderSharedMemory


def create_extractor(files_to_extract: int = 10) -> FilesExtactor:
    """Create a simple mocked extractor"""
    return FilesExtactor(
        data_provider_client=MockProviderClient(
            client_configuration=MockProviderClientConfiguration(
                base_url='https://mock.example',
                domain='mock-domain-1',
                token='secret',
            ),
        ),
        shared_memory=MockProviderSharedMemory(domain='mock-domain-2'),
        shared_configuration=MockProviderSharedConfiguration(
            extactor_logs_every_n_raw_items=3,
            files_to_extract=files_to_extract,
        ),
    )


def test_log_every_n_fetches():
    extractor_with_some_results = create_extractor(files_to_extract=10)
    with patch.object(
        extractor_with_some_results,
        '_log_progress',
        MagicMock(),
    ) as log_progress:
        list(extractor_with_some_results())
        assert_that(
            log_progress.call_count,
            is_(equal_to(3)),
        )
