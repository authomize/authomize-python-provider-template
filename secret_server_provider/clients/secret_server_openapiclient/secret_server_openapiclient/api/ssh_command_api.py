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
from secret_server_openapiclient.model.internal_server_error_response import InternalServerErrorResponse
from secret_server_openapiclient.model.paging_of_ssh_command_summary_model import PagingOfSshCommandSummaryModel
from secret_server_openapiclient.model.ssh_command_create_args import SshCommandCreateArgs
from secret_server_openapiclient.model.ssh_command_dto import SshCommandDto
from secret_server_openapiclient.model.ssh_command_model import SshCommandModel
from secret_server_openapiclient.model.ssh_command_patch_args import SshCommandPatchArgs


class SshCommandApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.ssh_command_service_create_ssh_command_endpoint = _Endpoint(
            settings={
                'response_type': (SshCommandModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/ssh-command',
                'operation_id': 'ssh_command_service_create_ssh_command',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ssh_command_create_args',
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
                    'ssh_command_create_args':
                        (SshCommandCreateArgs,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'ssh_command_create_args': 'body',
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
        self.ssh_command_service_get_ssh_command_endpoint = _Endpoint(
            settings={
                'response_type': (SshCommandModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/ssh-command/{id}',
                'operation_id': 'ssh_command_service_get_ssh_command',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
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
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
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
        self.ssh_command_service_get_ssh_command_stub_endpoint = _Endpoint(
            settings={
                'response_type': (SshCommandDto,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/ssh-command/stub',
                'operation_id': 'ssh_command_service_get_ssh_command_stub',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
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
                },
                'attribute_map': {
                },
                'location_map': {
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
        self.ssh_command_service_get_ssh_commands_endpoint = _Endpoint(
            settings={
                'response_type': (PagingOfSshCommandSummaryModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/ssh-command/list',
                'operation_id': 'ssh_command_service_get_ssh_commands',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'filter_command_permission_type',
                    'filter_name_or_command',
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
                    'filter_command_permission_type':
                        (str,),
                    'filter_name_or_command':
                        (str,),
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
                    'filter_command_permission_type': 'filter.commandPermissionType',
                    'filter_name_or_command': 'filter.nameOrCommand',
                    'skip': 'skip',
                    'sort_by_0_direction': 'sortBy[0].direction',
                    'sort_by_0_name': 'sortBy[0].name',
                    'sort_by_0_priority': 'sortBy[0].priority',
                    'take': 'take',
                },
                'location_map': {
                    'filter_command_permission_type': 'query',
                    'filter_name_or_command': 'query',
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
        self.ssh_command_service_update_ssh_command_endpoint = _Endpoint(
            settings={
                'response_type': (SshCommandModel,),
                'auth': [
                    'BearerToken'
                ],
                'endpoint_path': '/v1/ssh-command/{sshCommandId}',
                'operation_id': 'ssh_command_service_update_ssh_command',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'ssh_command_id',
                    'ssh_command_patch_args',
                ],
                'required': [
                    'ssh_command_id',
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
                    'ssh_command_id':
                        (str,),
                    'ssh_command_patch_args':
                        (SshCommandPatchArgs,),
                },
                'attribute_map': {
                    'ssh_command_id': 'sshCommandId',
                },
                'location_map': {
                    'ssh_command_id': 'path',
                    'ssh_command_patch_args': 'body',
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

    def ssh_command_service_create_ssh_command(
        self,
        **kwargs
    ):
        """Add an SSH Command  # noqa: E501

        Add an SSH Command  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ssh_command_service_create_ssh_command(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            ssh_command_create_args (SshCommandCreateArgs): SSH Command add options. [optional]
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
            SshCommandModel
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
        return self.ssh_command_service_create_ssh_command_endpoint.call_with_http_info(**kwargs)

    def ssh_command_service_get_ssh_command(
        self,
        id,
        **kwargs
    ):
        """Get an SSH Command  # noqa: E501

        Returns the SSH Command for the provided ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ssh_command_service_get_ssh_command(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (int): SSH Command ID

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
            SshCommandModel
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
        return self.ssh_command_service_get_ssh_command_endpoint.call_with_http_info(**kwargs)

    def ssh_command_service_get_ssh_command_stub(
        self,
        **kwargs
    ):
        """Stub an empty SSH Command  # noqa: E501

        Returns an empty SSH Command to be filled out.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ssh_command_service_get_ssh_command_stub(async_req=True)
        >>> result = thread.get()


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
            SshCommandDto
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
        return self.ssh_command_service_get_ssh_command_stub_endpoint.call_with_http_info(**kwargs)

    def ssh_command_service_get_ssh_commands(
        self,
        **kwargs
    ):
        """Get a list of SSH Commands  # noqa: E501

        Returns a list of SSH Commands that meet the paging/searching critera  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ssh_command_service_get_ssh_commands(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            filter_command_permission_type (str): CommandPermissionType. [optional]
            filter_name_or_command (str): NameOrCommand. [optional]
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
            PagingOfSshCommandSummaryModel
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
        return self.ssh_command_service_get_ssh_commands_endpoint.call_with_http_info(**kwargs)

    def ssh_command_service_update_ssh_command(
        self,
        ssh_command_id,
        **kwargs
    ):
        """Update an SSH Command  # noqa: E501

        Update an SSH Command  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ssh_command_service_update_ssh_command(ssh_command_id, async_req=True)
        >>> result = thread.get()

        Args:
            ssh_command_id (str): sshCommandId

        Keyword Args:
            ssh_command_patch_args (SshCommandPatchArgs): SSH Command Update Options. [optional]
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
            SshCommandModel
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
        kwargs['ssh_command_id'] = \
            ssh_command_id
        return self.ssh_command_service_update_ssh_command_endpoint.call_with_http_info(**kwargs)
