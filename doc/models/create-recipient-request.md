
# Create Recipient Request

## Structure

`CreateRecipientRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `business_name` | `string` | Required | - |
| `category_id` | `uuid\|string` | Required | - |
| `business_address` | [`RecipientAddress`](/doc/models/recipient-address.md) | Required | - |
| `contact` | [`Contact`](/doc/models/contact.md) | Required | - |
| `receiving_method` | `object` | Required | - |
| `payer` | [`PayerId`](/doc/models/payer-id.md) | Optional | - |

## Example (as JSON)

```json
{
  "businessName": "Coffee Beans Supply Co.",
  "categoryId": "d7a2beba-0c2c-42de-9690-26f00ba08339",
  "businessAddress": {
    "line1": "19439 Stevens Creek Blvd",
    "country": "US"
  },
  "contact": {
    "email": "bobsmith@coffeebean.supply"
  },
  "receivingMethod": {
    "type": "ACH",
    "accountNumber": "3829473294723",
    "routingNumber": "021000021",
    "beneficiaryName": "Coffee Beans Supply Co."
  }
}
```

