
# Create Document Upload Request

## Structure

`CreateDocumentUploadRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payer` | [`PayerId`](/doc/models/payer-id.md) | Required | - |
| `mtype` | `string` | Required | **Default**: `'INVOICE'`<br>*Default: `'INVOICE'`* |
| `file_type` | [`FileTypeEnum`](/doc/models/file-type-enum.md) | Required | - |
| `filename` | `string` | Required | - |

## Example (as JSON)

```json
{
  "payer": {
    "id": "8f51c396-6e29-49a6-ba5a-1a31d5420158"
  },
  "type": "INVOICE",
  "fileType": null,
  "filename": "invoice_123.pdf"
}
```

