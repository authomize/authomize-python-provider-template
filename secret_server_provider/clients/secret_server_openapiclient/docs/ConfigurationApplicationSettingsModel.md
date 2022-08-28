# ConfigurationApplicationSettingsModel

Configuration Application Settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_send_telemetry** | **bool** | Send Anonymized System Metrics Information | [optional] 
**allow_software_update_checks** | **bool** | Allow software update checks. This setting is ignored in cloud environments. | [optional] 
**api_refresh_tokens_enabled** | **bool** | API Refresh Tokens Enabled | [optional] 
**api_session_timeout_days** | **bool, date, datetime, dict, float, int, list, str, none_type** | API session timeout days | [optional] 
**api_session_timeout_hours** | **bool, date, datetime, dict, float, int, list, str, none_type** | API session timeout hours | [optional] 
**api_session_timeout_minutes** | **bool, date, datetime, dict, float, int, list, str, none_type** | API session timeout minutes | [optional] 
**api_session_timeout_unlimited** | **bool** | API session timeout unlimited | [optional] 
**configuration_early_adopter_enabled** | **bool** | Notify when preview releases are available. False by default | [optional] 
**custom_url** | **bool, date, datetime, dict, float, int, list, str, none_type** | Outward accessible url to get to application. This setting is ignored in cloud environments. | [optional] 
**display_downtime_message_to_admins_only** | **bool** | Display Downtime Message To Admins Only | [optional] 
**enable_cred_ssp** | **bool** | Enable Cred SSP for win RM | [optional] 
**enable_syslog_cef_logging** | **bool** | Enable Syslog/CEF Logging | [optional] 
**enable_web_services** | **bool** | Enable Web services | [optional] 
**maximum_token_refreshes_allowed** | **bool, date, datetime, dict, float, int, list, str, none_type** | Maximum Token Refreshes Allowed | [optional] 
**max_secret_log_length** | **bool, date, datetime, dict, float, int, list, str, none_type** | Maximum number of entries in secret log | [optional] 
**mobile_max_offline_days** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Maximum Time for Offline Access on Mobile Devices setting in Secret Server determines how long to cache secret data on the mobile device | [optional] 
**mobile_max_offline_hours** | **bool, date, datetime, dict, float, int, list, str, none_type** | The Maximum Time for Offline Access on Mobile Devices setting in Secret Server determines how long to cache secret data on the mobile device | [optional] 
**obfuscate_personally_identifiable_information** | **bool** | Should Secret Server obfuscate information that could identify a person | [optional] 
**pii_obfuscation_level** | **bool, date, datetime, dict, float, int, list, str, none_type** | Delimit or replace personally identifiable information and automatically remove from Audit Exports  | [optional] 
**prevent_application_from_sleeping** | **bool** | A keep alive thread will run in the background pinging the web URL to make sure IIS does not stop running due to inactivity. This setting is ignored in cloud environments. | [optional] 
**prevent_direct_api_authentication** | **bool** | Prevent non-Application Account users from directly authenticating against the API. | [optional] 
**syslog_cef_log_site** | **bool, date, datetime, dict, float, int, list, str, none_type** | This is the site that the CEF/Syslogs will run on | [optional] 
**syslog_cef_port** | **bool, date, datetime, dict, float, int, list, str, none_type** | Syslog/CEF Protocol | [optional] 
**syslog_cef_protocol** | **bool, date, datetime, dict, float, int, list, str, none_type** | Syslog/CEF Protocol to use when sending logs | [optional] 
**syslog_cef_server** | **bool, date, datetime, dict, float, int, list, str, none_type** | Syslog/CEF Server Address | [optional] 
**syslog_cef_time_zone** | **bool, date, datetime, dict, float, int, list, str, none_type** | Time Zone to use when sending Syslog/CEF Protocol log entries | [optional] 
**tms_installation_path** | **bool, date, datetime, dict, float, int, list, str, none_type** | If TMS is installed, the file location. This setting is ignored in cloud environments. | [optional] 
**win_rm_endpoint_url** | **bool, date, datetime, dict, float, int, list, str, none_type** | Win RM endpoint url | [optional] 
**write_syslog_to_event_log** | **bool** | Enable syslog events to the windows event log. This setting is ignored in cloud environments. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


