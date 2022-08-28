# InboxRuleSummary

Query results

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether or not this rule is active | [optional] 
**current_user_subscribed** | **bool** | Only populated when IncludeCurrentUserSubscriptionStatus is passed as true on a rule search | [optional] 
**digest** | **bool** | Whether or not this rule is for a Digest that runs on a schedule. | [optional] 
**inbox_rule_id** | **int** | Inbox Rule ID | [optional] 
**inbox_rule_name** | **str** | The name of the rule | [optional] 
**is_system** | **bool** | Whether or not this rule is a system rule | [optional] 
**notification_types** | **[str]** | Notification Types where this rule is used | [optional] 
**usage_count** | **int** | Number of times this rule has been used in the last 7 days | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


