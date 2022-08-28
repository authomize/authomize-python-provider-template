# PasswordTypeModel

Displays the properties of a Password Type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the Password Type is Active  | [optional] 
**allows_privileged_account** | **bool** | Allows a Default Privileged Account | [optional] 
**can_edit** | **bool** | Whether the Password Type can be edited | [optional] 
**custom_port** | **int** | Custom Port | [optional] 
**exit_command** | **str** | Exit Command | [optional] 
**fields** | [**[IRestPasswordTypeField]**](IRestPasswordTypeField.md) | Password Type Fields | [optional] 
**has_commands** | **bool** | Whether Commands Exist | [optional] 
**has_ldap_settings** | **bool** | Whether LDAP Settings Exist | [optional] 
**heartbeat_script_args** | **str** | Heartbeat Script Args | [optional] 
**heartbeat_script_id** | **int** | Heartbeat Script Id | [optional] 
**ignore_ssl** | **bool** | Whether Password Type ignores SSL warnings | [optional] 
**is_web** | **bool** | Whether Is Web | [optional] 
**ldap_connection_settings_id** | **int** | LDAP Connection Settings Id | [optional] 
**line_ending** | [**LineEnding**](LineEnding.md) |  | [optional] 
**mainframe_connection_string** | **str** | Mainframe Connection String | [optional] 
**name** | **str** | Password Type Name | [optional] 
**odbc_connection_string** | **str** | ODBC Connection String | [optional] 
**password_type_id** | **int** | Password Type Id | [optional] 
**rpc_script_args** | **str** | RPC Script Args | [optional] 
**rpc_script_id** | **int** | RPC Script Id | [optional] 
**runner_type** | [**RunnerType**](RunnerType.md) |  | [optional] 
**scan_item_template_id** | **int** | Scan Template Id | [optional] 
**type_name** | **str** | Federator Type | [optional] 
**use_ssl** | **bool** | Whether Password Type uses SSL | [optional] 
**use_username_and_password** | **bool** | Whether Password Type uses both Username and Password | [optional] 
**valid_for_takeover** | **bool** | Whether is Valid For Takeover | [optional] 
**windows_custom_ports** | **str** | Custom Ports for Windows | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


