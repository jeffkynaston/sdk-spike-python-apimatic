
# Patch Payment Intent Request Payload

## Structure

`PatchPaymentIntentRequestPayload`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `target_amount` | [`AmountDetails`](/doc/models/amount-details.md) | Optional | - |
| `details` | [`PaymentDetails`](/doc/models/payment-details.md) | Optional | - |
| `metadata` | `object` | Optional | additional payment information to support operational requirements |

## Example (as JSON)

```json
{
  "targetAmount": null,
  "details": null,
  "metadata": null
}
```

