
# Card

Debit or Credit Card

## Structure

`Card`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_holder_name` | `string` | Required | - |
| `account_number` | `string` | Required | Card number. |
| `cvv` | `string` | Required | 3-4 digits |
| `expiration_month` | `string` | Required | - |
| `expiration_year` | `string` | Required | - |
| `billing_address` | [`Address`](/doc/models/address.md) | Required | - |

## Example (as JSON)

```json
{
  "cardHolderName": "Jen Doe",
  "accountNumber": "4242424242424242",
  "cvv": "123",
  "expirationMonth": "01",
  "expirationYear": "2021",
  "billingAddress": {
    "line1": "360 9th St.",
    "city": "San Francisco",
    "state": "CA",
    "postalCode": "94103",
    "country": "US"
  }
}
```

