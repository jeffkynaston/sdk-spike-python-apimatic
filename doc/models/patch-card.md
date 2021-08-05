
# Patch Card

Debit or Credit Card

## Structure

`PatchCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_holder_name` | `string` | Optional | - |
| `cvv` | `string` | Required | 3-4 digits |
| `expiration_month` | `string` | Optional | - |
| `expiration_year` | `string` | Optional | - |
| `billing_address` | [`Address`](/doc/models/address.md) | Optional | - |

## Example (as JSON)

```json
{
  "cvv": "123"
}
```

