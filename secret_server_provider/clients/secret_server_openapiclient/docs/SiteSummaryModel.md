# SiteSummaryModel

Site Summary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Is Site Active | [optional] 
**is_local** | **bool** | Indicates if this site is the local site that cannot have engines assigned | [optional] 
**last_activity** | **bool, date, datetime, dict, float, int, list, str, none_type** | Last Date of Activity of Site | [optional] 
**num_engines_missing_net_framework** | **bool, date, datetime, dict, float, int, list, str, none_type** | The number of engines on the site missing the minimum DotNet Framework | [optional] 
**num_engines_without_ability_to_restart_service** | **bool, date, datetime, dict, float, int, list, str, none_type** | The number of engines on the site without the ability to restart the service, required for upgrades | [optional] 
**offline_engine_count** | **bool, date, datetime, dict, float, int, list, str, none_type** | Offline Engine Count of Site | [optional] 
**online_engine_count** | **bool, date, datetime, dict, float, int, list, str, none_type** | Online Engine Count of Site | [optional] 
**site_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Id of Site | [optional] 
**site_metrics** | [**[SiteMetric]**](SiteMetric.md) | List of Metrics for this site such as ConnectionStatusOffline, ConnectionStatusOnline, ActivationStatusPending, LostConnection, and more.  Only returned on a search when IncludeSiteMetrics is true. | [optional] 
**site_name** | **bool, date, datetime, dict, float, int, list, str, none_type** | Name of Site | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


