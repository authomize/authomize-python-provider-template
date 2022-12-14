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


def lazy_import():
    from secret_server_openapiclient.model.secret_template_launcher_field_value_model import SecretTemplateLauncherFieldValueModel
    globals()['SecretTemplateLauncherFieldValueModel'] = SecretTemplateLauncherFieldValueModel


class SecretTemplateLauncherModel(ModelNormal):
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
        lazy_import()
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
        lazy_import()
        return {
            'allow_list': (int, none_type,),  # noqa: E501
            'connect_as_command': (str, none_type,),  # noqa: E501
            'connect_as_command_response': (str, none_type,),  # noqa: E501
            'deny_list': (int, none_type,),  # noqa: E501
            'fields': ([SecretTemplateLauncherFieldValueModel], none_type,),  # noqa: E501
            'include_machines_from_dependencies': (bool, none_type,),  # noqa: E501
            'launcher_type_id': (int, none_type,),  # noqa: E501
            'launcher_type_name': (str, none_type,),  # noqa: E501
            'line_ending': (str, none_type,),  # noqa: E501
            'restrict_as': (int, none_type,),  # noqa: E501
            'restrict_by_secret_field': (int, none_type,),  # noqa: E501
            'restrict_user_input': (bool, none_type,),  # noqa: E501
        }
    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'allow_list': 'allowList',  # noqa: E501
        'connect_as_command': 'connectAsCommand',  # noqa: E501
        'connect_as_command_response': 'connectAsCommandResponse',  # noqa: E501
        'deny_list': 'denyList',  # noqa: E501
        'fields': 'fields',  # noqa: E501
        'include_machines_from_dependencies': 'includeMachinesFromDependencies',  # noqa: E501
        'launcher_type_id': 'launcherTypeId',  # noqa: E501
        'launcher_type_name': 'launcherTypeName',  # noqa: E501
        'line_ending': 'lineEnding',  # noqa: E501
        'restrict_as': 'restrictAs',  # noqa: E501
        'restrict_by_secret_field': 'restrictBySecretField',  # noqa: E501
        'restrict_user_input': 'restrictUserInput',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """SecretTemplateLauncherModel - a model defined in OpenAPI

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
            allow_list (int): User can select from values in this list. [optional]  # noqa: E501
            connect_as_command (str): This command is used after a PuTTy session is launched on a Secret that has SSH Proxy enabled and has a Secret set under 'Connect As' in the Launcher tab. The default su command is 'su - $USERNAME'. $USERNAME is the token used to retrieve the username field from the Secret. Sudo can also be used by specifying 'sudo -u $USERNAME /bin/bash'.. [optional]  # noqa: E501
            connect_as_command_response (str): The Connect As Command Response is the response from the server prompting for a password. This is used so $productName knows when to send the password to the system. If the response from the server after typing 'su - root' is 'Password:' then the Connect As Command Response needs to contain 'Password:$PASSWORD'. The $CONNECTASPASSWORD token will use the credentials from the Secret set under 'Connect As' when prompted.. [optional]  # noqa: E501
            deny_list (int): User cannot enter these values. If used with an Allow List, the Deny List will take precedence.. [optional]  # noqa: E501
            fields ([SecretTemplateLauncherFieldValueModel]): Fields that can be mapped to this launcher. [optional]  # noqa: E501
            include_machines_from_dependencies (bool): This will add the list of machine names from the secret dependencies to either the allow list or block list.. [optional]  # noqa: E501
            launcher_type_id (int): Unique ID for Launcher Type. [optional]  # noqa: E501
            launcher_type_name (str): Name for Launcher Type. [optional]  # noqa: E501
            line_ending (str): The line ending that will be append to the end of the Connect As Command. This needs to match the type of line ending required by the system being proxied to.. [optional]  # noqa: E501
            restrict_as (int): Restrict what can be selected to come from a list, only allow certain fields, or only deny certain fields.. [optional]  # noqa: E501
            restrict_by_secret_field (int): Select a field that will contain the list of items that will restrict the input.. [optional]  # noqa: E501
            restrict_user_input (bool): You may specify a field of comma separated hosts or IP addresses that the user will be restricted to. The allow list will allow only these values, while the block list will allow all values except the hosts on the Secret Field.  Example: 192.168.1.2, MACHINE.EXAMPLE.COM, 192.168.1.60. [optional]  # noqa: E501
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
        """SecretTemplateLauncherModel - a model defined in OpenAPI

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
            allow_list (int): User can select from values in this list. [optional]  # noqa: E501
            connect_as_command (str): This command is used after a PuTTy session is launched on a Secret that has SSH Proxy enabled and has a Secret set under 'Connect As' in the Launcher tab. The default su command is 'su - $USERNAME'. $USERNAME is the token used to retrieve the username field from the Secret. Sudo can also be used by specifying 'sudo -u $USERNAME /bin/bash'.. [optional]  # noqa: E501
            connect_as_command_response (str): The Connect As Command Response is the response from the server prompting for a password. This is used so $productName knows when to send the password to the system. If the response from the server after typing 'su - root' is 'Password:' then the Connect As Command Response needs to contain 'Password:$PASSWORD'. The $CONNECTASPASSWORD token will use the credentials from the Secret set under 'Connect As' when prompted.. [optional]  # noqa: E501
            deny_list (int): User cannot enter these values. If used with an Allow List, the Deny List will take precedence.. [optional]  # noqa: E501
            fields ([SecretTemplateLauncherFieldValueModel]): Fields that can be mapped to this launcher. [optional]  # noqa: E501
            include_machines_from_dependencies (bool): This will add the list of machine names from the secret dependencies to either the allow list or block list.. [optional]  # noqa: E501
            launcher_type_id (int): Unique ID for Launcher Type. [optional]  # noqa: E501
            launcher_type_name (str): Name for Launcher Type. [optional]  # noqa: E501
            line_ending (str): The line ending that will be append to the end of the Connect As Command. This needs to match the type of line ending required by the system being proxied to.. [optional]  # noqa: E501
            restrict_as (int): Restrict what can be selected to come from a list, only allow certain fields, or only deny certain fields.. [optional]  # noqa: E501
            restrict_by_secret_field (int): Select a field that will contain the list of items that will restrict the input.. [optional]  # noqa: E501
            restrict_user_input (bool): You may specify a field of comma separated hosts or IP addresses that the user will be restricted to. The allow list will allow only these values, while the block list will allow all values except the hosts on the Secret Field.  Example: 192.168.1.2, MACHINE.EXAMPLE.COM, 192.168.1.60. [optional]  # noqa: E501
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
