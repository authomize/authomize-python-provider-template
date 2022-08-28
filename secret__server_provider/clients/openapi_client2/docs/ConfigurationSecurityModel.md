# ConfigurationSecurityModel

Security Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_web_service_http_get** | **bool** | Allows the Http Get verb for Web Services.  This allows REST-style calls to many Web Service methods, but reduces security | [optional] 
**audit_tls_errors** | **bool** | When enabled, this setting will add audits for TLS certificate validation. Auditing will apply to all Active Directory domains using LDAPS and Syslog using TLS. Certificate policy options including ignoring certificate revocation failures applies to Syslog using TLS only. The default is the most strict so the certificate chain policy may need to be updated. TLS errors will be logged to Security Audit Log found on the Administration page | [optional] 
**audit_tls_errors_debug** | **bool** | Enable TLS Debugging and Connection Tracking | [optional] 
**certificate_chain_policy_options** | **str** | Certificate chain policy options | [optional] 
**client_certificate_ids** | **str** | Client Certificate Thumbprint(s) | [optional] 
**database_integrity_monitoring_symmetric_key** | **str** | The secure symmetric key to use when sending data to the separate Database Integrity Monitoring service. This can be retrieved from the configuration utility in the Database Integrity Monitoring service install location | [optional] 
**enable_database_integrity_monitoring** | **bool** | When enabled, Secret Server will communicate with the separately installed Database Integrity Monitoring service.  This service will send email alerts if it detects possible database tampering.  Access to Secret Server&#39;s database and web servers should be restricted to highly trusted individuals only | [optional] 
**enable_file_restrictions** | **bool** | Enable restrictions on the types or sizes of files that can be uploaded into Secret Server | [optional] 
**enable_frame_blocking** | **bool** | Enable Frame Blocking | [optional] 
**enable_hsts** | **bool** | Enable HTTP Strict Transport Security | [optional] 
**enable_secret_erase** | **bool** | Enable secret erase functionality | [optional] 
**file_extension_restrictions** | **str** | File Extension Restrictions | [optional] 
**fips_enabled** | **bool** | Allow only FIPS compliant encryption schemes to be used | [optional] 
**force_https** | **bool** | By requiring HTTPS, users will not be able to access Secret Server using HTTP | [optional] 
**hide_version_number** | **bool** | This will disable the VersionGet SOAP call. It will also hide the Secret Server Version Numbers from the Headers and Footer | [optional] 
**hsts_max_age** | **int** | Maximum Age (in seconds) | [optional] 
**ignore_certificate_revocation_failures** | **bool** | Indicates if X509RevocationMode.NoCheck certificate chain policy option is set | [optional] 
**maximum_file_size_bytes** | **str** | Maximum File Size (bytes) | [optional] 
**maximum_file_size_supported** | **bool** | Maximum File Size supported by ASP.NET | [optional] 
**secret_erase_workflow** | **int** | The workflow used by secret erase | [optional] 
**web_password_filler_requires_full_domain_match** | **bool** | When enabled, the Web Password Filler will only allow exact domain matches.  When disabled, subdomains such as https://sub.google.com will match http://google.com Secrets.  The recommended setting is enabled. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


