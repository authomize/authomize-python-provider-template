# ConfigurationEmailModel

Outgoing email server configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_email_address** | **str** | All emails will be sent from this address | [optional] 
**from_email_name** | **str** | This is the &#39;From&#39; friendly name for emails that are sent. It can be left empty. | [optional] 
**send_legacy_emails** | **bool** | Send Legacy Emails | [optional] 
**smtp_check_certificate_revocation** | **bool** | Check Certificate Revocation when in Implicit SSL Connection Mode | [optional] 
**smtp_domain** | **str** | SMTP user domain | [optional] 
**smtp_password** | **str** | SMTP user password | [optional] 
**smtp_port** | **int** | Custom port, otherwise the default | [optional] 
**smtp_server** | **str** | The resolvable and reachable host name for the outgoing SMTP server | [optional] 
**smtp_use_credentials** | **bool** | true if credentials are set, false if anonymous | [optional] 
**smtp_use_implicit_ssl** | **bool** | Implicit SSL Connection Mode | [optional] 
**smtp_user_name** | **str** | SMTP user name | [optional] 
**smtp_use_ssl** | **bool** | Use SSL to connect | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


