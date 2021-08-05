# Payments

```python
payments_controller = client.payments
```

## Class Name

`PaymentsController`

## Methods

* [Create a Payment From a Payment Intent](/doc/controllers/payments.md#create-a-payment-from-a-payment-intent)
* [Retrieve a Paginated List of Payments by Query Parameter S](/doc/controllers/payments.md#retrieve-a-paginated-list-of-payments-by-query-parameter-s)
* [Retrieve a Single Payment](/doc/controllers/payments.md#retrieve-a-single-payment)
* [Refund or Cancel an Existing Payment](/doc/controllers/payments.md#refund-or-cancel-an-existing-payment)
* [Create a Payment Intent](/doc/controllers/payments.md#create-a-payment-intent)
* [Retrieve a Single Payment Intent](/doc/controllers/payments.md#retrieve-a-single-payment-intent)
* [Update a Payment Intent](/doc/controllers/payments.md#update-a-payment-intent)


# Create a Payment From a Payment Intent

Create a Payment from a Payment Intent

```python
def create_a_payment_from_a_payment_intent(self,
                                          body,
                                          trace_id=None,
                                          user_agent=None,
                                          end_user_device_id=None,
                                          end_user_ip=None,
                                          idempotency_key=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `object` | Body, Required | Payment to create |
| `trace_id` | `string` | Header, Optional | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. |
| `user_agent` | `string` | Header, Optional | A string representing the User Agent. Required only when the request is not coming from the end user's browser. |
| `end_user_device_id` | `string` | Header, Optional | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. |
| `end_user_ip` | `string` | Header, Optional | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. |
| `idempotency_key` | `string` | Header, Optional | A valid UUID (V4) for handling duplicate requests. Will return original status code, response body, and set a 'Idempotent-Replay' header on response for a given key if a match exists. |

## Response Type

[`Payment`](/doc/models/payment.md)

## Example Usage

```python
body = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = payments_controller.create_a_payment_from_a_payment_intent(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Retrieve a Paginated List of Payments by Query Parameter S

Retrieve a paginated list of payments by query parameter(s)

```python
def retrieve_a_paginated_list_of_payments_by_query_parameter_s(self,
                                                              payer_id,
                                                              offset=None,
                                                              limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payer_id` | `uuid\|string` | Query, Required | The associated Payer ID to list payments for |
| `offset` | `int` | Query, Optional | The number of records you wish to skip before selecting records |
| `limit` | `int` | Query, Optional | Number of items to return |

## Response Type

[`PaymentsResponse`](/doc/models/payments-response.md)

## Example Usage

```python
payer_id = '0000192e-0000-0000-0000-000000000000'

result = payments_controller.retrieve_a_paginated_list_of_payments_by_query_parameter_s(payer_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 404 | Not found | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Retrieve a Single Payment

Retrieve a single Payment

```python
def retrieve_a_single_payment(self,
                             payer_id,
                             id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payer_id` | `uuid\|string` | Query, Required | The Payer ID associated with the Payment |
| `id` | `uuid\|string` | Template, Required | The ID of the Payment |

## Response Type

[`Payment`](/doc/models/payment.md)

## Example Usage

```python
payer_id = '0000192e-0000-0000-0000-000000000000'
id = '00001770-0000-0000-0000-000000000000'

result = payments_controller.retrieve_a_single_payment(payer_id, id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 404 | Not found | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Refund or Cancel an Existing Payment

Refund or cancel an existing Payment

```python
def refund_or_cancel_an_existing_payment(self,
                                        id,
                                        body,
                                        trace_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | The ID of the Payment to refund |
| `body` | [`PaymentRefundRequest`](/doc/models/payment-refund-request.md) | Body, Required | Payment Refund body |
| `trace_id` | `string` | Header, Optional | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. |

## Response Type

[`PaymentRefund`](/doc/models/payment-refund.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'
body = PaymentRefundRequest()

result = payments_controller.refund_or_cancel_an_existing_payment(id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Create a Payment Intent

Create a Payment Intent

```python
def create_a_payment_intent(self,
                           body,
                           trace_id=None,
                           user_agent=None,
                           end_user_device_id=None,
                           end_user_ip=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreatePaymentIntentRequestPayload`](/doc/models/create-payment-intent-request-payload.md) | Body, Required | Create a Payment Intent object staging it for execution |
| `trace_id` | `string` | Header, Optional | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. |
| `user_agent` | `string` | Header, Optional | A string representing the User Agent. Required only when the request is not coming from the end user's browser. |
| `end_user_device_id` | `string` | Header, Optional | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. |
| `end_user_ip` | `string` | Header, Optional | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. |

## Response Type

[`PaymentIntent`](/doc/models/payment-intent.md)

## Example Usage

```python
body = CreatePaymentIntentRequestPayload()
body.payment_method = PaymentMethodId()
body.payment_method.id = '6f0eb884-3f41-4b57-b86a-80f62dca011e'
body.recipient = jsonpickle.decode('{"key1":"val1","key2":"val2"}')
body.payer = PayerId()
body.payer.id = '8f51c396-6e29-49a6-ba5a-1a31d5420158'

result = payments_controller.create_a_payment_intent(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Retrieve a Single Payment Intent

Retrieve a single Payment Intent

```python
def retrieve_a_single_payment_intent(self,
                                    payer_id,
                                    id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payer_id` | `uuid\|string` | Query, Required | The Payer ID of the Payment Intent |
| `id` | `uuid\|string` | Template, Required | The ID of the Payment Intent |

## Response Type

[`PaymentIntent`](/doc/models/payment-intent.md)

## Example Usage

```python
payer_id = '0000192e-0000-0000-0000-000000000000'
id = '00001770-0000-0000-0000-000000000000'

result = payments_controller.retrieve_a_single_payment_intent(payer_id, id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 404 | Not found | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Update a Payment Intent

Update a Payment Intent

```python
def update_a_payment_intent(self,
                           id,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | The ID of the Payment Intent |
| `body` | [`PatchPaymentIntentRequestPayload`](/doc/models/patch-payment-intent-request-payload.md) | Body, Required | Payment Intent to update |

## Response Type

[`PaymentIntent`](/doc/models/payment-intent.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'
body = PatchPaymentIntentRequestPayload()

result = payments_controller.update_a_payment_intent(id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |

