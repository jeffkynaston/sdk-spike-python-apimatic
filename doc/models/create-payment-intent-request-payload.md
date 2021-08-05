
# Create Payment Intent Request Payload

## Structure

`CreatePaymentIntentRequestPayload`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `target_amount` | [`AmountDetails`](/doc/models/amount-details.md) | Optional | - |
| `payment_method` | [`PaymentMethodId`](/doc/models/payment-method-id.md) | Required | - |
| `recipient` | `object` | Required | - |
| `payer` | [`PayerId`](/doc/models/payer-id.md) | Required | - |
| `details` | [`PaymentDetails`](/doc/models/payment-details.md) | Optional | - |
| `metadata` | `object` | Optional | additional payment information to support operational requirements |

## Example (as JSON)

```json
{
  "paymentMethod": {
    "id": "6f0eb884-3f41-4b57-b86a-80f62dca011e"
  },
  "recipient": null,
  "payer": {
    "id": "8f51c396-6e29-49a6-ba5a-1a31d5420158"
  }
}
```

