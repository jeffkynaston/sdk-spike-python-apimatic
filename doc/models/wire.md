
# Wire

## Structure

`Wire`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `string` | Required | **Default**: `'WIRE'`<br>*Default: `'WIRE'`* |
| `account_number` | `string` | Required | Bank wire account number (alphanumeric)<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `35` |
| `routing_number` | `string` | Required | Bank wire routing number<br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `11` |
| `beneficiary_name` | `string` | Required | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `35` |
| `country` | `string` | Required | Two-letter country code (ISO 3166-1 alpha-2).<br>**Default**: `'US'`<br>*Default: `'US'`* |

## Example (as JSON)

```json
{
  "type": "WIRE",
  "accountNumber": "3829473294723",
  "routingNumber": "021000021",
  "beneficiaryName": "Coffee Beans Supply Co.",
  "country": "US"
}
```

