
# Card Response

## Structure

`CardResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `last_4` | `string` | Optional | Last 4 digits of card number |
| `brand` | `string` | Optional | - |
| `expiration_month` | `string` | Optional | - |
| `expiration_year` | `string` | Optional | - |
| `created_at` | `string` | Optional | - |
| `billing_address` | [`Address`](/doc/models/address.md) | Optional | - |
| `sub_type` | [`SubTypeEnum`](/doc/models/sub-type-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "last4": null,
  "brand": null,
  "expirationMonth": null,
  "expirationYear": null,
  "createdAt": null,
  "billingAddress": null,
  "subType": null
}
```

