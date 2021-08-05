
# Payment

## Structure

`Payment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Optional | - |
| `fees` | [`List of Fee`](/doc/models/fee.md) | Optional | - |
| `source_amount` | [`SourceAmount`](/doc/models/source-amount.md) | Optional | - |
| `target_amount` | [`TargetAmount`](/doc/models/target-amount.md) | Optional | - |
| `payment_method` | [`PaymentMethodId`](/doc/models/payment-method-id.md) | Optional | - |
| `recipient` | [`RecipientId`](/doc/models/recipient-id.md) | Optional | - |
| `payer` | [`PayerId`](/doc/models/payer-id.md) | Optional | - |
| `details` | [`PaymentDetails`](/doc/models/payment-details.md) | Optional | - |
| `delivery_date` | `date` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `status` | [`PaymentStatusEnum`](/doc/models/payment-status-enum.md) | Optional | - |
| `source_descriptor` | `string` | Optional | - |
| `target_descriptor` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "fees": null,
  "sourceAmount": null,
  "targetAmount": null,
  "paymentMethod": null,
  "recipient": null,
  "payer": null,
  "details": null,
  "deliveryDate": null,
  "createdAt": null,
  "status": null,
  "sourceDescriptor": null,
  "targetDescriptor": null
}
```

