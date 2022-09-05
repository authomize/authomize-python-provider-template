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
    from secret_server_openapiclient.model.update_field_value_of_boolean import UpdateFieldValueOfBoolean
    from secret_server_openapiclient.model.update_field_value_of_int32 import UpdateFieldValueOfInt32
    from secret_server_openapiclient.model.update_field_value_of_string import UpdateFieldValueOfString
    globals()['UpdateFieldValueOfBoolean'] = UpdateFieldValueOfBoolean
    globals()['UpdateFieldValueOfInt32'] = UpdateFieldValueOfInt32
    globals()['UpdateFieldValueOfString'] = UpdateFieldValueOfString


class ConfigurationSamlIdentityProviderPatchModel(ModelNormal):
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
            'active': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'authn_context': (UpdateFieldValueOfString, none_type,),  # noqa: E501
            'clock_skew': (UpdateFieldValueOfInt32, none_type,),  # noqa: E501
            'description': (UpdateFieldValueOfString, none_type,),  # noqa: E501
            'disable_assertion_replay_check': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'disable_audience_restriction_check': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'disable_authn_context_check': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'disable_destination_check': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'disable_inbound_logout': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'disable_in_response_to_check': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'disable_pending_logout_check': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'disable_recipient_check': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'disable_time_period_check': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'display_name': (UpdateFieldValueOfString, none_type,),  # noqa: E501
            'domain_attribute': (UpdateFieldValueOfString, none_type,),  # noqa: E501
            'enable_detailed_log': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'enable_slo': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'force_authentication': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'identity_provider_id': (int, none_type,),  # noqa: E501
            'logout_request_life_time': (UpdateFieldValueOfInt32, none_type,),  # noqa: E501
            'name': (UpdateFieldValueOfString, none_type,),  # noqa: E501
            'override_pending_authn_request': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'public_certificate': (UpdateFieldValueOfString, none_type,),  # noqa: E501
            'sign_authn_request': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'sign_logout_request': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'sign_logout_response': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'single_logout_service_response_url': (UpdateFieldValueOfString, none_type,),  # noqa: E501
            'single_logout_service_url': (UpdateFieldValueOfString, none_type,),  # noqa: E501
            'sso_service_binding': (UpdateFieldValueOfInt32, none_type,),  # noqa: E501
            'sso_service_url': (UpdateFieldValueOfString, none_type,),  # noqa: E501
            'username_attribute': (UpdateFieldValueOfString, none_type,),  # noqa: E501
            'want_assertion_encrypted': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'want_assertion_or_response_signed': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'want_assertion_signed': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'want_logout_request_signed': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'want_logout_response_signed': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
            'want_saml_response_signed': (UpdateFieldValueOfBoolean, none_type,),  # noqa: E501
        }
    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'active': 'active',  # noqa: E501
        'authn_context': 'authnContext',  # noqa: E501
        'clock_skew': 'clockSkew',  # noqa: E501
        'description': 'description',  # noqa: E501
        'disable_assertion_replay_check': 'disableAssertionReplayCheck',  # noqa: E501
        'disable_audience_restriction_check': 'disableAudienceRestrictionCheck',  # noqa: E501
        'disable_authn_context_check': 'disableAuthnContextCheck',  # noqa: E501
        'disable_destination_check': 'disableDestinationCheck',  # noqa: E501
        'disable_inbound_logout': 'disableInboundLogout',  # noqa: E501
        'disable_in_response_to_check': 'disableInResponseToCheck',  # noqa: E501
        'disable_pending_logout_check': 'disablePendingLogoutCheck',  # noqa: E501
        'disable_recipient_check': 'disableRecipientCheck',  # noqa: E501
        'disable_time_period_check': 'disableTimePeriodCheck',  # noqa: E501
        'display_name': 'displayName',  # noqa: E501
        'domain_attribute': 'domainAttribute',  # noqa: E501
        'enable_detailed_log': 'enableDetailedLog',  # noqa: E501
        'enable_slo': 'enableSLO',  # noqa: E501
        'force_authentication': 'forceAuthentication',  # noqa: E501
        'identity_provider_id': 'identityProviderId',  # noqa: E501
        'logout_request_life_time': 'logoutRequestLifeTime',  # noqa: E501
        'name': 'name',  # noqa: E501
        'override_pending_authn_request': 'overridePendingAuthnRequest',  # noqa: E501
        'public_certificate': 'publicCertificate',  # noqa: E501
        'sign_authn_request': 'signAuthnRequest',  # noqa: E501
        'sign_logout_request': 'signLogoutRequest',  # noqa: E501
        'sign_logout_response': 'signLogoutResponse',  # noqa: E501
        'single_logout_service_response_url': 'singleLogoutServiceResponseUrl',  # noqa: E501
        'single_logout_service_url': 'singleLogoutServiceUrl',  # noqa: E501
        'sso_service_binding': 'ssoServiceBinding',  # noqa: E501
        'sso_service_url': 'ssoServiceUrl',  # noqa: E501
        'username_attribute': 'usernameAttribute',  # noqa: E501
        'want_assertion_encrypted': 'wantAssertionEncrypted',  # noqa: E501
        'want_assertion_or_response_signed': 'wantAssertionOrResponseSigned',  # noqa: E501
        'want_assertion_signed': 'wantAssertionSigned',  # noqa: E501
        'want_logout_request_signed': 'wantLogoutRequestSigned',  # noqa: E501
        'want_logout_response_signed': 'wantLogoutResponseSigned',  # noqa: E501
        'want_saml_response_signed': 'wantSAMLResponseSigned',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ConfigurationSamlIdentityProviderPatchModel - a model defined in OpenAPI

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
            active (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            authn_context (UpdateFieldValueOfString): [optional]  # noqa: E501
            clock_skew (UpdateFieldValueOfInt32): [optional]  # noqa: E501
            description (UpdateFieldValueOfString): [optional]  # noqa: E501
            disable_assertion_replay_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_audience_restriction_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_authn_context_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_destination_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_inbound_logout (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_in_response_to_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_pending_logout_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_recipient_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_time_period_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            display_name (UpdateFieldValueOfString): [optional]  # noqa: E501
            domain_attribute (UpdateFieldValueOfString): [optional]  # noqa: E501
            enable_detailed_log (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            enable_slo (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            force_authentication (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            identity_provider_id (int): SAML Identity Provider Id. [optional]  # noqa: E501
            logout_request_life_time (UpdateFieldValueOfInt32): [optional]  # noqa: E501
            name (UpdateFieldValueOfString): [optional]  # noqa: E501
            override_pending_authn_request (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            public_certificate (UpdateFieldValueOfString): [optional]  # noqa: E501
            sign_authn_request (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            sign_logout_request (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            sign_logout_response (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            single_logout_service_response_url (UpdateFieldValueOfString): [optional]  # noqa: E501
            single_logout_service_url (UpdateFieldValueOfString): [optional]  # noqa: E501
            sso_service_binding (UpdateFieldValueOfInt32): [optional]  # noqa: E501
            sso_service_url (UpdateFieldValueOfString): [optional]  # noqa: E501
            username_attribute (UpdateFieldValueOfString): [optional]  # noqa: E501
            want_assertion_encrypted (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            want_assertion_or_response_signed (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            want_assertion_signed (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            want_logout_request_signed (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            want_logout_response_signed (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            want_saml_response_signed (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
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
        """ConfigurationSamlIdentityProviderPatchModel - a model defined in OpenAPI

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
            active (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            authn_context (UpdateFieldValueOfString): [optional]  # noqa: E501
            clock_skew (UpdateFieldValueOfInt32): [optional]  # noqa: E501
            description (UpdateFieldValueOfString): [optional]  # noqa: E501
            disable_assertion_replay_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_audience_restriction_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_authn_context_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_destination_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_inbound_logout (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_in_response_to_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_pending_logout_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_recipient_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            disable_time_period_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            display_name (UpdateFieldValueOfString): [optional]  # noqa: E501
            domain_attribute (UpdateFieldValueOfString): [optional]  # noqa: E501
            enable_detailed_log (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            enable_slo (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            force_authentication (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            identity_provider_id (int): SAML Identity Provider Id. [optional]  # noqa: E501
            logout_request_life_time (UpdateFieldValueOfInt32): [optional]  # noqa: E501
            name (UpdateFieldValueOfString): [optional]  # noqa: E501
            override_pending_authn_request (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            public_certificate (UpdateFieldValueOfString): [optional]  # noqa: E501
            sign_authn_request (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            sign_logout_request (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            sign_logout_response (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            single_logout_service_response_url (UpdateFieldValueOfString): [optional]  # noqa: E501
            single_logout_service_url (UpdateFieldValueOfString): [optional]  # noqa: E501
            sso_service_binding (UpdateFieldValueOfInt32): [optional]  # noqa: E501
            sso_service_url (UpdateFieldValueOfString): [optional]  # noqa: E501
            username_attribute (UpdateFieldValueOfString): [optional]  # noqa: E501
            want_assertion_encrypted (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            want_assertion_or_response_signed (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            want_assertion_signed (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            want_logout_request_signed (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            want_logout_response_signed (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            want_saml_response_signed (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
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
