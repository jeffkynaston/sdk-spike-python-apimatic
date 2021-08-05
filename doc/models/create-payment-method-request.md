
# Create Payment Method Request

## Structure

`CreatePaymentMethodRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type2Enum`](/doc/models/type-2-enum.md) | Required | - |
| `data` | `object` | Optional | - |
| `payer` | [`PayerId`](/doc/models/payer-id.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "CARD",
  "data": null,
  "payer": null
}
```

