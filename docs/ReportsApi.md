# vericite_lms_client.ReportsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report_urls**](ReportsApi.md#get_report_urls) | **GET** /reports/urls/{contextID} | 
[**get_scores**](ReportsApi.md#get_scores) | **GET** /reports/scores/{contextID} | 
[**submit_request**](ReportsApi.md#submit_request) | **POST** /reports/submit/request/{contextID}/{assignmentID}/{userID} | 


# **get_report_urls**
> list[ReportURLLinkReponse] get_report_urls(context_id, assignment_id_filter, consumer, consumer_secret, token_user, token_user_role, user_id_filter=user_id_filter, external_content_id_filter=external_content_id_filter, print_report_page=print_report_page)



Retrieves URLS for the reports

### Example 
```python
from __future__ import print_statement
import time
import vericite_lms_client
from vericite_lms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vericite_lms_client.ReportsApi()
context_id = 'context_id_example' # str | Context ID
assignment_id_filter = 'assignment_id_filter_example' # str | ID of assignment to filter results on
consumer = 'consumer_example' # str | the consumer
consumer_secret = 'consumer_secret_example' # str | the consumer secret
token_user = 'token_user_example' # str | ID of user who will view the report
token_user_role = 'token_user_role_example' # str | role of user who will view the report
user_id_filter = 'user_id_filter_example' # str | ID of user to filter results on (optional)
external_content_id_filter = 'external_content_id_filter_example' # str | external content id to filter results on (optional)
print_report_page = true # bool | flag to indicate a request for the print report page URL (optional)

try: 
    api_response = api_instance.get_report_urls(context_id, assignment_id_filter, consumer, consumer_secret, token_user, token_user_role, user_id_filter=user_id_filter, external_content_id_filter=external_content_id_filter, print_report_page=print_report_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_report_urls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **str**| Context ID | 
 **assignment_id_filter** | **str**| ID of assignment to filter results on | 
 **consumer** | **str**| the consumer | 
 **consumer_secret** | **str**| the consumer secret | 
 **token_user** | **str**| ID of user who will view the report | 
 **token_user_role** | **str**| role of user who will view the report | 
 **user_id_filter** | **str**| ID of user to filter results on | [optional] 
 **external_content_id_filter** | **str**| external content id to filter results on | [optional] 
 **print_report_page** | **bool**| flag to indicate a request for the print report page URL | [optional] 

### Return type

[**list[ReportURLLinkReponse]**](ReportURLLinkReponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scores**
> list[ReportScoreReponse] get_scores(context_id, consumer, consumer_secret, assignment_id=assignment_id, user_id=user_id, external_content_id=external_content_id)



Retrieves scores for the reports

### Example 
```python
from __future__ import print_statement
import time
import vericite_lms_client
from vericite_lms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vericite_lms_client.ReportsApi()
context_id = 'context_id_example' # str | Context ID
consumer = 'consumer_example' # str | the consumer
consumer_secret = 'consumer_secret_example' # str | the consumer secret
assignment_id = 'assignment_id_example' # str | ID of assignment (optional)
user_id = 'user_id_example' # str | ID of user (optional)
external_content_id = 'external_content_id_example' # str | external content id (optional)

try: 
    api_response = api_instance.get_scores(context_id, consumer, consumer_secret, assignment_id=assignment_id, user_id=user_id, external_content_id=external_content_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_scores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **str**| Context ID | 
 **consumer** | **str**| the consumer | 
 **consumer_secret** | **str**| the consumer secret | 
 **assignment_id** | **str**| ID of assignment | [optional] 
 **user_id** | **str**| ID of user | [optional] 
 **external_content_id** | **str**| external content id | [optional] 

### Return type

[**list[ReportScoreReponse]**](ReportScoreReponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_request**
> list[ExternalContentUploadInfo] submit_request(context_id, assignment_id, user_id, immediate_score_only, consumer, consumer_secret, report_meta_data)



Request a file submission

### Example 
```python
from __future__ import print_statement
import time
import vericite_lms_client
from vericite_lms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vericite_lms_client.ReportsApi()
context_id = 'context_id_example' # str | Context ID
assignment_id = 'assignment_id_example' # str | ID of assignment
user_id = 'user_id_example' # str | ID of user
immediate_score_only = true # bool | Will only run the report for immediate scoring
consumer = 'consumer_example' # str | the consumer
consumer_secret = 'consumer_secret_example' # str | the consumer secret
report_meta_data = vericite_lms_client.ReportMetaData() # ReportMetaData | 

try: 
    api_response = api_instance.submit_request(context_id, assignment_id, user_id, immediate_score_only, consumer, consumer_secret, report_meta_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->submit_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **str**| Context ID | 
 **assignment_id** | **str**| ID of assignment | 
 **user_id** | **str**| ID of user | 
 **immediate_score_only** | **bool**| Will only run the report for immediate scoring | 
 **consumer** | **str**| the consumer | 
 **consumer_secret** | **str**| the consumer secret | 
 **report_meta_data** | [**ReportMetaData**](ReportMetaData.md)|  | 

### Return type

[**list[ExternalContentUploadInfo]**](ExternalContentUploadInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

