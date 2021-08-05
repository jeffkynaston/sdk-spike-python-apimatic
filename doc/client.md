
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `access_token` | `string` | The OAuth 2.0 Access Token to use for API requests. |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |

The API client can be initialized as follows:

```python
from plastiqpublicapi.plastiqpublicapi_client import PlastiqpublicapiClient
from plastiqpublicapi.configuration import Environment

client = PlastiqpublicapiClient(
    access_token='AccessToken',
    environment=Environment.PRODUCTION,)
```

## Plastiq Public API Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| recipients | Gets RecipientsController |
| categories | Gets CategoriesController |
| client_secrets | Gets ClientSecretsController |
| documents | Gets DocumentsController |
| payers | Gets PayersController |
| payments | Gets PaymentsController |
| payment_methods | Gets PaymentMethodsController |

