
# Payment Method

## Structure

`PaymentMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Optional | - |
| `mtype` | [`Type2Enum`](/doc/models/type-2-enum.md) | Optional | - |
| `data` | `object` | Optional | - |
| `status` | [`PaymentMethodStatusEnum`](/doc/models/payment-method-status-enum.md) | Optional | - |
| `status_reasons` | [`List of StatusReason`](/doc/models/status-reason.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "type": null,
  "data": null,
  "status": null,
  "statusReasons": null
}
```

