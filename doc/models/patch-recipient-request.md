
# Patch Recipient Request

## Structure

`PatchRecipientRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `business_name` | `string` | Optional | - |
| `business_address` | [`RecipientAddress`](/doc/models/recipient-address.md) | Optional | - |
| `contact` | [`Contact`](/doc/models/contact.md) | Optional | - |
| `payer` | [`PayerId`](/doc/models/payer-id.md) | Optional | - |

## Example (as JSON)

```json
{
  "businessName": null,
  "businessAddress": null,
  "contact": null,
  "payer": null
}
```

