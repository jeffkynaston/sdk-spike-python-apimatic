
# EFT

## Structure

`EFT`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `string` | Required | **Default**: `'EFT'`<br>*Default: `'EFT'`* |
| `account_number` | `string` | Required | Bank EFT account number |
| `routing_number` | `string` | Required | 8 digit routing number<br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `8` |
| `beneficiary_name` | `string` | Required | **Constraints**: *Minimum Length*: `1`, *Maximum Length*: `35` |

## Example (as JSON)

```json
{
  "type": "EFT",
  "accountNumber": "3864328462",
  "routingNumber": "00301094",
  "beneficiaryName": "Coffee Beans Supply Co."
}
```

