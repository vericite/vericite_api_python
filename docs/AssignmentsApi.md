# vericite_lms_client.AssignmentsApi

All URIs are relative to *https://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_update_assignment**](AssignmentsApi.md#create_update_assignment) | **POST** /assignments/{contextID}/{assignmentID} | 


# **create_update_assignment**
> list[ExternalContentUploadInfo] create_update_assignment(context_id, assignment_id, consumer, consumer_secret, assignment_data)



Create/update assignment

### Example 
```python
import time
import vericite_lms_client
from vericite_lms_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = vericite_lms_client.AssignmentsApi()
context_id = 'context_id_example' # str | Context ID
assignment_id = 'assignment_id_example' # str | ID of assignment
consumer = 'consumer_example' # str | the consumer
consumer_secret = 'consumer_secret_example' # str | the consumer secret
assignment_data = vericite_lms_client.AssignmentData() # AssignmentData | 

try: 
    api_response = api_instance.create_update_assignment(context_id, assignment_id, consumer, consumer_secret, assignment_data)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AssignmentsApi->create_update_assignment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_id** | **str**| Context ID | 
 **assignment_id** | **str**| ID of assignment | 
 **consumer** | **str**| the consumer | 
 **consumer_secret** | **str**| the consumer secret | 
 **assignment_data** | [**AssignmentData**](AssignmentData.md)|  | 

### Return type

[**list[ExternalContentUploadInfo]**](ExternalContentUploadInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

