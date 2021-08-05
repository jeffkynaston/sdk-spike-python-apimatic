
# Recipient

## Structure

`Recipient`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Optional | - |
| `business_name` | `string` | Optional | - |
| `category_id` | `uuid\|string` | Optional | - |
| `business_address` | [`RecipientAddress`](/doc/models/recipient-address.md) | Optional | - |
| `contact` | [`Contact1`](/doc/models/contact-1.md) | Optional | - |
| `receiving_method` | `object` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `status` | [`StatusEnum`](/doc/models/status-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "businessName": null,
  "categoryId": null,
  "businessAddress": null,
  "contact": null,
  "receivingMethod": null,
  "createdAt": null,
  "status": null
}
```

