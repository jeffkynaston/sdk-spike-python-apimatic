# Recipients

The recipient is the party (usually a business) to whom funds are sent. This is usually a business address or bank account.

```python
recipients_controller = client.recipients
```

## Class Name

`RecipientsController`

## Methods

* [Create a Recipient](/doc/controllers/recipients.md#create-a-recipient)
* [Retrieve a Paginated List of Recipients by Query Parameter S](/doc/controllers/recipients.md#retrieve-a-paginated-list-of-recipients-by-query-parameter-s)
* [Retrieve a Recipient](/doc/controllers/recipients.md#retrieve-a-recipient)
* [Update a Recipient](/doc/controllers/recipients.md#update-a-recipient)
* [Delete a Recipient](/doc/controllers/recipients.md#delete-a-recipient)


# Create a Recipient

Create a Recipient

```python
def create_a_recipient(self,
                      body,
                      trace_id=None,
                      user_agent=None,
                      end_user_device_id=None,
                      end_user_ip=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateRecipientRequest`](/doc/models/create-recipient-request.md) | Body, Required | Recipient to create |
| `trace_id` | `string` | Header, Optional | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. |
| `user_agent` | `string` | Header, Optional | A string representing the User Agent. Required only when the request is not coming from the end user's browser. |
| `end_user_device_id` | `string` | Header, Optional | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. |
| `end_user_ip` | `string` | Header, Optional | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. |

## Response Type

[`Recipient`](/doc/models/recipient.md)

## Example Usage

```python
body = CreateRecipientRequest()
body.business_name = 'Coffee Beans Supply Co.'
body.category_id = 'd7a2beba-0c2c-42de-9690-26f00ba08339'
body.business_address = RecipientAddress()
body.business_address.line_1 = '19439 Stevens Creek Blvd'
body.business_address.country = 'US'
body.contact = Contact()
body.contact.email = 'bobsmith@coffeebean.supply'
body.receiving_method = jsonpickle.decode('{"type":"ACH","accountNumber":"3829473294723","routingNumber":"021000021","beneficiaryName":"Coffee Beans Supply Co."}')

result = recipients_controller.create_a_recipient(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Retrieve a Paginated List of Recipients by Query Parameter S

Retrieve a paginated list of Recipients by query parameter(s)

```python
def retrieve_a_paginated_list_of_recipients_by_query_parameter_s(self,
                                                                payer_id=None,
                                                                offset=None,
                                                                limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payer_id` | `uuid\|string` | Query, Optional | List only Recipients associated with this Payer ID |
| `offset` | `int` | Query, Optional | The number of records you wish to skip before selecting records |
| `limit` | `int` | Query, Optional | Number of items to return |

## Response Type

[`RecipientsResponse`](/doc/models/recipients-response.md)

## Example Usage

```python
result = recipients_controller.retrieve_a_paginated_list_of_recipients_by_query_parameter_s()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 404 | Not found | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Retrieve a Recipient

Retrieve a Recipient

```python
def retrieve_a_recipient(self,
                        id,
                        payer_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | The ID of the Recipient |
| `payer_id` | `uuid\|string` | Query, Optional | The ID of the Payer the Recipient is scoped to |

## Response Type

[`Recipient`](/doc/models/recipient.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = recipients_controller.retrieve_a_recipient(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 404 | Not found | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Update a Recipient

Update a Recipient

```python
def update_a_recipient(self,
                      id,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | The ID of the Recipient |
| `body` | [`PatchRecipientRequest`](/doc/models/patch-recipient-request.md) | Body, Required | Recipient to create |

## Response Type

[`Recipient`](/doc/models/recipient.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'
body = PatchRecipientRequest()

result = recipients_controller.update_a_recipient(id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 404 | Not found | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |


# Delete a Recipient

Delete a Recipient

```python
def delete_a_recipient(self,
                      id,
                      payer_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | The ID of the Recipient |
| `payer_id` | `uuid\|string` | Query, Optional | The ID of the Payer the Recipient is scoped to |

## Response Type

`void`

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'

result = recipients_controller.delete_a_recipient(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 404 | Not found | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |

