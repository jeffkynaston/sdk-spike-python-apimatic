
# Patch Payment Method Request

## Structure

`PatchPaymentMethodRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type2Enum`](/doc/models/type-2-enum.md) | Required | - |
| `data` | `object` | Required | - |
| `payer` | [`PayerId`](/doc/models/payer-id.md) | Required | - |

## Example (as JSON)

```json
{
  "type": null,
  "data": null,
  "payer": {
    "id": "8f51c396-6e29-49a6-ba5a-1a31d5420158"
  }
}
```

