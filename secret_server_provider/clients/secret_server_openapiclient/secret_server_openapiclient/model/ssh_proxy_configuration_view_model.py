"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from secret_server_openapiclient.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from secret_server_openapiclient.exceptions import ApiAttributeError



class SshProxyConfigurationViewModel(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }
    validations = {
    }
    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501
    _nullable = False
    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'available_port_range': (str, none_type,),  # noqa: E501
            'days_to_keep_operational_logs': (int, none_type,),  # noqa: E501
            'enable_password_hiding': (bool, none_type,),  # noqa: E501
            'enable_proxy_block_listing': (bool, none_type,),  # noqa: E501
            'enable_proxy_inactivity_timeout': (bool, none_type,),  # noqa: E501
            'enable_ssh_proxy': (bool, none_type,),  # noqa: E501
            'enable_ssh_public_key_auth': (bool, none_type,),  # noqa: E501
            'enable_ssh_terminal': (bool, none_type,),  # noqa: E501
            'enable_ssh_tunneling': (bool, none_type,),  # noqa: E501
            'enable_terminal_inactivity_timeout': (bool, none_type,),  # noqa: E501
            'enable_window_title_change_command': (bool, none_type,),  # noqa: E501
            'is_cloud': (bool, none_type,),  # noqa: E501
            'password_regex_filter': (str, none_type,),  # noqa: E501
            'proxy_auto_block_listing_max_num': (int, none_type,),  # noqa: E501
            'proxy_auto_block_listing_time_frame_minutes': (int, none_type,),  # noqa: E501
            'proxy_inactivity_timeout_seconds': (int, none_type,),  # noqa: E501
            'proxy_new_secrets_by_default': (bool, none_type,),  # noqa: E501
            'ssh_host_key': (str, none_type,),  # noqa: E501
            'ssh_proxy_banner': (str, none_type,),  # noqa: E501
            'ssh_proxy_host_fingerprint': (str, none_type,),  # noqa: E501
            'ssh_proxy_port': (int, none_type,),  # noqa: E501
            'ssh_terminal_banner': (str, none_type,),  # noqa: E501
            'terminal_inactivity_timeout_seconds': (int, none_type,),  # noqa: E501
            'tunnel_keep_alive_in_seconds': (int, none_type,),  # noqa: E501
        }
    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'available_port_range': 'availablePortRange',  # noqa: E501
        'days_to_keep_operational_logs': 'daysToKeepOperationalLogs',  # noqa: E501
        'enable_password_hiding': 'enablePasswordHiding',  # noqa: E501
        'enable_proxy_block_listing': 'enableProxyBlockListing',  # noqa: E501
        'enable_proxy_inactivity_timeout': 'enableProxyInactivityTimeout',  # noqa: E501
        'enable_ssh_proxy': 'enableSshProxy',  # noqa: E501
        'enable_ssh_public_key_auth': 'enableSshPublicKeyAuth',  # noqa: E501
        'enable_ssh_terminal': 'enableSshTerminal',  # noqa: E501
        'enable_ssh_tunneling': 'enableSshTunneling',  # noqa: E501
        'enable_terminal_inactivity_timeout': 'enableTerminalInactivityTimeout',  # noqa: E501
        'enable_window_title_change_command': 'enableWindowTitleChangeCommand',  # noqa: E501
        'is_cloud': 'isCloud',  # noqa: E501
        'password_regex_filter': 'passwordRegexFilter',  # noqa: E501
        'proxy_auto_block_listing_max_num': 'proxyAutoBlockListingMaxNum',  # noqa: E501
        'proxy_auto_block_listing_time_frame_minutes': 'proxyAutoBlockListingTimeFrameMinutes',  # noqa: E501
        'proxy_inactivity_timeout_seconds': 'proxyInactivityTimeoutSeconds',  # noqa: E501
        'proxy_new_secrets_by_default': 'proxyNewSecretsByDefault',  # noqa: E501
        'ssh_host_key': 'sshHostKey',  # noqa: E501
        'ssh_proxy_banner': 'sshProxyBanner',  # noqa: E501
        'ssh_proxy_host_fingerprint': 'sshProxyHostFingerprint',  # noqa: E501
        'ssh_proxy_port': 'sshProxyPort',  # noqa: E501
        'ssh_terminal_banner': 'sshTerminalBanner',  # noqa: E501
        'terminal_inactivity_timeout_seconds': 'terminalInactivityTimeoutSeconds',  # noqa: E501
        'tunnel_keep_alive_in_seconds': 'tunnelKeepAliveInSeconds',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """SshProxyConfigurationViewModel - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            available_port_range (str): Range of unused ports available on the SSH Proxy endpoint to be used for Jumpbox port forwarding. [optional]  # noqa: E501
            days_to_keep_operational_logs (int): The number of days to store SSH proxy logs before they are rolled over. [optional]  # noqa: E501
            enable_password_hiding (bool): Enable to hide passwords from SSH keystroke capture. This prevents logging user input on lines that are determined to be a password prompt.. [optional]  # noqa: E501
            enable_proxy_block_listing (bool): Enable block listing of IP Addresses that connect and fail to authenticate too many times. [optional]  # noqa: E501
            enable_proxy_inactivity_timeout (bool): Whether or not the proxy should disconnect inactive sessions. [optional]  # noqa: E501
            enable_ssh_proxy (bool): Whether or not the SSH proxy is enabled. [optional]  # noqa: E501
            enable_ssh_public_key_auth (bool): Whether or not the SSH Terminal can allow key authentication. [optional]  # noqa: E501
            enable_ssh_terminal (bool): Whether or not the SSH terminal is enabled. [optional]  # noqa: E501
            enable_ssh_tunneling (bool): Whether or not to allow SSH tunneling through the proxy for proxied RDP sessions. [optional]  # noqa: E501
            enable_terminal_inactivity_timeout (bool): Whether or not the SSH terminal should disconnect inactive sessions. [optional]  # noqa: E501
            enable_window_title_change_command (bool): Send window title change command on startup. [optional]  # noqa: E501
            is_cloud (bool): IsCloud. [optional]  # noqa: E501
            password_regex_filter (str): Regular Expression used to identify password prompts. The default expression search for either prompts beginning with 'sudo password for' or prompts ending with 'password:'. [optional]  # noqa: E501
            proxy_auto_block_listing_max_num (int): The number of failed authentication attempts before being blocked. [optional]  # noqa: E501
            proxy_auto_block_listing_time_frame_minutes (int): The time frame in which all the failed attempts must happen before being blocked. [optional]  # noqa: E501
            proxy_inactivity_timeout_seconds (int): The amount of time in seconds to wait before disconnecting inactive proxy sessions. [optional]  # noqa: E501
            proxy_new_secrets_by_default (bool): Whether or not new SSH-enabled secrets should be created with 'Proxy Enabled' set. [optional]  # noqa: E501
            ssh_host_key (str): The host key that will the proxy will serve. [optional]  # noqa: E501
            ssh_proxy_banner (str): The banner that is display when someone opens an shell connection to the proxy. [optional]  # noqa: E501
            ssh_proxy_host_fingerprint (str): The fingerprint of the host key that the proxy will serve. [optional]  # noqa: E501
            ssh_proxy_port (int): The port that that SSH proxy runs on. [optional]  # noqa: E501
            ssh_terminal_banner (str): The banner that is displayed when someone authenticates to the SSH terminal. [optional]  # noqa: E501
            terminal_inactivity_timeout_seconds (int): The amount of time in seconds to wait before disconnecting inactive terminal sessions. [optional]  # noqa: E501
            tunnel_keep_alive_in_seconds (int): Keep alive signals to local port forwarding tunnels at this interval (in seconds). Prevents port forwarding tunnels from closing. (0-86400) . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """SshProxyConfigurationViewModel - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            available_port_range (str): Range of unused ports available on the SSH Proxy endpoint to be used for Jumpbox port forwarding. [optional]  # noqa: E501
            days_to_keep_operational_logs (int): The number of days to store SSH proxy logs before they are rolled over. [optional]  # noqa: E501
            enable_password_hiding (bool): Enable to hide passwords from SSH keystroke capture. This prevents logging user input on lines that are determined to be a password prompt.. [optional]  # noqa: E501
            enable_proxy_block_listing (bool): Enable block listing of IP Addresses that connect and fail to authenticate too many times. [optional]  # noqa: E501
            enable_proxy_inactivity_timeout (bool): Whether or not the proxy should disconnect inactive sessions. [optional]  # noqa: E501
            enable_ssh_proxy (bool): Whether or not the SSH proxy is enabled. [optional]  # noqa: E501
            enable_ssh_public_key_auth (bool): Whether or not the SSH Terminal can allow key authentication. [optional]  # noqa: E501
            enable_ssh_terminal (bool): Whether or not the SSH terminal is enabled. [optional]  # noqa: E501
            enable_ssh_tunneling (bool): Whether or not to allow SSH tunneling through the proxy for proxied RDP sessions. [optional]  # noqa: E501
            enable_terminal_inactivity_timeout (bool): Whether or not the SSH terminal should disconnect inactive sessions. [optional]  # noqa: E501
            enable_window_title_change_command (bool): Send window title change command on startup. [optional]  # noqa: E501
            is_cloud (bool): IsCloud. [optional]  # noqa: E501
            password_regex_filter (str): Regular Expression used to identify password prompts. The default expression search for either prompts beginning with 'sudo password for' or prompts ending with 'password:'. [optional]  # noqa: E501
            proxy_auto_block_listing_max_num (int): The number of failed authentication attempts before being blocked. [optional]  # noqa: E501
            proxy_auto_block_listing_time_frame_minutes (int): The time frame in which all the failed attempts must happen before being blocked. [optional]  # noqa: E501
            proxy_inactivity_timeout_seconds (int): The amount of time in seconds to wait before disconnecting inactive proxy sessions. [optional]  # noqa: E501
            proxy_new_secrets_by_default (bool): Whether or not new SSH-enabled secrets should be created with 'Proxy Enabled' set. [optional]  # noqa: E501
            ssh_host_key (str): The host key that will the proxy will serve. [optional]  # noqa: E501
            ssh_proxy_banner (str): The banner that is display when someone opens an shell connection to the proxy. [optional]  # noqa: E501
            ssh_proxy_host_fingerprint (str): The fingerprint of the host key that the proxy will serve. [optional]  # noqa: E501
            ssh_proxy_port (int): The port that that SSH proxy runs on. [optional]  # noqa: E501
            ssh_terminal_banner (str): The banner that is displayed when someone authenticates to the SSH terminal. [optional]  # noqa: E501
            terminal_inactivity_timeout_seconds (int): The amount of time in seconds to wait before disconnecting inactive terminal sessions. [optional]  # noqa: E501
            tunnel_keep_alive_in_seconds (int): Keep alive signals to local port forwarding tunnels at this interval (in seconds). Prevents port forwarding tunnels from closing. (0-86400) . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
