# InboxRuleSubscriberSummary

A user, group, or external email that is subscribed or unsubscribed to an inbox rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | A display name for this subscriber | [optional] 
**domain_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Active Directory domain ID | [optional] 
**domain_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Active Directory Domain Name | [optional] 
**email_address** | **bool, date, datetime, dict, float, int, list, str, none_type** | EmailAddress | [optional] 
**group_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The subscribers group id.  Either an actual group or a personal group ID for a single user. | [optional] 
**inbox_rule_additional_email_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | InboxRuleAdditionalEmailId | [optional] 
**inbox_rule_subscribers_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The identifier for this subscriber.  Email only subscribers will not have this ID. | [optional] 
**is_group** | **bool** | Is this a group or a single user | [optional] 
**subscribed** | **bool** | True if the user, group, or external email is subscribed.  False if the user is unsubscribed.  Groups and external emails cannot be unsubscribed as they are just removed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


