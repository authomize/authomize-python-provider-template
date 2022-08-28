"""
    Secret Server Rest API

    REST API documentation for Secret Server. This document describes how to use the REST API. All requests require an authentication token; please see the <a href=\"../OAuth/\">authentication document</a> for more information. The <a href=\"swagger.json\">Swagger specification</a> for this API is also available.  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 11.2.2
    Contact: info@authomize.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plugins.model_utils import (  # noqa: F401
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
from plugins.exceptions import ApiAttributeError


def lazy_import():
    from plugins.model.update_field_value_of_boolean import UpdateFieldValueOfBoolean
    from plugins.model.update_field_value_of_date_time import UpdateFieldValueOfDateTime
    from plugins.model.update_field_value_of_int32_array import UpdateFieldValueOfInt32Array
    from plugins.model.update_field_value_of_optional_boolean import UpdateFieldValueOfOptionalBoolean
    from plugins.model.update_field_value_of_optional_int32 import UpdateFieldValueOfOptionalInt32
    from plugins.model.update_field_value_of_optional_schedule_monthly_day_order_type import UpdateFieldValueOfOptionalScheduleMonthlyDayOrderType
    from plugins.model.update_field_value_of_optional_schedule_monthly_day_type import UpdateFieldValueOfOptionalScheduleMonthlyDayType
    from plugins.model.update_field_value_of_optional_schedule_monthly_type import UpdateFieldValueOfOptionalScheduleMonthlyType
    from plugins.model.update_field_value_of_schedule_change_type import UpdateFieldValueOfScheduleChangeType
    from plugins.model.update_field_value_of_string import UpdateFieldValueOfString
    globals()['UpdateFieldValueOfBoolean'] = UpdateFieldValueOfBoolean
    globals()['UpdateFieldValueOfDateTime'] = UpdateFieldValueOfDateTime
    globals()['UpdateFieldValueOfInt32Array'] = UpdateFieldValueOfInt32Array
    globals()['UpdateFieldValueOfOptionalBoolean'] = UpdateFieldValueOfOptionalBoolean
    globals()['UpdateFieldValueOfOptionalInt32'] = UpdateFieldValueOfOptionalInt32
    globals()['UpdateFieldValueOfOptionalScheduleMonthlyDayOrderType'] = UpdateFieldValueOfOptionalScheduleMonthlyDayOrderType
    globals()['UpdateFieldValueOfOptionalScheduleMonthlyDayType'] = UpdateFieldValueOfOptionalScheduleMonthlyDayType
    globals()['UpdateFieldValueOfOptionalScheduleMonthlyType'] = UpdateFieldValueOfOptionalScheduleMonthlyType
    globals()['UpdateFieldValueOfScheduleChangeType'] = UpdateFieldValueOfScheduleChangeType
    globals()['UpdateFieldValueOfString'] = UpdateFieldValueOfString


class ScheduleUpdateModel(ModelNormal):
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
            'additional_email_addresses': (UpdateFieldValueOfString,),  # noqa: E501
            'change_type': (UpdateFieldValueOfScheduleChangeType,),  # noqa: E501
            'days': (UpdateFieldValueOfOptionalInt32,),  # noqa: E501
            'email_groups': (UpdateFieldValueOfInt32Array,),  # noqa: E501
            'friday': (UpdateFieldValueOfOptionalBoolean,),  # noqa: E501
            'health_check': (UpdateFieldValueOfBoolean,),  # noqa: E501
            'history_size': (UpdateFieldValueOfOptionalInt32,),  # noqa: E501
            'monday': (UpdateFieldValueOfOptionalBoolean,),  # noqa: E501
            'monthly_day': (UpdateFieldValueOfOptionalScheduleMonthlyDayType,),  # noqa: E501
            'monthly_day_of_month': (UpdateFieldValueOfOptionalInt32,),  # noqa: E501
            'monthly_day_order': (UpdateFieldValueOfOptionalScheduleMonthlyDayOrderType,),  # noqa: E501
            'monthly_day_order_recurrence': (UpdateFieldValueOfOptionalInt32,),  # noqa: E501
            'monthly_day_recurrence': (UpdateFieldValueOfOptionalInt32,),  # noqa: E501
            'monthly_schedule_type': (UpdateFieldValueOfOptionalScheduleMonthlyType,),  # noqa: E501
            'saturday': (UpdateFieldValueOfOptionalBoolean,),  # noqa: E501
            'schedule_name': (UpdateFieldValueOfString,),  # noqa: E501
            'send_email': (UpdateFieldValueOfBoolean,),  # noqa: E501
            'send_email_with_high_priority': (UpdateFieldValueOfBoolean,),  # noqa: E501
            'starting_on': (UpdateFieldValueOfDateTime,),  # noqa: E501
            'sunday': (UpdateFieldValueOfOptionalBoolean,),  # noqa: E501
            'thursday': (UpdateFieldValueOfOptionalBoolean,),  # noqa: E501
            'tuesday': (UpdateFieldValueOfOptionalBoolean,),  # noqa: E501
            'wednesday': (UpdateFieldValueOfOptionalBoolean,),  # noqa: E501
            'weeks': (UpdateFieldValueOfOptionalInt32,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'additional_email_addresses': 'additionalEmailAddresses',  # noqa: E501
        'change_type': 'changeType',  # noqa: E501
        'days': 'days',  # noqa: E501
        'email_groups': 'emailGroups',  # noqa: E501
        'friday': 'friday',  # noqa: E501
        'health_check': 'healthCheck',  # noqa: E501
        'history_size': 'historySize',  # noqa: E501
        'monday': 'monday',  # noqa: E501
        'monthly_day': 'monthlyDay',  # noqa: E501
        'monthly_day_of_month': 'monthlyDayOfMonth',  # noqa: E501
        'monthly_day_order': 'monthlyDayOrder',  # noqa: E501
        'monthly_day_order_recurrence': 'monthlyDayOrderRecurrence',  # noqa: E501
        'monthly_day_recurrence': 'monthlyDayRecurrence',  # noqa: E501
        'monthly_schedule_type': 'monthlyScheduleType',  # noqa: E501
        'saturday': 'saturday',  # noqa: E501
        'schedule_name': 'scheduleName',  # noqa: E501
        'send_email': 'sendEmail',  # noqa: E501
        'send_email_with_high_priority': 'sendEmailWithHighPriority',  # noqa: E501
        'starting_on': 'startingOn',  # noqa: E501
        'sunday': 'sunday',  # noqa: E501
        'thursday': 'thursday',  # noqa: E501
        'tuesday': 'tuesday',  # noqa: E501
        'wednesday': 'wednesday',  # noqa: E501
        'weeks': 'weeks',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ScheduleUpdateModel - a model defined in OpenAPI

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
            additional_email_addresses (UpdateFieldValueOfString): [optional]  # noqa: E501
            change_type (UpdateFieldValueOfScheduleChangeType): [optional]  # noqa: E501
            days (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            email_groups (UpdateFieldValueOfInt32Array): [optional]  # noqa: E501
            friday (UpdateFieldValueOfOptionalBoolean): [optional]  # noqa: E501
            health_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            history_size (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            monday (UpdateFieldValueOfOptionalBoolean): [optional]  # noqa: E501
            monthly_day (UpdateFieldValueOfOptionalScheduleMonthlyDayType): [optional]  # noqa: E501
            monthly_day_of_month (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            monthly_day_order (UpdateFieldValueOfOptionalScheduleMonthlyDayOrderType): [optional]  # noqa: E501
            monthly_day_order_recurrence (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            monthly_day_recurrence (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            monthly_schedule_type (UpdateFieldValueOfOptionalScheduleMonthlyType): [optional]  # noqa: E501
            saturday (UpdateFieldValueOfOptionalBoolean): [optional]  # noqa: E501
            schedule_name (UpdateFieldValueOfString): [optional]  # noqa: E501
            send_email (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            send_email_with_high_priority (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            starting_on (UpdateFieldValueOfDateTime): [optional]  # noqa: E501
            sunday (UpdateFieldValueOfOptionalBoolean): [optional]  # noqa: E501
            thursday (UpdateFieldValueOfOptionalBoolean): [optional]  # noqa: E501
            tuesday (UpdateFieldValueOfOptionalBoolean): [optional]  # noqa: E501
            wednesday (UpdateFieldValueOfOptionalBoolean): [optional]  # noqa: E501
            weeks (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
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
        """ScheduleUpdateModel - a model defined in OpenAPI

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
            additional_email_addresses (UpdateFieldValueOfString): [optional]  # noqa: E501
            change_type (UpdateFieldValueOfScheduleChangeType): [optional]  # noqa: E501
            days (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            email_groups (UpdateFieldValueOfInt32Array): [optional]  # noqa: E501
            friday (UpdateFieldValueOfOptionalBoolean): [optional]  # noqa: E501
            health_check (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            history_size (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            monday (UpdateFieldValueOfOptionalBoolean): [optional]  # noqa: E501
            monthly_day (UpdateFieldValueOfOptionalScheduleMonthlyDayType): [optional]  # noqa: E501
            monthly_day_of_month (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            monthly_day_order (UpdateFieldValueOfOptionalScheduleMonthlyDayOrderType): [optional]  # noqa: E501
            monthly_day_order_recurrence (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            monthly_day_recurrence (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
            monthly_schedule_type (UpdateFieldValueOfOptionalScheduleMonthlyType): [optional]  # noqa: E501
            saturday (UpdateFieldValueOfOptionalBoolean): [optional]  # noqa: E501
            schedule_name (UpdateFieldValueOfString): [optional]  # noqa: E501
            send_email (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            send_email_with_high_priority (UpdateFieldValueOfBoolean): [optional]  # noqa: E501
            starting_on (UpdateFieldValueOfDateTime): [optional]  # noqa: E501
            sunday (UpdateFieldValueOfOptionalBoolean): [optional]  # noqa: E501
            thursday (UpdateFieldValueOfOptionalBoolean): [optional]  # noqa: E501
            tuesday (UpdateFieldValueOfOptionalBoolean): [optional]  # noqa: E501
            wednesday (UpdateFieldValueOfOptionalBoolean): [optional]  # noqa: E501
            weeks (UpdateFieldValueOfOptionalInt32): [optional]  # noqa: E501
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
