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
    from secret_server_openapiclient.model.secret_policy_item_of_optional_boolean import SecretPolicyItemOfOptionalBoolean
    from secret_server_openapiclient.model.secret_policy_item_of_optional_command_restriction_type import SecretPolicyItemOfOptionalCommandRestrictionType
    from secret_server_openapiclient.model.secret_policy_item_of_optional_guid import SecretPolicyItemOfOptionalGuid
    from secret_server_openapiclient.model.secret_policy_item_of_optional_int32 import SecretPolicyItemOfOptionalInt32
    from secret_server_openapiclient.model.secret_policy_item_of_ssh_command_menu_group_map_model_array import SecretPolicyItemOfSshCommandMenuGroupMapModelArray
    from secret_server_openapiclient.model.secret_policy_item_of_user_group_map_model_array import SecretPolicyItemOfUserGroupMapModelArray
    globals()['SecretPolicyItemOfOptionalBoolean'] = SecretPolicyItemOfOptionalBoolean
    globals()['SecretPolicyItemOfOptionalCommandRestrictionType'] = SecretPolicyItemOfOptionalCommandRestrictionType
    globals()['SecretPolicyItemOfOptionalGuid'] = SecretPolicyItemOfOptionalGuid
    globals()['SecretPolicyItemOfOptionalInt32'] = SecretPolicyItemOfOptionalInt32
    globals()['SecretPolicyItemOfSshCommandMenuGroupMapModelArray'] = SecretPolicyItemOfSshCommandMenuGroupMapModelArray
    globals()['SecretPolicyItemOfUserGroupMapModelArray'] = SecretPolicyItemOfUserGroupMapModelArray


class SecretPolicySecurityItemsModel(ModelNormal):
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
            'allow_owners_unrestricted_ssh_commands': (SecretPolicyItemOfOptionalBoolean, none_type,),  # noqa: E501
            'approval_groups': (SecretPolicyItemOfUserGroupMapModelArray, none_type,),  # noqa: E501
            'approval_workflow': (SecretPolicyItemOfOptionalInt32, none_type,),  # noqa: E501
            'check_out_change_password': (SecretPolicyItemOfOptionalBoolean, none_type,),  # noqa: E501
            'check_out_enabled': (SecretPolicyItemOfOptionalBoolean, none_type,),  # noqa: E501
            'check_out_interval_minutes': (SecretPolicyItemOfOptionalInt32, none_type,),  # noqa: E501
            'enable_ssh_command_restrictions': (SecretPolicyItemOfOptionalBoolean, none_type,),  # noqa: E501
            'event_pipeline_policy': (SecretPolicyItemOfOptionalInt32, none_type,),  # noqa: E501
            'hide_launcher_password': (SecretPolicyItemOfOptionalBoolean, none_type,),  # noqa: E501
            'is_proxy_enabled': (SecretPolicyItemOfOptionalBoolean, none_type,),  # noqa: E501
            'is_session_recording_enabled': (SecretPolicyItemOfOptionalBoolean, none_type,),  # noqa: E501
            'require_approval_for_access': (SecretPolicyItemOfOptionalBoolean, none_type,),  # noqa: E501
            'require_approval_for_access_for_editors': (SecretPolicyItemOfOptionalBoolean, none_type,),  # noqa: E501
            'require_approval_for_access_for_owners_and_approvers': (SecretPolicyItemOfOptionalBoolean, none_type,),  # noqa: E501
            'require_view_comment': (SecretPolicyItemOfOptionalBoolean, none_type,),  # noqa: E501
            'run_launcher_using_ssh_key_secret_id': (SecretPolicyItemOfOptionalInt32, none_type,),  # noqa: E501
            'ssh_command_blocklist_editors': (SecretPolicyItemOfOptionalGuid, none_type,),  # noqa: E501
            'ssh_command_blocklist_owners': (SecretPolicyItemOfOptionalGuid, none_type,),  # noqa: E501
            'ssh_command_blocklist_viewers': (SecretPolicyItemOfOptionalGuid, none_type,),  # noqa: E501
            'ssh_command_menu_groups': (SecretPolicyItemOfSshCommandMenuGroupMapModelArray, none_type,),  # noqa: E501
            'ssh_command_restriction_type': (SecretPolicyItemOfOptionalCommandRestrictionType, none_type,),  # noqa: E501
        }
    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'allow_owners_unrestricted_ssh_commands': 'allowOwnersUnrestrictedSshCommands',  # noqa: E501
        'approval_groups': 'approvalGroups',  # noqa: E501
        'approval_workflow': 'approvalWorkflow',  # noqa: E501
        'check_out_change_password': 'checkOutChangePassword',  # noqa: E501
        'check_out_enabled': 'checkOutEnabled',  # noqa: E501
        'check_out_interval_minutes': 'checkOutIntervalMinutes',  # noqa: E501
        'enable_ssh_command_restrictions': 'enableSshCommandRestrictions',  # noqa: E501
        'event_pipeline_policy': 'eventPipelinePolicy',  # noqa: E501
        'hide_launcher_password': 'hideLauncherPassword',  # noqa: E501
        'is_proxy_enabled': 'isProxyEnabled',  # noqa: E501
        'is_session_recording_enabled': 'isSessionRecordingEnabled',  # noqa: E501
        'require_approval_for_access': 'requireApprovalForAccess',  # noqa: E501
        'require_approval_for_access_for_editors': 'requireApprovalForAccessForEditors',  # noqa: E501
        'require_approval_for_access_for_owners_and_approvers': 'requireApprovalForAccessForOwnersAndApprovers',  # noqa: E501
        'require_view_comment': 'requireViewComment',  # noqa: E501
        'run_launcher_using_ssh_key_secret_id': 'runLauncherUsingSSHKeySecretId',  # noqa: E501
        'ssh_command_blocklist_editors': 'sshCommandBlocklistEditors',  # noqa: E501
        'ssh_command_blocklist_owners': 'sshCommandBlocklistOwners',  # noqa: E501
        'ssh_command_blocklist_viewers': 'sshCommandBlocklistViewers',  # noqa: E501
        'ssh_command_menu_groups': 'sshCommandMenuGroups',  # noqa: E501
        'ssh_command_restriction_type': 'sshCommandRestrictionType',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """SecretPolicySecurityItemsModel - a model defined in OpenAPI

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
            allow_owners_unrestricted_ssh_commands (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            approval_groups (SecretPolicyItemOfUserGroupMapModelArray): [optional]  # noqa: E501
            approval_workflow (SecretPolicyItemOfOptionalInt32): [optional]  # noqa: E501
            check_out_change_password (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            check_out_enabled (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            check_out_interval_minutes (SecretPolicyItemOfOptionalInt32): [optional]  # noqa: E501
            enable_ssh_command_restrictions (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            event_pipeline_policy (SecretPolicyItemOfOptionalInt32): [optional]  # noqa: E501
            hide_launcher_password (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            is_proxy_enabled (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            is_session_recording_enabled (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            require_approval_for_access (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            require_approval_for_access_for_editors (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            require_approval_for_access_for_owners_and_approvers (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            require_view_comment (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            run_launcher_using_ssh_key_secret_id (SecretPolicyItemOfOptionalInt32): [optional]  # noqa: E501
            ssh_command_blocklist_editors (SecretPolicyItemOfOptionalGuid): [optional]  # noqa: E501
            ssh_command_blocklist_owners (SecretPolicyItemOfOptionalGuid): [optional]  # noqa: E501
            ssh_command_blocklist_viewers (SecretPolicyItemOfOptionalGuid): [optional]  # noqa: E501
            ssh_command_menu_groups (SecretPolicyItemOfSshCommandMenuGroupMapModelArray): [optional]  # noqa: E501
            ssh_command_restriction_type (SecretPolicyItemOfOptionalCommandRestrictionType): [optional]  # noqa: E501
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
        """SecretPolicySecurityItemsModel - a model defined in OpenAPI

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
            allow_owners_unrestricted_ssh_commands (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            approval_groups (SecretPolicyItemOfUserGroupMapModelArray): [optional]  # noqa: E501
            approval_workflow (SecretPolicyItemOfOptionalInt32): [optional]  # noqa: E501
            check_out_change_password (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            check_out_enabled (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            check_out_interval_minutes (SecretPolicyItemOfOptionalInt32): [optional]  # noqa: E501
            enable_ssh_command_restrictions (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            event_pipeline_policy (SecretPolicyItemOfOptionalInt32): [optional]  # noqa: E501
            hide_launcher_password (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            is_proxy_enabled (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            is_session_recording_enabled (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            require_approval_for_access (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            require_approval_for_access_for_editors (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            require_approval_for_access_for_owners_and_approvers (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            require_view_comment (SecretPolicyItemOfOptionalBoolean): [optional]  # noqa: E501
            run_launcher_using_ssh_key_secret_id (SecretPolicyItemOfOptionalInt32): [optional]  # noqa: E501
            ssh_command_blocklist_editors (SecretPolicyItemOfOptionalGuid): [optional]  # noqa: E501
            ssh_command_blocklist_owners (SecretPolicyItemOfOptionalGuid): [optional]  # noqa: E501
            ssh_command_blocklist_viewers (SecretPolicyItemOfOptionalGuid): [optional]  # noqa: E501
            ssh_command_menu_groups (SecretPolicyItemOfSshCommandMenuGroupMapModelArray): [optional]  # noqa: E501
            ssh_command_restriction_type (SecretPolicyItemOfOptionalCommandRestrictionType): [optional]  # noqa: E501
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
