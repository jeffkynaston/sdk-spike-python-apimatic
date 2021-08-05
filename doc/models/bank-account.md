
# Bank Account

Bank Account Funded

## Structure

`BankAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_name` | `string` | Required | The legal name of the account holder |
| `account_number` | `string` | Required | The account number of the bank account |
| `account_type` | [`AccountTypeEnum`](/doc/models/account-type-enum.md) | Optional | The type of the bank account |
| `routing_number` | `string` | Required | The routing number of the bank account |
| `billing_address` | [`Address`](/doc/models/address.md) | Required | - |

## Example (as JSON)

```json
{
  "accountHolderName": "Jane Payer",
  "accountNumber": "41541433888",
  "routingNumber": "211371120",
  "billingAddress": {
    "line1": "360 9th St.",
    "city": "San Francisco",
    "state": "CA",
    "postalCode": "94103",
    "country": "US"
  }
}
```

