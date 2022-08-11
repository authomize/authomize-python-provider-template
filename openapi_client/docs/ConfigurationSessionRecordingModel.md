# ConfigurationSessionRecordingModel

Session Recording Configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_location_by_site** | **bool** | If archive location changes based on site | [optional] 
**archive_path** | **bool, date, datetime, dict, float, int, list, str, none_type** | The location of the recordings stored on disk | [optional] 
**days_until_archive** | **bool, date, datetime, dict, float, int, list, str, none_type** | The number of days until a recording is archived | [optional] 
**days_until_delete** | **bool, date, datetime, dict, float, int, list, str, none_type** | The number of days before a session recording is deleted | [optional] 
**enable_archive** | **bool** | If recordings should be archived | [optional] 
**enable_delete** | **bool** | If session recordings will be automatically deleted | [optional] 
**enable_hardware_acceleration** | **bool** | If hardware acceleration should be enabled | [optional] 
**enable_inactivity_timeout** | **bool** | If sessions should end if inactive | [optional] 
**enable_on_demand_video_processing** | **bool** | If on demand video processing should be available | [optional] 
**enable_session_recording** | **bool** | Whether or not Session Recording is enabled | [optional] 
**encrypt_archive** | **bool** | If archived session recordings should be encrypted | [optional] 
**hide_recording_indicator** | **bool** | If the recording indicator should be shown | [optional] 
**inactivity_timeout_minutes** | **bool, date, datetime, dict, float, int, list, str, none_type** | The length of inactivity before the session is ended | [optional] 
**max_session_length** | **bool, date, datetime, dict, float, int, list, str, none_type** | The longest a session is allowed to be in hours | [optional] 
**rdp_proxy_record_key_strokes** | **bool** | If proxied RDP sessions should have keystrokes recorded | [optional] 
**rdp_proxy_record_video** | **bool** | If proxied RDP sessions should have video recorded | [optional] 
**ssh_proxy_record_key_strokes** | **bool** | If proxied SSH sessions should have keystrokes recorded | [optional] 
**ssh_proxy_record_video** | **bool** | If proxied SSH sessions should have video recorded | [optional] 
**store_in_database** | **bool** | If session recordings should be stored in the database | [optional] 
**use_temporary_archives** | **bool** | If the archive location should store temporary session recording data instead of the database | [optional] 
**video_codec_id** | **bool, date, datetime, dict, float, int, list, str, none_type** | Which video codec to use for session recordings on OSX | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


