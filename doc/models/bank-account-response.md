
# Bank Account Response

## Structure

`BankAccountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_type` | [`AccountTypeEnum`](/doc/models/account-type-enum.md) | Optional | The type of the bank account |
| `account_holder_name` | `string` | Optional | The legal name of the account holder |
| `created_at` | `string` | Optional | - |
| `account_last_four` | `string` | Optional | Last 4 digits of the account number |
| `routing_number` | `string` | Optional | The routing number of the bank account |
| `billing_address` | [`Address`](/doc/models/address.md) | Optional | - |

## Example (as JSON)

```json
{
  "accountType": null,
  "accountHolderName": null,
  "createdAt": null,
  "accountLastFour": null,
  "routingNumber": null,
  "billingAddress": null
}
```

