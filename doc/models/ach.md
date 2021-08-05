
# ACH

## Structure

`ACH`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `string` | Required | **Default**: `'ACH'`<br>*Default: `'ACH'`* |
| `account_number` | `string` | Required | Bank ACH account number |
| `routing_number` | `string` | Required | 9 digit bank routing number<br>**Constraints**: *Minimum Length*: `9`, *Maximum Length*: `9` |
| `beneficiary_name` | `string` | Required | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `35` |

## Example (as JSON)

```json
{
  "type": "ACH",
  "accountNumber": "3829473294723",
  "routingNumber": "021000021",
  "beneficiaryName": "Coffee Beans Supply Co."
}
```

