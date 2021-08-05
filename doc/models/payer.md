
# Payer

## Structure

`Payer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Optional | - |
| `business_name` | `string` | Optional | - |
| `contact` | `object` | Optional | - |
| `business_address` | [`Address`](/doc/models/address.md) | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `status` | [`StatusEnum`](/doc/models/status-enum.md) | Optional | - |
| `identity_documents` | [`List of IdentityDocumentResponse`](/doc/models/identity-document-response.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "businessName": null,
  "contact": null,
  "businessAddress": null,
  "createdAt": null,
  "status": null,
  "identityDocuments": null
}
```

