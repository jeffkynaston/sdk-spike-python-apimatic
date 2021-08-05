# Documents

```python
documents_controller = client.documents
```

## Class Name

`DocumentsController`


# Upload a Document

Upload a document

```python
def upload_a_document(self,
                     body,
                     trace_id=None,
                     user_agent=None,
                     end_user_device_id=None,
                     end_user_ip=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateDocumentUploadRequest`](/doc/models/create-document-upload-request.md) | Body, Required | Document metadata |
| `trace_id` | `string` | Header, Optional | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. |
| `user_agent` | `string` | Header, Optional | A string representing the User Agent. Required only when the request is not coming from the end user's browser. |
| `end_user_device_id` | `string` | Header, Optional | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. |
| `end_user_ip` | `string` | Header, Optional | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. |

## Response Type

[`DocumentUpload`](/doc/models/document-upload.md)

## Example Usage

```python
body = CreateDocumentUploadRequest()
body.payer = PayerId()
body.payer.id = '8f51c396-6e29-49a6-ba5a-1a31d5420158'
body.mtype = 'INVOICE'
body.file_type = FileTypeEnum.JPG
body.filename = 'invoice_123.pdf'

result = documents_controller.upload_a_document(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |

