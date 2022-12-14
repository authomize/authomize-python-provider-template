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
    from secret_server_openapiclient.model.heartbeat_status import HeartbeatStatus
    from secret_server_openapiclient.model.rest_secret_item import RestSecretItem
    globals()['HeartbeatStatus'] = HeartbeatStatus
    globals()['RestSecretItem'] = RestSecretItem


class SecretModel(ModelNormal):
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
            'access_request_workflow_map_id': (int, none_type,),  # noqa: E501
            'active': (bool, none_type,),  # noqa: E501
            'allow_owners_unrestricted_ssh_commands': (bool, none_type,),  # noqa: E501
            'auto_change_enabled': (bool, none_type,),  # noqa: E501
            'auto_change_next_password': (str, none_type,),  # noqa: E501
            'checked_out': (bool, none_type,),  # noqa: E501
            'check_out_change_password_enabled': (bool, none_type,),  # noqa: E501
            'check_out_enabled': (bool, none_type,),  # noqa: E501
            'check_out_interval_minutes': (int, none_type,),  # noqa: E501
            'check_out_minutes_remaining': (int, none_type,),  # noqa: E501
            'check_out_user_display_name': (str, none_type,),  # noqa: E501
            'check_out_user_id': (int, none_type,),  # noqa: E501
            'double_lock_id': (int, none_type,),  # noqa: E501
            'enable_inherit_permissions': (bool, none_type,),  # noqa: E501
            'enable_inherit_secret_policy': (bool, none_type,),  # noqa: E501
            'failed_password_change_attempts': (int, none_type,),  # noqa: E501
            'folder_id': (int, none_type,),  # noqa: E501
            'id': (int, none_type,),  # noqa: E501
            'is_double_lock': (bool, none_type,),  # noqa: E501
            'is_out_of_sync': (bool, none_type,),  # noqa: E501
            'is_restricted': (bool, none_type,),  # noqa: E501
            'items': ([RestSecretItem], none_type,),  # noqa: E501
            'jumpbox_route_id': (str, none_type,),  # noqa: E501
            'last_heart_beat_check': (datetime, none_type,),  # noqa: E501
            'last_heart_beat_status': (HeartbeatStatus, none_type,),  # noqa: E501
            'last_password_change_attempt': (datetime, none_type,),  # noqa: E501
            'launcher_connect_as_secret_id': (int, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'out_of_sync_reason': (str, none_type,),  # noqa: E501
            'password_type_web_script_id': (int, none_type,),  # noqa: E501
            'proxy_enabled': (bool, none_type,),  # noqa: E501
            'requires_approval_for_access': (bool, none_type,),  # noqa: E501
            'requires_comment': (bool, none_type,),  # noqa: E501
            'response_codes': ([str], none_type,),  # noqa: E501
            'restrict_ssh_commands': (bool, none_type,),  # noqa: E501
            'secret_policy_id': (int, none_type,),  # noqa: E501
            'secret_template_id': (int, none_type,),  # noqa: E501
            'secret_template_name': (str, none_type,),  # noqa: E501
            'session_recording_enabled': (bool, none_type,),  # noqa: E501
            'site_id': (int, none_type,),  # noqa: E501
            'web_launcher_requires_incognito_mode': (bool, none_type,),  # noqa: E501
        }
    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'access_request_workflow_map_id': 'accessRequestWorkflowMapId',  # noqa: E501
        'active': 'active',  # noqa: E501
        'allow_owners_unrestricted_ssh_commands': 'allowOwnersUnrestrictedSshCommands',  # noqa: E501
        'auto_change_enabled': 'autoChangeEnabled',  # noqa: E501
        'auto_change_next_password': 'autoChangeNextPassword',  # noqa: E501
        'checked_out': 'checkedOut',  # noqa: E501
        'check_out_change_password_enabled': 'checkOutChangePasswordEnabled',  # noqa: E501
        'check_out_enabled': 'checkOutEnabled',  # noqa: E501
        'check_out_interval_minutes': 'checkOutIntervalMinutes',  # noqa: E501
        'check_out_minutes_remaining': 'checkOutMinutesRemaining',  # noqa: E501
        'check_out_user_display_name': 'checkOutUserDisplayName',  # noqa: E501
        'check_out_user_id': 'checkOutUserId',  # noqa: E501
        'double_lock_id': 'doubleLockId',  # noqa: E501
        'enable_inherit_permissions': 'enableInheritPermissions',  # noqa: E501
        'enable_inherit_secret_policy': 'enableInheritSecretPolicy',  # noqa: E501
        'failed_password_change_attempts': 'failedPasswordChangeAttempts',  # noqa: E501
        'folder_id': 'folderId',  # noqa: E501
        'id': 'id',  # noqa: E501
        'is_double_lock': 'isDoubleLock',  # noqa: E501
        'is_out_of_sync': 'isOutOfSync',  # noqa: E501
        'is_restricted': 'isRestricted',  # noqa: E501
        'items': 'items',  # noqa: E501
        'jumpbox_route_id': 'jumpboxRouteId',  # noqa: E501
        'last_heart_beat_check': 'lastHeartBeatCheck',  # noqa: E501
        'last_heart_beat_status': 'lastHeartBeatStatus',  # noqa: E501
        'last_password_change_attempt': 'lastPasswordChangeAttempt',  # noqa: E501
        'launcher_connect_as_secret_id': 'launcherConnectAsSecretId',  # noqa: E501
        'name': 'name',  # noqa: E501
        'out_of_sync_reason': 'outOfSyncReason',  # noqa: E501
        'password_type_web_script_id': 'passwordTypeWebScriptId',  # noqa: E501
        'proxy_enabled': 'proxyEnabled',  # noqa: E501
        'requires_approval_for_access': 'requiresApprovalForAccess',  # noqa: E501
        'requires_comment': 'requiresComment',  # noqa: E501
        'response_codes': 'responseCodes',  # noqa: E501
        'restrict_ssh_commands': 'restrictSshCommands',  # noqa: E501
        'secret_policy_id': 'secretPolicyId',  # noqa: E501
        'secret_template_id': 'secretTemplateId',  # noqa: E501
        'secret_template_name': 'secretTemplateName',  # noqa: E501
        'session_recording_enabled': 'sessionRecordingEnabled',  # noqa: E501
        'site_id': 'siteId',  # noqa: E501
        'web_launcher_requires_incognito_mode': 'webLauncherRequiresIncognitoMode',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """SecretModel - a model defined in OpenAPI

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
            access_request_workflow_map_id (int): AccessRequestWorkflowMapId. [optional]  # noqa: E501
            active (bool): Whether the secret is active. [optional]  # noqa: E501
            allow_owners_unrestricted_ssh_commands (bool): AllowOwnersUnrestrictedSshCommands. [optional]  # noqa: E501
            auto_change_enabled (bool): AutoChangeEnabled. [optional]  # noqa: E501
            auto_change_next_password (str): AutoChangeNextPassword. [optional]  # noqa: E501
            checked_out (bool): Whether the secret is currently checked out. [optional]  # noqa: E501
            check_out_change_password_enabled (bool): CheckOutChangePasswordEnabled. [optional]  # noqa: E501
            check_out_enabled (bool): Whether secret checkout is enabled. [optional]  # noqa: E501
            check_out_interval_minutes (int): Checkout interval, in minutes. [optional]  # noqa: E501
            check_out_minutes_remaining (int): Minutes remaining in current checkout interval. [optional]  # noqa: E501
            check_out_user_display_name (str): Name of user who has checked out the secret. [optional]  # noqa: E501
            check_out_user_id (int): ID of user who has checked out the secret. [optional]  # noqa: E501
            double_lock_id (int): DoubleLockId. [optional]  # noqa: E501
            enable_inherit_permissions (bool): EnableInheritPermissions. [optional]  # noqa: E501
            enable_inherit_secret_policy (bool): Whether the secret policy is inherited from the containing folder. [optional]  # noqa: E501
            failed_password_change_attempts (int): Number of failed password change attempts. [optional]  # noqa: E501
            folder_id (int): Containing folder ID. [optional]  # noqa: E501
            id (int): Secret ID. [optional]  # noqa: E501
            is_double_lock (bool): Whether double lock is enabled. [optional]  # noqa: E501
            is_out_of_sync (bool): Out of sync indicates that a Password is setup for autochange and has failed its last password change attempt or has exceeded the maximum RPC attempts. [optional]  # noqa: E501
            is_restricted (bool): Whether the secret is restricted. [optional]  # noqa: E501
            items ([RestSecretItem]): Secret data fields. [optional]  # noqa: E501
            jumpbox_route_id (str): JumpboxRouteId. [optional]  # noqa: E501
            last_heart_beat_check (datetime): Time of last heartbeat check. [optional]  # noqa: E501
            last_heart_beat_status (HeartbeatStatus): [optional]  # noqa: E501
            last_password_change_attempt (datetime): Time of most recent password change attempt. [optional]  # noqa: E501
            launcher_connect_as_secret_id (int): LauncherConnectAsSecretId. [optional]  # noqa: E501
            name (str): Secret name. [optional]  # noqa: E501
            out_of_sync_reason (str): Reason message if the secret is out of sync. [optional]  # noqa: E501
            password_type_web_script_id (int): PasswordTypeWebScriptId. [optional]  # noqa: E501
            proxy_enabled (bool): ProxyEnabled. [optional]  # noqa: E501
            requires_approval_for_access (bool): RequiresApprovalForAccess. [optional]  # noqa: E501
            requires_comment (bool): RequiresComment. [optional]  # noqa: E501
            response_codes ([str]): ResponseCodes. [optional]  # noqa: E501
            restrict_ssh_commands (bool): RestrictSshCommands. [optional]  # noqa: E501
            secret_policy_id (int): SecretPolicyId. [optional]  # noqa: E501
            secret_template_id (int): Secret template ID. [optional]  # noqa: E501
            secret_template_name (str): Name of secret template. [optional]  # noqa: E501
            session_recording_enabled (bool): Whether session recording is enabled. [optional]  # noqa: E501
            site_id (int): SiteId. [optional]  # noqa: E501
            web_launcher_requires_incognito_mode (bool): WebLauncherRequiresIncognitoMode. [optional]  # noqa: E501
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
        """SecretModel - a model defined in OpenAPI

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
            access_request_workflow_map_id (int): AccessRequestWorkflowMapId. [optional]  # noqa: E501
            active (bool): Whether the secret is active. [optional]  # noqa: E501
            allow_owners_unrestricted_ssh_commands (bool): AllowOwnersUnrestrictedSshCommands. [optional]  # noqa: E501
            auto_change_enabled (bool): AutoChangeEnabled. [optional]  # noqa: E501
            auto_change_next_password (str): AutoChangeNextPassword. [optional]  # noqa: E501
            checked_out (bool): Whether the secret is currently checked out. [optional]  # noqa: E501
            check_out_change_password_enabled (bool): CheckOutChangePasswordEnabled. [optional]  # noqa: E501
            check_out_enabled (bool): Whether secret checkout is enabled. [optional]  # noqa: E501
            check_out_interval_minutes (int): Checkout interval, in minutes. [optional]  # noqa: E501
            check_out_minutes_remaining (int): Minutes remaining in current checkout interval. [optional]  # noqa: E501
            check_out_user_display_name (str): Name of user who has checked out the secret. [optional]  # noqa: E501
            check_out_user_id (int): ID of user who has checked out the secret. [optional]  # noqa: E501
            double_lock_id (int): DoubleLockId. [optional]  # noqa: E501
            enable_inherit_permissions (bool): EnableInheritPermissions. [optional]  # noqa: E501
            enable_inherit_secret_policy (bool): Whether the secret policy is inherited from the containing folder. [optional]  # noqa: E501
            failed_password_change_attempts (int): Number of failed password change attempts. [optional]  # noqa: E501
            folder_id (int): Containing folder ID. [optional]  # noqa: E501
            id (int): Secret ID. [optional]  # noqa: E501
            is_double_lock (bool): Whether double lock is enabled. [optional]  # noqa: E501
            is_out_of_sync (bool): Out of sync indicates that a Password is setup for autochange and has failed its last password change attempt or has exceeded the maximum RPC attempts. [optional]  # noqa: E501
            is_restricted (bool): Whether the secret is restricted. [optional]  # noqa: E501
            items ([RestSecretItem]): Secret data fields. [optional]  # noqa: E501
            jumpbox_route_id (str): JumpboxRouteId. [optional]  # noqa: E501
            last_heart_beat_check (datetime): Time of last heartbeat check. [optional]  # noqa: E501
            last_heart_beat_status (HeartbeatStatus): [optional]  # noqa: E501
            last_password_change_attempt (datetime): Time of most recent password change attempt. [optional]  # noqa: E501
            launcher_connect_as_secret_id (int): LauncherConnectAsSecretId. [optional]  # noqa: E501
            name (str): Secret name. [optional]  # noqa: E501
            out_of_sync_reason (str): Reason message if the secret is out of sync. [optional]  # noqa: E501
            password_type_web_script_id (int): PasswordTypeWebScriptId. [optional]  # noqa: E501
            proxy_enabled (bool): ProxyEnabled. [optional]  # noqa: E501
            requires_approval_for_access (bool): RequiresApprovalForAccess. [optional]  # noqa: E501
            requires_comment (bool): RequiresComment. [optional]  # noqa: E501
            response_codes ([str]): ResponseCodes. [optional]  # noqa: E501
            restrict_ssh_commands (bool): RestrictSshCommands. [optional]  # noqa: E501
            secret_policy_id (int): SecretPolicyId. [optional]  # noqa: E501
            secret_template_id (int): Secret template ID. [optional]  # noqa: E501
            secret_template_name (str): Name of secret template. [optional]  # noqa: E501
            session_recording_enabled (bool): Whether session recording is enabled. [optional]  # noqa: E501
            site_id (int): SiteId. [optional]  # noqa: E501
            web_launcher_requires_incognito_mode (bool): WebLauncherRequiresIncognitoMode. [optional]  # noqa: E501
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
