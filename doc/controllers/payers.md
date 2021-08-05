# Payers

```python
payers_controller = client.payers
```

## Class Name

`PayersController`

## Methods

* [Create a Payer](/doc/controllers/payers.md#create-a-payer)
* [Retrieve a Payer](/doc/controllers/payers.md#retrieve-a-payer)
* [Update a Payer](/doc/controllers/payers.md#update-a-payer)
* [Delete a Payer](/doc/controllers/payers.md#delete-a-payer)


# Create a Payer

Create a Payer

```python
def create_a_payer(self,
                  body,
                  trace_id=None,
                  user_agent=None,
                  end_user_device_id=None,
                  end_user_ip=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreatePayerRequest`](/doc/models/create-payer-request.md) | Body, Required | Payer to create |
| `trace_id` | `string` | Header, Optional | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. |
| `user_agent` | `string` | Header, Optional | A string representing the User Agent. Required only when the request is not coming from the end user's browser. |
| `end_user_device_id` | `string` | Header, Optional | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. |
| `end_user_ip` | `string` | Header, Optional | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. |

## Response Type

[`Payer`](/doc/models/payer.md)

## Example Usage

```python
body = CreatePayerRequest()
body.contact = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = payers_controller.create_a_payer(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 404 | Not found | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Retrieve a Payer

Retrieve a Payer

```python
def retrieve_a_payer(self,
                    id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | The ID of the Payer |

## Response Type

[`Payer`](/doc/models/payer.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = payers_controller.retrieve_a_payer(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 404 | Not found | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Update a Payer

Update a Payer

```python
def update_a_payer(self,
                  id,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | The ID of the Payer |
| `body` | [`UpdatePayerRequest`](/doc/models/update-payer-request.md) | Body, Required | Payer to update |

## Response Type

[`Payer`](/doc/models/payer.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'
body = UpdatePayerRequest()

result = payers_controller.update_a_payer(id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 404 | Not found | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Delete a Payer

Delete a Payer

```python
def delete_a_payer(self,
                  id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | The ID of the Payer |

## Response Type

`void`

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = payers_controller.delete_a_payer(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 404 | Not found | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |

