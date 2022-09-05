# ConfigurationLoginTwoFactorRadiusModel

RADIUS Two Factor Login Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt_user_password** | **bool** | If checked, Secret Server will automatically try to authenticate to RADIUS using the user&#39;s local password after it is entered during login.  If RADIUS authentication fails, the user will be prompted for the correct RADIUS password.Please note that this is not supported when Integrated Windows  Authentication is enabled | [optional] 
**client_port_range** | **str** | RADIUS Client Port Range | [optional] 
**default_username** | **str** | RADIUS Default Username | [optional] 
**disable_nas_ip_address_attribute** | **bool** | Disable Radius NAS-IP-Address Attribute | [optional] 
**enable** | **bool** | Enabling RADIUS integration will allow another form of two factor authentication for users | [optional] 
**enable_failover_server** | **bool** | Enabling a Failover RADIUS server will allow another server to fail over to | [optional] 
**enable_radius_nas_id** | **bool** | Configure the NAS-Identifier that will be sent with the RADIUS Access-Request | [optional] 
**failover_server_ip** | **str** | The IP address of your Failover RADIUS server | [optional] 
**failover_server_port** | **int** | Failover RADIUS Server Port | [optional] 
**failover_shared_secret** | **str** | Failover RADIUS Shared Secret | [optional] 
**failover_timeout_seconds** | **int** | Failover Time Out (seconds) | [optional] 
**login_explanation** | **str** | RADIUS Login Explanation | [optional] 
**nas_id** | **str** | The NAS-Identifier attribute value that will be sent with the RADIUS Access-Request | [optional] 
**protocol** | **int** | Authentication Protocol | [optional] 
**server_ip** | **str** | The IP address of your RADIUS server | [optional] 
**server_port** | **int** | RADIUS Server Port | [optional] 
**shared_secret** | **str** | RADIUS Shared Secret for All Users | [optional] 
**shared_secret_same_for_all_users** | **bool** | Use Same RADIUS Shared Secret for All Users | [optional] 
**timeout_seconds** | **int** | Time Out (seconds) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


