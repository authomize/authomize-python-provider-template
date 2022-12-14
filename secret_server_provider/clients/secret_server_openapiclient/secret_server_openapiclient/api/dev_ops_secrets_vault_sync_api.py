"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from secret_server_openapiclient.api_client import ApiClient, Endpoint as _Endpoint
from secret_server_openapiclient.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from secret_server_openapiclient.model.authentication_failed_response import AuthenticationFailedResponse
from secret_server_openapiclient.model.bad_request_response import BadRequestResponse
from secret_server_openapiclient.model.dev_ops_secrets_vault_create_sync_args import DevOpsSecretsVaultCreateSyncArgs
from secret_server_openapiclient.model.dev_ops_secrets_vault_sync_secrets_args import DevOpsSecretsVaultSyncSecretsArgs
from secret_server_openapiclient.model.dev_ops_secrets_vault_sync_status_model import DevOpsSecretsVaultSyncStatusModel
from secret_server_openapiclient.model.dev_ops_secrets_vault_sync_status_view_model import DevOpsSecretsVaultSyncStatusViewModel
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_dev_ops_secrets_vault_sync_status_summary import PagingOfDevOpsSecretsVaultSyncStatusSummary


class DevOpsSecretsVaultSyncApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.dev_ops_secrets_vault_sync_service_create_sync_endpoint = _Endpoint(
            settings={
                'response_type': (DevOpsSecretsVaultSyncStatusModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/devops-secrets-vault/add-sync',
                'operation_id': 'dev_ops_secrets_vault_sync_service_create_sync',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'dev_ops_secrets_vault_create_sync_args',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'dev_ops_secrets_vault_create_sync_args':
                        (DevOpsSecretsVaultCreateSyncArgs,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'dev_ops_secrets_vault_create_sync_args': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.dev_ops_secrets_vault_sync_service_get_sync_status_endpoint = _Endpoint(
            settings={
                'response_type': (DevOpsSecretsVaultSyncStatusModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/devops-secrets-vault/sync/status/{syncMapId}',
                'operation_id': 'dev_ops_secrets_vault_sync_service_get_sync_status',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'sync_map_id',
                ],
                'required': [
                    'sync_map_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'sync_map_id':
                        (int,),
                },
                'attribute_map': {
                    'sync_map_id': 'syncMapId',
                },
                'location_map': {
                    'sync_map_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.dev_ops_secrets_vault_sync_service_get_sync_statuses_endpoint = _Endpoint(
            settings={
                'response_type': (PagingOfDevOpsSecretsVaultSyncStatusSummary,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/devops-secrets-vault/sync/status',
                'operation_id': 'dev_ops_secrets_vault_sync_service_get_sync_statuses',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'filter_include_inactive',
                    'filter_secret_id',
                    'filter_tenant_id',
                    'skip',
                    'sort_by_0_direction',
                    'sort_by_0_name',
                    'sort_by_0_priority',
                    'take',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'filter_include_inactive':
                        (bool,),
                    'filter_secret_id':
                        (int,),
                    'filter_tenant_id':
                        (int,),
                    'skip':
                        (int,),
                    'sort_by_0_direction':
                        (str,),
                    'sort_by_0_name':
                        (str,),
                    'sort_by_0_priority':
                        (int,),
                    'take':
                        (int,),
                },
                'attribute_map': {
                    'filter_include_inactive': 'filter.includeInactive',
                    'filter_secret_id': 'filter.secretId',
                    'filter_tenant_id': 'filter.tenantId',
                    'skip': 'skip',
                    'sort_by_0_direction': 'sortBy[0].direction',
                    'sort_by_0_name': 'sortBy[0].name',
                    'sort_by_0_priority': 'sortBy[0].priority',
                    'take': 'take',
                },
                'location_map': {
                    'filter_include_inactive': 'query',
                    'filter_secret_id': 'query',
                    'filter_tenant_id': 'query',
                    'skip': 'query',
                    'sort_by_0_direction': 'query',
                    'sort_by_0_name': 'query',
                    'sort_by_0_priority': 'query',
                    'take': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.dev_ops_secrets_vault_sync_service_sync_secret_endpoint = _Endpoint(
            settings={
                'response_type': ([DevOpsSecretsVaultSyncStatusViewModel],),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/devops-secrets-vault/sync',
                'operation_id': 'dev_ops_secrets_vault_sync_service_sync_secret',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'dev_ops_secrets_vault_sync_secrets_args',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'dev_ops_secrets_vault_sync_secrets_args':
                        (DevOpsSecretsVaultSyncSecretsArgs,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'dev_ops_secrets_vault_sync_secrets_args': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.dev_ops_secrets_vault_sync_service_update_sync_endpoint = _Endpoint(
            settings={
                'response_type': (DevOpsSecretsVaultSyncStatusModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/devops-secrets-vault/sync/{syncSecretMapId}',
                'operation_id': 'dev_ops_secrets_vault_sync_service_update_sync',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'sync_secret_map_id',
                    'dev_ops_secrets_vault_create_sync_args',
                ],
                'required': [
                    'sync_secret_map_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'sync_secret_map_id':
                        (int,),
                    'dev_ops_secrets_vault_create_sync_args':
                        (DevOpsSecretsVaultCreateSyncArgs,),
                },
                'attribute_map': {
                    'sync_secret_map_id': 'syncSecretMapId',
                },
                'location_map': {
                    'sync_secret_map_id': 'path',
                    'dev_ops_secrets_vault_create_sync_args': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def dev_ops_secrets_vault_sync_service_create_sync(
        self,
        **kwargs
    ):
        """Create a DevOps sync for a secret.  # noqa: E501

        Create a sync between a secret and a DevOps Secrets Vault tenant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.dev_ops_secrets_vault_sync_service_create_sync(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            dev_ops_secrets_vault_create_sync_args (DevOpsSecretsVaultCreateSyncArgs): args. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DevOpsSecretsVaultSyncStatusModel
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.dev_ops_secrets_vault_sync_service_create_sync_endpoint.call_with_http_info(**kwargs)

    def dev_ops_secrets_vault_sync_service_get_sync_status(
        self,
        sync_map_id,
        **kwargs
    ):
        """Information about secret syncing.  # noqa: E501

        Get which tenants a secret is syncing to, the current status of the sync, and the last sync time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.dev_ops_secrets_vault_sync_service_get_sync_status(sync_map_id, async_req=True)
        >>> result = thread.get()

        Args:
            sync_map_id (int): syncMapId

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DevOpsSecretsVaultSyncStatusModel
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['sync_map_id'] = \
            sync_map_id
        return self.dev_ops_secrets_vault_sync_service_get_sync_status_endpoint.call_with_http_info(**kwargs)

    def dev_ops_secrets_vault_sync_service_get_sync_statuses(
        self,
        **kwargs
    ):
        """Information about secrets syncing.  # noqa: E501

        Get which tenants the secrets are syncing to, the current status of the sync, and the last sync time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.dev_ops_secrets_vault_sync_service_get_sync_statuses(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            filter_include_inactive (bool): If inactive sync maps should be returned.. [optional]
            filter_secret_id (int): Search by the secret being synced.. [optional]
            filter_tenant_id (int): Search by the tenant being pushed to.. [optional]
            skip (int): Number of records to skip before taking results. [optional]
            sort_by_0_direction (str): Sort direction. [optional]
            sort_by_0_name (str): Sort field name. [optional]
            sort_by_0_priority (int): Priority index. Sorts with lower values are executed earlier. [optional]
            take (int): Maximum number of records to include in results. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PagingOfDevOpsSecretsVaultSyncStatusSummary
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.dev_ops_secrets_vault_sync_service_get_sync_statuses_endpoint.call_with_http_info(**kwargs)

    def dev_ops_secrets_vault_sync_service_sync_secret(
        self,
        **kwargs
    ):
        """Sync a secret.  # noqa: E501

        Sync a secret to a DevOps Secrets Vault tenant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.dev_ops_secrets_vault_sync_service_sync_secret(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            dev_ops_secrets_vault_sync_secrets_args (DevOpsSecretsVaultSyncSecretsArgs): args. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [DevOpsSecretsVaultSyncStatusViewModel]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.dev_ops_secrets_vault_sync_service_sync_secret_endpoint.call_with_http_info(**kwargs)

    def dev_ops_secrets_vault_sync_service_update_sync(
        self,
        sync_secret_map_id,
        **kwargs
    ):
        """Update a secret sync.  # noqa: E501

        Update a sync between a secret and a DevOps Secrets Vault tenant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.dev_ops_secrets_vault_sync_service_update_sync(sync_secret_map_id, async_req=True)
        >>> result = thread.get()

        Args:
            sync_secret_map_id (int): syncSecretMapId

        Keyword Args:
            dev_ops_secrets_vault_create_sync_args (DevOpsSecretsVaultCreateSyncArgs): args. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DevOpsSecretsVaultSyncStatusModel
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['sync_secret_map_id'] = \
            sync_secret_map_id
        return self.dev_ops_secrets_vault_sync_service_update_sync_endpoint.call_with_http_info(**kwargs)

