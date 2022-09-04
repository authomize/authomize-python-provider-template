# SecretTemplateLauncherModel

Secret Template Launcher Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_list** | **int** | User can select from values in this list | [optional] 
**connect_as_command** | **str** | This command is used after a PuTTy session is launched on a Secret that has SSH Proxy enabled and has a Secret set under &#39;Connect As&#39; in the Launcher tab. The default su command is &#39;su - $USERNAME&#39;. $USERNAME is the token used to retrieve the username field from the Secret. Sudo can also be used by specifying &#39;sudo -u $USERNAME /bin/bash&#39;. | [optional] 
**connect_as_command_response** | **str** | The Connect As Command Response is the response from the server prompting for a password. This is used so $productName knows when to send the password to the system. If the response from the server after typing &#39;su - root&#39; is &#39;Password:&#39; then the Connect As Command Response needs to contain &#39;Password:$PASSWORD&#39;. The $CONNECTASPASSWORD token will use the credentials from the Secret set under &#39;Connect As&#39; when prompted. | [optional] 
**deny_list** | **int** | User cannot enter these values. If used with an Allow List, the Deny List will take precedence. | [optional] 
**fields** | [**[SecretTemplateLauncherFieldValueModel]**](SecretTemplateLauncherFieldValueModel.md) | Fields that can be mapped to this launcher | [optional] 
**include_machines_from_dependencies** | **bool** | This will add the list of machine names from the secret dependencies to either the allow list or block list. | [optional] 
**launcher_type_id** | **int** | Unique ID for Launcher Type | [optional] 
**launcher_type_name** | **str** | Name for Launcher Type | [optional] 
**line_ending** | **str** | The line ending that will be append to the end of the Connect As Command. This needs to match the type of line ending required by the system being proxied to. | [optional] 
**restrict_as** | **int** | Restrict what can be selected to come from a list, only allow certain fields, or only deny certain fields. | [optional] 
**restrict_by_secret_field** | **int** | Select a field that will contain the list of items that will restrict the input. | [optional] 
**restrict_user_input** | **bool** | You may specify a field of comma separated hosts or IP addresses that the user will be restricted to. The allow list will allow only these values, while the block list will allow all values except the hosts on the Secret Field.  Example: 192.168.1.2, MACHINE.EXAMPLE.COM, 192.168.1.60 | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


