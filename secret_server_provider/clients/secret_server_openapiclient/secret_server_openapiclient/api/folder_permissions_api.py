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
from secret_server_openapiclient.model.deleted_model import DeletedModel
from secret_server_openapiclient.model.folder_permission_create_args import FolderPermissionCreateArgs
from secret_server_openapiclient.model.folder_permission_model import FolderPermissionModel
from secret_server_openapiclient.model.folder_permission_update_args import FolderPermissionUpdateArgs
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_folder_permission_summary import PagingOfFolderPermissionSummary


class FolderPermissionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.folder_permissions_service_create_endpoint = _Endpoint(
            settings={
                'response_type': (FolderPermissionModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/folder-permissions',
                'operation_id': 'folder_permissions_service_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'folder_permission_create_args',
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
                    'folder_permission_create_args':
                        (FolderPermissionCreateArgs,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'folder_permission_create_args': 'body',
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
        self.folder_permissions_service_delete_endpoint = _Endpoint(
            settings={
                'response_type': (DeletedModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/folder-permissions/{id}',
                'operation_id': 'folder_permissions_service_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'break_inheritance',
                ],
                'required': [
                    'id',
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
                    'id':
                        (int,),
                    'break_inheritance':
                        (bool,),
                },
                'attribute_map': {
                    'id': 'id',
                    'break_inheritance': 'breakInheritance',
                },
                'location_map': {
                    'id': 'path',
                    'break_inheritance': 'query',
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
        self.folder_permissions_service_get_endpoint = _Endpoint(
            settings={
                'response_type': (FolderPermissionModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/folder-permissions/{id}',
                'operation_id': 'folder_permissions_service_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'include_inactive',
                ],
                'required': [
                    'id',
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
                    'id':
                        (int,),
                    'include_inactive':
                        (bool,),
                },
                'attribute_map': {
                    'id': 'id',
                    'include_inactive': 'includeInactive',
                },
                'location_map': {
                    'id': 'path',
                    'include_inactive': 'query',
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
        self.folder_permissions_service_search_endpoint = _Endpoint(
            settings={
                'response_type': (PagingOfFolderPermissionSummary,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/folder-permissions',
                'operation_id': 'folder_permissions_service_search',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'filter_exclude_editors',
                    'filter_exclude_owners',
                    'filter_exclude_viewers',
                    'filter_folder_id',
                    'filter_group_id',
                    'filter_user_id',
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
                    'filter_exclude_editors':
                        (bool,),
                    'filter_exclude_owners':
                        (bool,),
                    'filter_exclude_viewers':
                        (bool,),
                    'filter_folder_id':
                        (int,),
                    'filter_group_id':
                        (int,),
                    'filter_user_id':
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
                    'filter_exclude_editors': 'filter.excludeEditors',
                    'filter_exclude_owners': 'filter.excludeOwners',
                    'filter_exclude_viewers': 'filter.excludeViewers',
                    'filter_folder_id': 'filter.folderId',
                    'filter_group_id': 'filter.groupId',
                    'filter_user_id': 'filter.userId',
                    'skip': 'skip',
                    'sort_by_0_direction': 'sortBy[0].direction',
                    'sort_by_0_name': 'sortBy[0].name',
                    'sort_by_0_priority': 'sortBy[0].priority',
                    'take': 'take',
                },
                'location_map': {
                    'filter_exclude_editors': 'query',
                    'filter_exclude_owners': 'query',
                    'filter_exclude_viewers': 'query',
                    'filter_folder_id': 'query',
                    'filter_group_id': 'query',
                    'filter_user_id': 'query',
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
        self.folder_permissions_service_stub_endpoint = _Endpoint(
            settings={
                'response_type': (FolderPermissionModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/folder-permissions/stub',
                'operation_id': 'folder_permissions_service_stub',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'folder_id',
                ],
                'required': [
                    'folder_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'folder_id',
                ]
            },
            root_map={
                'validations': {
                    ('folder_id',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'folder_id':
                        (int,),
                },
                'attribute_map': {
                    'folder_id': 'folderId',
                },
                'location_map': {
                    'folder_id': 'query',
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
        self.folder_permissions_service_update_endpoint = _Endpoint(
            settings={
                'response_type': (FolderPermissionModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/folder-permissions/{id}',
                'operation_id': 'folder_permissions_service_update',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'folder_permission_update_args',
                ],
                'required': [
                    'id',
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
                    'id':
                        (int,),
                    'folder_permission_update_args':
                        (FolderPermissionUpdateArgs,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                    'folder_permission_update_args': 'body',
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

    def folder_permissions_service_create(
        self,
        **kwargs
    ):
        """Create Folder Permission  # noqa: E501

        Create a new folder permission  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.folder_permissions_service_create(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            folder_permission_create_args (FolderPermissionCreateArgs): Folder permission creation options. [optional]
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
            FolderPermissionModel
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
        return self.folder_permissions_service_create_endpoint.call_with_http_info(**kwargs)

    def folder_permissions_service_delete(
        self,
        id,
        **kwargs
    ):
        """Delete Folder Permission  # noqa: E501

        Delete a folder permission by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.folder_permissions_service_delete(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (int): Folder permission ID

        Keyword Args:
            break_inheritance (bool): Include to remove permission inheritance. [optional]
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
            DeletedModel
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
        kwargs['id'] = \
            id
        return self.folder_permissions_service_delete_endpoint.call_with_http_info(**kwargs)

    def folder_permissions_service_get(
        self,
        id,
        **kwargs
    ):
        """Get Folder Permission  # noqa: E501

        Get a single folder permission by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.folder_permissions_service_get(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (int): Folder permission ID

        Keyword Args:
            include_inactive (bool): Whether to include inactive folder permissions in the results. [optional]
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
            FolderPermissionModel
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
        kwargs['id'] = \
            id
        return self.folder_permissions_service_get_endpoint.call_with_http_info(**kwargs)

    def folder_permissions_service_search(
        self,
        **kwargs
    ):
        """Search Folder Permissions  # noqa: E501

        Search, filter, sort, and page folder permissions  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.folder_permissions_service_search(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            filter_exclude_editors (bool): If populated with true, will filter editors from results. Will default to false. [optional]
            filter_exclude_owners (bool): If populated with true, will filter owners from results. Will default to false. [optional]
            filter_exclude_viewers (bool): If populated with true, will filter viewers from results. Will default to false. [optional]
            filter_folder_id (int): Limit results to a certain folder. [optional]
            filter_group_id (int): Limit results to a certain group. [optional]
            filter_user_id (int): Limit results to a certain user. [optional]
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
            PagingOfFolderPermissionSummary
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
        return self.folder_permissions_service_search_endpoint.call_with_http_info(**kwargs)

    def folder_permissions_service_stub(
        self,
        folder_id,
        **kwargs
    ):
        """Get Folder Permission Stub  # noqa: E501

        Return the default values for a new folder permission  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.folder_permissions_service_stub(folder_id, async_req=True)
        >>> result = thread.get()

        Args:
            folder_id (int): Folder for which to generate a permission stub

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
            FolderPermissionModel
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
        kwargs['folder_id'] = \
            folder_id
        return self.folder_permissions_service_stub_endpoint.call_with_http_info(**kwargs)

    def folder_permissions_service_update(
        self,
        id,
        **kwargs
    ):
        """Update Folder Permission  # noqa: E501

        Update a single folder permission by ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.folder_permissions_service_update(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (int): Folder permission ID

        Keyword Args:
            folder_permission_update_args (FolderPermissionUpdateArgs): Folder permission update options. [optional]
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
            FolderPermissionModel
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
        kwargs['id'] = \
            id
        return self.folder_permissions_service_update_endpoint.call_with_http_info(**kwargs)

