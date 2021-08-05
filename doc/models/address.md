
# Address

## Structure

`Address`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `line_1` | `string` | Required | Address line 1 (e.g., street, PO Box, or company name). |
| `line_2` | `string` | Optional | Address line 2 (e.g., apartment, suite, unit, or building). |
| `city` | `string` | Required | City, district, suburb, town, or village. |
| `state` | `string` | Required | State, county, province, or region. |
| `postal_code` | `string` | Required | ZIP or postal code. |
| `country` | `string` | Required | Two-letter country code (ISO 3166-1 alpha-2). |

## Example (as JSON)

```json
{
  "line1": "360 9th St.",
  "city": "San Francisco",
  "state": "CA",
  "postalCode": "94103",
  "country": "US"
}
```

