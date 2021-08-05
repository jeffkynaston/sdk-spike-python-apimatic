# Client Secrets

```python
client_secrets_controller = client.client_secrets
```

## Class Name

`ClientSecretsController`


# Create a Single-Use Client Secret

Create a single-use Client Secret

```python
def create_a_single_use_client_secret(self,
                                     body,
                                     trace_id=None,
                                     user_agent=None,
                                     end_user_device_id=None,
                                     end_user_ip=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ClientSecretsRequest`](/doc/models/client-secrets-request.md) | Body, Required | Create a single-use Client Secret to be shared with browser for tokenization of sensitive data such as credit card numbers. The Client Secret expires after 60 seconds. |
| `trace_id` | `string` | Header, Optional | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. |
| `user_agent` | `string` | Header, Optional | A string representing the User Agent. Required only when the request is not coming from the end user's browser. |
| `end_user_device_id` | `string` | Header, Optional | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. |
| `end_user_ip` | `string` | Header, Optional | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. |

## Response Type

[`ClientSecretsResponse`](/doc/models/client-secrets-response.md)

## Example Usage

```python
body = ClientSecretsRequest()

result = client_secrets_controller.create_a_single_use_client_secret(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |

