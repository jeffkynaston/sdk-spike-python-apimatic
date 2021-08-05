
# Client Secrets Request

## Structure

`ClientSecretsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payer` | [`PayerId`](/doc/models/payer-id.md) | Optional | - |
| `mtype` | [`Type7Enum`](/doc/models/type-7-enum.md) | Optional | The type of object to create the Client Secret for. Defaults to CARD. |

## Example (as JSON)

```json
{
  "payer": null,
  "type": null
}
```

