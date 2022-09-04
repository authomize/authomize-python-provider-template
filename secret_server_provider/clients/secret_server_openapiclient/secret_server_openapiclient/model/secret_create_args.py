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
    from secret_server_openapiclient.model.rest_secret_item import RestSecretItem
    from secret_server_openapiclient.model.ssh_key_args import SshKeyArgs
    globals()['RestSecretItem'] = RestSecretItem
    globals()['SshKeyArgs'] = SshKeyArgs


class SecretCreateArgs(ModelNormal):
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
        ('secret_template_id',): {
            'inclusive_minimum': 1,
        },
        ('site_id',): {
            'inclusive_minimum': 1,
        },
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
            'items': ([RestSecretItem],),  # noqa: E501
            'name': (str,),  # noqa: E501
            'secret_template_id': (int,),  # noqa: E501
            'auto_change_enabled': (bool, none_type,),  # noqa: E501
            'check_out_change_password_enabled': (bool, none_type,),  # noqa: E501
            'check_out_enabled': (bool, none_type,),  # noqa: E501
            'check_out_interval_minutes': (int, none_type,),  # noqa: E501
            'delay_indexing': (bool, none_type,),  # noqa: E501
            'enable_inherit_permissions': (bool, none_type,),  # noqa: E501
            'enable_inherit_secret_policy': (bool, none_type,),  # noqa: E501
            'folder_id': (int, none_type,),  # noqa: E501
            'launcher_connect_as_secret_id': (int, none_type,),  # noqa: E501
            'password_type_web_script_id': (int, none_type,),  # noqa: E501
            'proxy_enabled': (bool, none_type,),  # noqa: E501
            'requires_comment': (bool, none_type,),  # noqa: E501
            'secret_policy_id': (int, none_type,),  # noqa: E501
            'session_recording_enabled': (bool, none_type,),  # noqa: E501
            'site_id': (int, none_type,),  # noqa: E501
            'ssh_key_args': (SshKeyArgs, none_type,),  # noqa: E501
            'web_launcher_requires_incognito_mode': (bool, none_type,),  # noqa: E501
        }
    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'items': 'items',  # noqa: E501
        'name': 'name',  # noqa: E501
        'secret_template_id': 'secretTemplateId',  # noqa: E501
        'auto_change_enabled': 'autoChangeEnabled',  # noqa: E501
        'check_out_change_password_enabled': 'checkOutChangePasswordEnabled',  # noqa: E501
        'check_out_enabled': 'checkOutEnabled',  # noqa: E501
        'check_out_interval_minutes': 'checkOutIntervalMinutes',  # noqa: E501
        'delay_indexing': 'delayIndexing',  # noqa: E501
        'enable_inherit_permissions': 'enableInheritPermissions',  # noqa: E501
        'enable_inherit_secret_policy': 'enableInheritSecretPolicy',  # noqa: E501
        'folder_id': 'folderId',  # noqa: E501
        'launcher_connect_as_secret_id': 'launcherConnectAsSecretId',  # noqa: E501
        'password_type_web_script_id': 'passwordTypeWebScriptId',  # noqa: E501
        'proxy_enabled': 'proxyEnabled',  # noqa: E501
        'requires_comment': 'requiresComment',  # noqa: E501
        'secret_policy_id': 'secretPolicyId',  # noqa: E501
        'session_recording_enabled': 'sessionRecordingEnabled',  # noqa: E501
        'site_id': 'siteId',  # noqa: E501
        'ssh_key_args': 'sshKeyArgs',  # noqa: E501
        'web_launcher_requires_incognito_mode': 'webLauncherRequiresIncognitoMode',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, items, name, secret_template_id, *args, **kwargs):  # noqa: E501
        """SecretCreateArgs - a model defined in OpenAPI

        Args:
            items ([RestSecretItem]): An array of values for the secret fields defined in the secret template.
            name (str): The name to display for the secret.
            secret_template_id (int): The id of the secret template that defines the fields and properties of the secret.

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
            auto_change_enabled (bool): Whether the secret’s password is automatically rotated on a schedule.. [optional]  # noqa: E501
            check_out_change_password_enabled (bool): Whether the secret’s password is automatically changed when a secret is checked in. This is a security feature that prevents a use of the password retrieved from check-out after the secret is checked in.. [optional]  # noqa: E501
            check_out_enabled (bool): Whether the user must check-out the secret to view it. Checking out gives the user exclusive access to the secret for a specified period or until the secret is checked in.. [optional]  # noqa: E501
            check_out_interval_minutes (int): The number of minutes that a secret will remain checked out.. [optional]  # noqa: E501
            delay_indexing (bool): Whether the search indexing should be delayed to the background process. This can speed up bulk secret creation scripts by offloading the task of indexing the new secrets to the background task at the trade-off of not having search indexes immediately available.. [optional]  # noqa: E501
            enable_inherit_permissions (bool): Whether the secret inherits permissions from the containing folder.. [optional]  # noqa: E501
            enable_inherit_secret_policy (bool): Whether the secret policy is inherited from the containing folder.. [optional]  # noqa: E501
            folder_id (int): If the secret is contained in a folder, the id of the containing folder. Set to null or -1 for secrets that are in the root folder.. [optional]  # noqa: E501
            launcher_connect_as_secret_id (int): When an SSH secret is proxied, you can choose to connect as another user and then do an su to the current secret’s user. This is a common practice for connecting with a lower privileged account and then switching to the root user.. [optional]  # noqa: E501
            password_type_web_script_id (int): The id of the password change script to use on applicable web password secrets.. [optional]  # noqa: E501
            proxy_enabled (bool): Whether sessions launched on this secret use Secret Server’s proxying or connect directly.. [optional]  # noqa: E501
            requires_comment (bool): Whether the user must enter a comment to view the secret.. [optional]  # noqa: E501
            secret_policy_id (int): The id of the secret policy that controls the security and other settings of the secret. Set to null to not assign a secret policy.. [optional]  # noqa: E501
            session_recording_enabled (bool): Whether session recording is enabled.. [optional]  # noqa: E501
            site_id (int): The id of the distributed engine site that is used by this secret for operations such as password changing.. [optional]  # noqa: E501
            ssh_key_args (SshKeyArgs): [optional]  # noqa: E501
            web_launcher_requires_incognito_mode (bool): Whether the web launcher will require the browser to run in incognito mode.. [optional]  # noqa: E501
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

        self.items = items
        self.name = name
        self.secret_template_id = secret_template_id
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
    def __init__(self, items, name, secret_template_id, *args, **kwargs):  # noqa: E501
        """SecretCreateArgs - a model defined in OpenAPI

        Args:
            items ([RestSecretItem]): An array of values for the secret fields defined in the secret template.
            name (str): The name to display for the secret.
            secret_template_id (int): The id of the secret template that defines the fields and properties of the secret.

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
            auto_change_enabled (bool): Whether the secret’s password is automatically rotated on a schedule.. [optional]  # noqa: E501
            check_out_change_password_enabled (bool): Whether the secret’s password is automatically changed when a secret is checked in. This is a security feature that prevents a use of the password retrieved from check-out after the secret is checked in.. [optional]  # noqa: E501
            check_out_enabled (bool): Whether the user must check-out the secret to view it. Checking out gives the user exclusive access to the secret for a specified period or until the secret is checked in.. [optional]  # noqa: E501
            check_out_interval_minutes (int): The number of minutes that a secret will remain checked out.. [optional]  # noqa: E501
            delay_indexing (bool): Whether the search indexing should be delayed to the background process. This can speed up bulk secret creation scripts by offloading the task of indexing the new secrets to the background task at the trade-off of not having search indexes immediately available.. [optional]  # noqa: E501
            enable_inherit_permissions (bool): Whether the secret inherits permissions from the containing folder.. [optional]  # noqa: E501
            enable_inherit_secret_policy (bool): Whether the secret policy is inherited from the containing folder.. [optional]  # noqa: E501
            folder_id (int): If the secret is contained in a folder, the id of the containing folder. Set to null or -1 for secrets that are in the root folder.. [optional]  # noqa: E501
            launcher_connect_as_secret_id (int): When an SSH secret is proxied, you can choose to connect as another user and then do an su to the current secret’s user. This is a common practice for connecting with a lower privileged account and then switching to the root user.. [optional]  # noqa: E501
            password_type_web_script_id (int): The id of the password change script to use on applicable web password secrets.. [optional]  # noqa: E501
            proxy_enabled (bool): Whether sessions launched on this secret use Secret Server’s proxying or connect directly.. [optional]  # noqa: E501
            requires_comment (bool): Whether the user must enter a comment to view the secret.. [optional]  # noqa: E501
            secret_policy_id (int): The id of the secret policy that controls the security and other settings of the secret. Set to null to not assign a secret policy.. [optional]  # noqa: E501
            session_recording_enabled (bool): Whether session recording is enabled.. [optional]  # noqa: E501
            site_id (int): The id of the distributed engine site that is used by this secret for operations such as password changing.. [optional]  # noqa: E501
            ssh_key_args (SshKeyArgs): [optional]  # noqa: E501
            web_launcher_requires_incognito_mode (bool): Whether the web launcher will require the browser to run in incognito mode.. [optional]  # noqa: E501
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

        self.items = items
        self.name = name
        self.secret_template_id = secret_template_id
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
