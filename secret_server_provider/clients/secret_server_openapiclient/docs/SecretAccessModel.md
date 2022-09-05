# SecretAccessModel

The Secret Access model object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_request_workflow_map_id** | **int** | The Id of the Access Request Workflow Map. | [optional] 
**approver_display_name** | **str** | The Display Name of the Approver of the request | [optional] 
**completed** | **bool** | Indicating if request has been completed | [optional] 
**current_user_restricted_from_reviewing** | **bool** | Indicating if current user is restricted from viewing the request | [optional] 
**expiration_date** | **datetime** | The Expiration Date of the request | [optional] 
**folder_id** | **int** | The Folder Id of the Secret associated to the access request. | [optional] 
**has_workflow** | **bool** | Indicating if request is associated to a Work Flow | [optional] 
**request_comment** | **str** | The Comment of the request. | [optional] 
**request_date** | **datetime** | The Date of the request. | [optional] 
**requesting_user_id** | **int** | The Id of the User requesting access. | [optional] 
**request_username** | **str** | The Username of the User requesting access. | [optional] 
**response_comment** | **str** | The Comment of the response to the request | [optional] 
**response_date** | **datetime** | The Date of the response to the request | [optional] 
**review_status_message** | **str** | The Review Status Message of the request | [optional] 
**secret_access_request_id** | **int** | The Id of the Secret Access Request. | [optional] 
**secret_id** | **int** | The Id of the Secret associated to the access request. | [optional] 
**secret_name** | **str** | The Name of the Secret associated to the access request. | [optional] 
**start_date** | **datetime** | The Start Date of the request. | [optional] 
**status** | [**AccessRequestState**](AccessRequestState.md) |  | [optional] 
**status_description** | **str** | The Status Description of the request | [optional] 
**ticket_number** | **str** | The Ticket Number of the request | [optional] 
**ticket_system_id** | **int** | The Ticket System Id of the request | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


