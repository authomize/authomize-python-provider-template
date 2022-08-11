# SshProxyConfigurationViewModel

SshProxyConfigurationViewModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_port_range** | **bool, date, datetime, dict, float, int, list, str, none_type** | Range of unused ports available on the SSH Proxy endpoint to be used for Jumpbox port forwarding | [optional] 
**days_to_keep_operational_logs** | **bool, date, datetime, dict, float, int, list, str, none_type** | The number of days to store SSH proxy logs before they are rolled over | [optional] 
**enable_password_hiding** | **bool** | Enable to hide passwords from SSH keystroke capture. This prevents logging user input on lines that are determined to be a password prompt. | [optional] 
**enable_proxy_block_listing** | **bool** | Enable block listing of IP Addresses that connect and fail to authenticate too many times | [optional] 
**enable_proxy_inactivity_timeout** | **bool** | Whether or not the proxy should disconnect inactive sessions | [optional] 
**enable_ssh_proxy** | **bool** | Whether or not the SSH proxy is enabled | [optional] 
**enable_ssh_public_key_auth** | **bool** | Whether or not the SSH Terminal can allow key authentication | [optional] 
**enable_ssh_terminal** | **bool** | Whether or not the SSH terminal is enabled | [optional] 
**enable_ssh_tunneling** | **bool** | Whether or not to allow SSH tunneling through the proxy for proxied RDP sessions | [optional] 
**enable_terminal_inactivity_timeout** | **bool** | Whether or not the SSH terminal should disconnect inactive sessions | [optional] 
**enable_window_title_change_command** | **bool** | Send window title change command on startup | [optional] 
**is_cloud** | **bool** | IsCloud | [optional] 
**password_regex_filter** | **bool, date, datetime, dict, float, int, list, str, none_type** | Regular Expression used to identify password prompts. The default expression search for either prompts beginning with &#39;sudo password for&#39; or prompts ending with &#39;password:&#39; | [optional] 
**proxy_auto_block_listing_max_num** | **bool, date, datetime, dict, float, int, list, str, none_type** | The number of failed authentication attempts before being blocked | [optional] 
**proxy_auto_block_listing_time_frame_minutes** | **bool, date, datetime, dict, float, int, list, str, none_type** | The time frame in which all the failed attempts must happen before being blocked | [optional] 
**proxy_inactivity_timeout_seconds** | **bool, date, datetime, dict, float, int, list, str, none_type** | The amount of time in seconds to wait before disconnecting inactive proxy sessions | [optional] 
**proxy_new_secrets_by_default** | **bool** | Whether or not new SSH-enabled secrets should be created with &#39;Proxy Enabled&#39; set | [optional] 
**ssh_host_key** | **bool, date, datetime, dict, float, int, list, str, none_type** | The host key that will the proxy will serve | [optional] 
**ssh_proxy_banner** | **bool, date, datetime, dict, float, int, list, str, none_type** | The banner that is display when someone opens an shell connection to the proxy | [optional] 
**ssh_proxy_host_fingerprint** | **bool, date, datetime, dict, float, int, list, str, none_type** | The fingerprint of the host key that the proxy will serve | [optional] 
**ssh_proxy_port** | **bool, date, datetime, dict, float, int, list, str, none_type** | The port that that SSH proxy runs on | [optional] 
**ssh_terminal_banner** | **bool, date, datetime, dict, float, int, list, str, none_type** | The banner that is displayed when someone authenticates to the SSH terminal | [optional] 
**terminal_inactivity_timeout_seconds** | **bool, date, datetime, dict, float, int, list, str, none_type** | The amount of time in seconds to wait before disconnecting inactive terminal sessions | [optional] 
**tunnel_keep_alive_in_seconds** | **bool, date, datetime, dict, float, int, list, str, none_type** | Keep alive signals to local port forwarding tunnels at this interval (in seconds). Prevents port forwarding tunnels from closing. (0-86400)  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


