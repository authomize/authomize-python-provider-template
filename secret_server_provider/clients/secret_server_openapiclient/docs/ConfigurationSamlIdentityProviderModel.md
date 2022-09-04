# ConfigurationSamlIdentityProviderModel

SAML Identity Provider configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Active status of the Identity Provider. Users can only log-in via an active Identity Provider. | [optional] 
**authn_context** | **str** | When specified, instructs the IDP on how to authenticate the user(optional). | [optional] 
**clock_skew** | **int** | The allowed number of minutes of difference between Secret Server&#39;s clock and the IDP&#39;s clock.  The default is 3 minutes. | [optional] 
**description** | **str** | Description of the Identity Provider. | [optional] 
**disable_assertion_replay_check** | **bool** | When true, SAML messages that were already received from this IDP will be allowed by Secret Server.  Otherwise, resending messages from the IDP will trigger an error. | [optional] 
**disable_audience_restriction_check** | **bool** | A SAML assertion may include an audience restriction URI. This identifies the intended recipient of the SAML assertion. If included it should match the service provider&#39;s name.  When this setting is true, this check is skipped. | [optional] 
**disable_authn_context_check** | **bool** | Disables the authentication context check, which validates that the real authentication method matches the ExpectedAuthnContext method. | [optional] 
**disable_destination_check** | **bool** | When true, the destination URI in the SAML response will not be validated. | [optional] 
**disable_inbound_logout** | **bool** | When true, logout requests coming from this IDP are ignored. | [optional] 
**disable_in_response_to_check** | **bool** | When true, the InResponseTo attribute in SAML messages is not checked. | [optional] 
**disable_pending_logout_check** | **bool** | When true, a SAML logout response will be considered legitimate even if there was no corresponding logout request. | [optional] 
**disable_recipient_check** | **bool** | When true, the built-in check against the AssertionConsumerService URL will be skipped. | [optional] 
**disable_time_period_check** | **bool** | When true, a SAML response is valid regardless of when it was sent. | [optional] 
**display_name** | **str** | The Display Name for the Identity Provider. | [optional] 
**domain_attribute** | **str** | Optional AttributeName to use for matching a Secret Server user&#39;s domain. | [optional] 
**enable_detailed_log** | **bool** | When true, a more detailed log will be generated for SAML logins and logouts. | [optional] 
**enable_slo** | **bool** | When true, logging out of Secret Server will log the user out of this Identity Provider. | [optional] 
**force_authentication** | **bool** | When true, the Identity Provider will be instructed to re-authenticate the user, even if they are already authenticated. | [optional] 
**identity_provider_id** | **int** | SAML Identity Provider Id | [optional] 
**logout_request_life_time** | **int** | The logout request life time. | [optional] 
**name** | **str** | Name of the Identity Provider. | [optional] 
**override_pending_authn_request** | **bool** | When true, an in-progress SP-initiated login may be interrupted by an IDP-initiated login. | [optional] 
**public_certificate** | **str** | The public certificate for the Identity Provider. Base64 encoded | [optional] 
**public_certificate_thumbprint** | **str** | The public certificate thumbprint | [optional] 
**sign_authn_request** | **bool** | When true, the authentication requests sent to this IDP will be signed. | [optional] 
**sign_logout_request** | **bool** | When true, logout requests sent to this IDP will be signed.&lt; | [optional] 
**sign_logout_response** | **bool** | When true, logout responses sent to this IDP will be signed. | [optional] 
**single_logout_service_response_url** | **str** | The URL where Secret Server will send responses to single logout messages. | [optional] 
**single_logout_service_url** | **str** | The URL to send the single logout message to. | [optional] 
**sso_service_binding** | **int** | Method for communicating with the Identity Provider.  HTTPRedirect is recommended in most cases. | [optional] 
**sso_service_url** | **str** | The URL of the Identity Provider where the user will be sent to authenticate. | [optional] 
**username_attribute** | **str** | Optional AttributeName to use for matching a Secret Server user. | [optional] 
**want_assertion_encrypted** | **bool** | When true, Secret Server will expect SAML assertions from this IDP to be encrypted. Unencrypted assertions or assertions that cannot be decrypted will cause an error. | [optional] 
**want_assertion_or_response_signed** | **bool** | When true, Secret Server will expect either SAML assertions or SAML responses from this IDP to be signed. Unsigned assertions/responses and assertions/responses whose signatures cannot be verified will cause an error. | [optional] 
**want_assertion_signed** | **bool** | When true, Secret Server will expect SAML assertions from this IDP to be signed. Unsigned assertions or assertions whose signatures cannot be verified will cause an error. | [optional] 
**want_logout_request_signed** | **bool** | When true, Secret Server will expect logout requests from this IDP to be signed.  Unsigned responses or responses whose signatures cannot be verified will cause an error. | [optional] 
**want_logout_response_signed** | **bool** | When true, Secret Server will expect logout responses from this IDP to be signed.  Unsigned responses or responses whose signatures cannot be verified will cause an error. | [optional] 
**want_saml_response_signed** | **bool** | When true, Secret Server will expect SAML responses from this IDP to be signed. Unsigned responses or responses whose signatures cannot be verified will cause an error. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


