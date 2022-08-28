# RdpProxyConfigurationViewModel

RdpProxyConfigurationViewModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_site_selection_for_active_directory_accounts** | **bool** | Allows users to select a site when launching or generating proxy credentials for a RDP proxied secret | [optional] 
**days_to_keep_operational_logs** | **int** | The number of days to store RDP proxy logs before they are rolled over | [optional] 
**enable_rdp_proxy** | **bool** | Whether or not to enable the RDP proxy | [optional] 
**enable_remote_host_validation** | **bool** | Whether or not to enforce certificate validation on remote hosts that the proxy connects to | [optional] 
**is_cloud** | **bool** | IsCloud | [optional] 
**proxy_new_secrets_by_default** | **bool** | Whether or not new RDP-enabled secrets should be created with &#39;Proxy Enabled&#39; set | [optional] 
**rdp_proxy_port** | **int** | The port that the RDP proxy will run on | [optional] 
**rdp_server_certificate** | [**RdpProxyCertificateViewModel**](RdpProxyCertificateViewModel.md) |  | [optional] 
**rdp_server_certificate_multipart** | **file** | The certificate that is server when connections begin to the RDP proxy (used \&quot;Content-Type: multipart/form-data\&quot; only) | [optional] 
**rdp_server_certificate_multipart_password** | **str** | The password used to protect the certificate (only used for updating with \&quot;Content-Type: multipart/form-data\&quot; only) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


