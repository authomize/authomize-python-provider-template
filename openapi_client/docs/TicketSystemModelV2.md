# TicketSystemModelV2

List of Ticket Systems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Ticket System Active status | [optional] 
**add_comments_to_ticket** | **bool** | Send comment to your integrated Ticket System and add it to the incident or change request. | [optional] 
**bmc_change_management_comment_work_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | BMC Remedy Incident Management integration only.  Select work type for comments added. | [optional] 
**bmc_incident_management_comment_work_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | BMC Remedy Incident Management integration only.  Select work type for comments added. | [optional] 
**bmc_remedy_authentication** | **bool, date, datetime, dict, float, int, list, str, none_type** | BMC Remedy integration only. Authentication value that usually represents a login server. | [optional] 
**bmc_remedy_url_endpoint** | **bool, date, datetime, dict, float, int, list, str, none_type** | BMC Remedy integration only.  The SOAP URL endpoint for the BMC Remedy Incident or Change Management.  Should be the CHG_ChangeInterface_WS or HPD_IncidentInterface_WS endpoint. | [optional] 
**description** | **bool, date, datetime, dict, float, int, list, str, none_type** | Ticket System Description | [optional] 
**display_message** | **bool, date, datetime, dict, float, int, list, str, none_type** | Ticket System Ticket Title | [optional] 
**force_require_ticket_number** | [**ForceRequireTicketSystemOptions**](ForceRequireTicketSystemOptions.md) |  | [optional] 
**is_default** | **bool** | Indicates the Ticket System is the default choice. | [optional] 
**name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Ticket System Name | [optional] 
**organization_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Ticket System Organization Id | [optional] 
**power_shell_add_comment_script_arguments** | **bool, date, datetime, dict, float, int, list, str, none_type** | PowerShell integration only.  Optional arguments for the comment script.  Arguemnts are separated by a space. | [optional] 
**power_shell_add_comment_script_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | PowerShell integration only.  Custom PowerSHell script to add a comment to a ticket system. | [optional] 
**power_shell_add_ticket_comment_script_arguments** | **bool, date, datetime, dict, float, int, list, str, none_type** | PowerShell integration only.  Optional arguments for the ticket comment script.  Arguemnts are separated by a space. | [optional] 
**power_shell_add_ticket_comment_script_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | PowerShell integration only.  Custom PowerSHell script to add a comment to a ticket in a ticket system. | [optional] 
**power_shell_run_as_account_secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | PowerShell integration only.  Secret Id for credentials to use to run the Powershell. | [optional] 
**power_shell_ticket_status_script_arguments** | **bool, date, datetime, dict, float, int, list, str, none_type** | PowerShell integration only.  Optional arguments for the ticket status script.  Arguemnts are separated by a space. | [optional] 
**power_shell_ticket_status_script_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Powreshell Integration only.  Custom PowerShell script to get the ticket status. | [optional] 
**service_now_allowed_statuses** | **bool, date, datetime, dict, float, int, list, str, none_type** | ServiceNow integration only.  Statuses to accept from ServiceNow separated by commas. | [optional] 
**service_now_domain_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | ServiceNow integration only. The domain name that hosts the RESTful web services for Ticket System integration. | [optional] 
**site_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Ticket System Site | [optional] 
**system_credential_secret_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Privilged Secret Id for credentials to connect to integrated Ticket Systems. | [optional] 
**ticket_number_error_message** | **bool, date, datetime, dict, float, int, list, str, none_type** | Ticket Number Validation Error Message | [optional] 
**ticket_number_validation** | **bool, date, datetime, dict, float, int, list, str, none_type** | Ticket Number Validation Regex | [optional] 
**ticket_system_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | The unique Id of the ticket system. | [optional] 
**ticket_system_type** | [**TicketSystemTypes**](TicketSystemTypes.md) |  | [optional] 
**view_ticket_url** | **bool, date, datetime, dict, float, int, list, str, none_type** | Ticket System URL pattern | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


