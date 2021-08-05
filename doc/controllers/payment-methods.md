# Payment Methods

```python
payment_methods_controller = client.payment_methods
```

## Class Name

`PaymentMethodsController`

## Methods

* [Create a Payment Method](/doc/controllers/payment-methods.md#create-a-payment-method)
* [Retrieve a Paginated List of Payment Methods by Query Parameter S](/doc/controllers/payment-methods.md#retrieve-a-paginated-list-of-payment-methods-by-query-parameter-s)
* [Retrieve a Payment Method](/doc/controllers/payment-methods.md#retrieve-a-payment-method)
* [Delete a Payment Method](/doc/controllers/payment-methods.md#delete-a-payment-method)
* [Update a Payment Method](/doc/controllers/payment-methods.md#update-a-payment-method)


# Create a Payment Method

Create a Payment Method

```python
def create_a_payment_method(self,
                           body,
                           trace_id=None,
                           user_agent=None,
                           end_user_device_id=None,
                           end_user_ip=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreatePaymentMethodRequest`](/doc/models/create-payment-method-request.md) | Body, Required | Payment Method to create |
| `trace_id` | `string` | Header, Optional | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. |
| `user_agent` | `string` | Header, Optional | A string representing the User Agent. Required only when the request is not coming from the end user's browser. |
| `end_user_device_id` | `string` | Header, Optional | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. |
| `end_user_ip` | `string` | Header, Optional | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. |

## Response Type

[`PaymentMethod`](/doc/models/payment-method.md)

## Example Usage

```python
body = CreatePaymentMethodRequest()
body.mtype = Type2Enum.CARD

result = payment_methods_controller.create_a_payment_method(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Retrieve a Paginated List of Payment Methods by Query Parameter S

Retrieve a paginated list of Payment Methods by query parameter(s)

```python
def retrieve_a_paginated_list_of_payment_methods_by_query_parameter_s(self,
                                                                     payer_id,
                                                                     offset=None,
                                                                     limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payer_id` | `uuid\|string` | Query, Required | The associated Payer ID to list Payment Methods for |
| `offset` | `int` | Query, Optional | The number of records you wish to skip before selecting records |
| `limit` | `int` | Query, Optional | Number of items to return |

## Response Type

[`PaymentMethodsResponse`](/doc/models/payment-methods-response.md)

## Example Usage

```python
payer_id = '0000192e-0000-0000-0000-000000000000'

result = payment_methods_controller.retrieve_a_paginated_list_of_payment_methods_by_query_parameter_s(payer_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 404 | Not found | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Retrieve a Payment Method

Retrieve a Payment Method

```python
def retrieve_a_payment_method(self,
                             payer_id,
                             id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payer_id` | `uuid\|string` | Query, Required | The Payer ID associated to the Payment Method |
| `id` | `uuid\|string` | Template, Required | The ID of the Payment Method |

## Response Type

[`PaymentMethod`](/doc/models/payment-method.md)

## Example Usage

```python
payer_id = '0000192e-0000-0000-0000-000000000000'
id = '00001770-0000-0000-0000-000000000000'

result = payment_methods_controller.retrieve_a_payment_method(payer_id, id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 404 | Not found | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Delete a Payment Method

Delete a Payment Method

```python
def delete_a_payment_method(self,
                           id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | The ID of the Payment Method |

## Response Type

`void`

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = payment_methods_controller.delete_a_payment_method(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 404 | Not found | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Update a Payment Method

Update a Payment Method

```python
def update_a_payment_method(self,
                           id,
                           body,
                           trace_id=None,
                           user_agent=None,
                           end_user_device_id=None,
                           end_user_ip=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | The ID of the Payment Method |
| `body` | [`PatchPaymentMethodRequest`](/doc/models/patch-payment-method-request.md) | Body, Required | Payment Method to update |
| `trace_id` | `string` | Header, Optional | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. |
| `user_agent` | `string` | Header, Optional | A string representing the User Agent. Required only when the request is not coming from the end user's browser. |
| `end_user_device_id` | `string` | Header, Optional | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. |
| `end_user_ip` | `string` | Header, Optional | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. |

## Response Type

[`PaymentMethod`](/doc/models/payment-method.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'
body = PatchPaymentMethodRequest()
body.mtype = Type2Enum.CARD
body.data = jsonpickle.decode('{"key1":"val1","key2":"val2"}')
body.payer = PayerId()
body.payer.id = '8f51c396-6e29-49a6-ba5a-1a31d5420158'

result = payment_methods_controller.update_a_payment_method(id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |

