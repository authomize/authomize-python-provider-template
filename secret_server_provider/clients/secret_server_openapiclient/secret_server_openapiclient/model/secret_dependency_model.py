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
    from secret_server_openapiclient.model.secret_dependency_run_script import SecretDependencyRunScript
    from secret_server_openapiclient.model.secret_dependency_setting_map_for_display import SecretDependencySettingMapForDisplay
    from secret_server_openapiclient.model.secret_dependency_template import SecretDependencyTemplate
    globals()['SecretDependencyRunScript'] = SecretDependencyRunScript
    globals()['SecretDependencySettingMapForDisplay'] = SecretDependencySettingMapForDisplay
    globals()['SecretDependencyTemplate'] = SecretDependencyTemplate


class SecretDependencyModel(ModelNormal):
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
            'active': (bool, none_type,),  # noqa: E501
            'child_dependency_status': (bool, none_type,),  # noqa: E501
            'condition_dependency_id': (int, none_type,),  # noqa: E501
            'condition_mode': (str, none_type,),  # noqa: E501
            'dependency_template': (SecretDependencyTemplate, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'group_id': (int, none_type,),  # noqa: E501
            'id': (int, none_type,),  # noqa: E501
            'log_message': (str, none_type,),  # noqa: E501
            'privileged_account_secret_id': (int, none_type,),  # noqa: E501
            'run_script': (SecretDependencyRunScript, none_type,),  # noqa: E501
            'secret_dependency_status': (bool, none_type,),  # noqa: E501
            'secret_id': (int, none_type,),  # noqa: E501
            'secret_name': (str, none_type,),  # noqa: E501
            'settings': ([SecretDependencySettingMapForDisplay], none_type,),  # noqa: E501
            'sort_order': (int, none_type,),  # noqa: E501
            'ssh_key_secret_id': (int, none_type,),  # noqa: E501
            'ssh_key_secret_name': (str, none_type,),  # noqa: E501
            'type_id': (int, none_type,),  # noqa: E501
            'type_name': (str, none_type,),  # noqa: E501
        }
    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'active': 'active',  # noqa: E501
        'child_dependency_status': 'childDependencyStatus',  # noqa: E501
        'condition_dependency_id': 'conditionDependencyId',  # noqa: E501
        'condition_mode': 'conditionMode',  # noqa: E501
        'dependency_template': 'dependencyTemplate',  # noqa: E501
        'description': 'description',  # noqa: E501
        'group_id': 'groupId',  # noqa: E501
        'id': 'id',  # noqa: E501
        'log_message': 'logMessage',  # noqa: E501
        'privileged_account_secret_id': 'privilegedAccountSecretId',  # noqa: E501
        'run_script': 'runScript',  # noqa: E501
        'secret_dependency_status': 'secretDependencyStatus',  # noqa: E501
        'secret_id': 'secretId',  # noqa: E501
        'secret_name': 'secretName',  # noqa: E501
        'settings': 'settings',  # noqa: E501
        'sort_order': 'sortOrder',  # noqa: E501
        'ssh_key_secret_id': 'sshKeySecretId',  # noqa: E501
        'ssh_key_secret_name': 'sshKeySecretName',  # noqa: E501
        'type_id': 'typeId',  # noqa: E501
        'type_name': 'typeName',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """SecretDependencyModel - a model defined in OpenAPI

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
            active (bool): Whether or not the Secret Dependency is active.. [optional]  # noqa: E501
            child_dependency_status (bool): The last run status of the child Secret Dependency.. [optional]  # noqa: E501
            condition_dependency_id (int): The Id of the dependency that will be looked at when  Condition Mode is set to 'DEPENDENCYPASS', 'DEPENDENCYFAIL'. The Dependency must have a SortOrder lower than the current one.. [optional]  # noqa: E501
            condition_mode (str): Condition Mode governs if this dependency's run relies on the result of other dependencies above it. The Default is ALWAYSRUN. Other values maybe 'All Pass', 'Any Fail', 'DEPENDENCYPASS', 'DEPENDENCYFAIL'.. [optional]  # noqa: E501
            dependency_template (SecretDependencyTemplate): [optional]  # noqa: E501
            description (str): A description for the Secret Dependency.. [optional]  # noqa: E501
            group_id (int): The Id of the Dependency Group that contains the Secret Dependency.. [optional]  # noqa: E501
            id (int): The Id of the Secret Dependency.. [optional]  # noqa: E501
            log_message (str): The last Log message for the Secret Dependency.. [optional]  # noqa: E501
            privileged_account_secret_id (int): The Id of the Privileged Secret that the Secret Dependency will use to run.. [optional]  # noqa: E501
            run_script (SecretDependencyRunScript): [optional]  # noqa: E501
            secret_dependency_status (bool): The last run status of the Secret Dependency.. [optional]  # noqa: E501
            secret_id (int): The Id of the Secret that the Secret Dependency is assigned to.. [optional]  # noqa: E501
            secret_name (str): The Name of the Secret that the Secret Dependency is assigned to.. [optional]  # noqa: E501
            settings ([SecretDependencySettingMapForDisplay]): The Settings used by the Secret Dependency. (Ex: WaitBeforeSeconds, Database, Port, SSHKeyDigest). If a setting exists with the same name (or intent in the case of Port and SqlPort) as a field on the Dependency template's DependencyScanItemFields collection, the value assigned to the setting takes precedence and will overwrite the corresponding DependencyScanItemField.. [optional]  # noqa: E501
            sort_order (int): The sort order of the Secret Dependency in the group.  Determines the order of execution of the dependencies within a group.. [optional]  # noqa: E501
            ssh_key_secret_id (int): The Id of the Secret containing the SSH key. (If dependency is tied to SSH key Secret. [optional]  # noqa: E501
            ssh_key_secret_name (str): The Name of the Secret containing the SSH key. (If dependency is tied to SSH key Secret. [optional]  # noqa: E501
            type_id (int): The Id of the type of Secret Dependency.. [optional]  # noqa: E501
            type_name (str): The name of the type of Secret Dependency.. [optional]  # noqa: E501
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
        """SecretDependencyModel - a model defined in OpenAPI

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
            active (bool): Whether or not the Secret Dependency is active.. [optional]  # noqa: E501
            child_dependency_status (bool): The last run status of the child Secret Dependency.. [optional]  # noqa: E501
            condition_dependency_id (int): The Id of the dependency that will be looked at when  Condition Mode is set to 'DEPENDENCYPASS', 'DEPENDENCYFAIL'. The Dependency must have a SortOrder lower than the current one.. [optional]  # noqa: E501
            condition_mode (str): Condition Mode governs if this dependency's run relies on the result of other dependencies above it. The Default is ALWAYSRUN. Other values maybe 'All Pass', 'Any Fail', 'DEPENDENCYPASS', 'DEPENDENCYFAIL'.. [optional]  # noqa: E501
            dependency_template (SecretDependencyTemplate): [optional]  # noqa: E501
            description (str): A description for the Secret Dependency.. [optional]  # noqa: E501
            group_id (int): The Id of the Dependency Group that contains the Secret Dependency.. [optional]  # noqa: E501
            id (int): The Id of the Secret Dependency.. [optional]  # noqa: E501
            log_message (str): The last Log message for the Secret Dependency.. [optional]  # noqa: E501
            privileged_account_secret_id (int): The Id of the Privileged Secret that the Secret Dependency will use to run.. [optional]  # noqa: E501
            run_script (SecretDependencyRunScript): [optional]  # noqa: E501
            secret_dependency_status (bool): The last run status of the Secret Dependency.. [optional]  # noqa: E501
            secret_id (int): The Id of the Secret that the Secret Dependency is assigned to.. [optional]  # noqa: E501
            secret_name (str): The Name of the Secret that the Secret Dependency is assigned to.. [optional]  # noqa: E501
            settings ([SecretDependencySettingMapForDisplay]): The Settings used by the Secret Dependency. (Ex: WaitBeforeSeconds, Database, Port, SSHKeyDigest). If a setting exists with the same name (or intent in the case of Port and SqlPort) as a field on the Dependency template's DependencyScanItemFields collection, the value assigned to the setting takes precedence and will overwrite the corresponding DependencyScanItemField.. [optional]  # noqa: E501
            sort_order (int): The sort order of the Secret Dependency in the group.  Determines the order of execution of the dependencies within a group.. [optional]  # noqa: E501
            ssh_key_secret_id (int): The Id of the Secret containing the SSH key. (If dependency is tied to SSH key Secret. [optional]  # noqa: E501
            ssh_key_secret_name (str): The Name of the Secret containing the SSH key. (If dependency is tied to SSH key Secret. [optional]  # noqa: E501
            type_id (int): The Id of the type of Secret Dependency.. [optional]  # noqa: E501
            type_name (str): The name of the type of Secret Dependency.. [optional]  # noqa: E501
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
