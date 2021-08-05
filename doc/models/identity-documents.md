
# Identity Documents

This is currently only required if a Payment method from Texas is added.

## Structure

`IdentityDocuments`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type5Enum`](/doc/models/type-5-enum.md) | Required | - |
| `value` | `string` | Required | - |
| `country_of_issuance` | `string` | Optional | Passport country of issuance. Two-letter country code (ISO 3166-1 alpha-2). |

## Example (as JSON)

```json
{
  "type": "US_SSN",
  "value": "123456789"
}
```

