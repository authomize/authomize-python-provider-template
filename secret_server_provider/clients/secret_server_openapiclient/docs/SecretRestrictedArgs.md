# SecretRestrictedArgs

Restricted secret update options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | If the secret requires a comment to view or requires approval to view, a reason for accessing the secret must be provided. | [optional] 
**double_lock_password** | **str** | If the secret is DoubleLocked, this is the DoubleLock password needed to access the secret. | [optional] 
**force_check_in** | **bool** | Force the secret to be checked in, even if checked out by someone else. The user must have the \&quot;Force Check In\&quot; permission. | [optional] 
**include_inactive** | **bool** | If the secret is deactivated, this must be set to true in order to access the secret. The user must also have the \&quot;View Deleted Secrets\&quot; permission. | [optional] 
**new_password** | **str** | New secret password. | [optional] 
**no_auto_checkout** | **bool** | Don&#39;t check out the secret automatically. | [optional] 
**ticket_number** | **str** | If the secret requires a comment to view or requires approval and a user must provide a help desk a ticket number, this is the ticket number to the help desk request. | [optional] 
**ticket_system_id** | **int** | If the secret requires a comment to view or requires approval and a user must provide a help desk a ticket number, this is the id of the help desk system configured in Secret Server that should be used to validate the ticket number. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


