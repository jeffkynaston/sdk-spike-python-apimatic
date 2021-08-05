
# Create Payer Request

## Structure

`CreatePayerRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `business_name` | `string` | Optional | - |
| `contact` | `object` | Required | - |
| `business_address` | [`Address`](/doc/models/address.md) | Optional | - |
| `identity_documents` | [`List of IdentityDocuments`](/doc/models/identity-documents.md) | Optional | - |

## Example (as JSON)

```json
{
  "businessName": null,
  "contact": {
    "key1": "val1",
    "key2": "val2"
  },
  "businessAddress": null,
  "identityDocuments": null
}
```

