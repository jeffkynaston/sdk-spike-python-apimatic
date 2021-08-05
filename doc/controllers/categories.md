# Categories

```python
categories_controller = client.categories
```

## Class Name

`CategoriesController`


# Retrieve a Paginated List of Categories by Query Parameter S

Retrieve a paginated list of Categories by query parameter(s)

```python
def retrieve_a_paginated_list_of_categories_by_query_parameter_s(self)
```

## Response Type

[`CategoriesResponse`](/doc/models/categories-response.md)

## Example Usage

```python
result = categories_controller.retrieve_a_paginated_list_of_categories_by_query_parameter_s()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorException`](/doc/models/error-exception.md) |
| 401 | Unauthorized | [`ErrorException`](/doc/models/error-exception.md) |
| 403 | Forbidden | [`ErrorException`](/doc/models/error-exception.md) |
| 404 | Not found | [`ErrorException`](/doc/models/error-exception.md) |
| 500 | Internal Server Error | [`ErrorException`](/doc/models/error-exception.md) |

