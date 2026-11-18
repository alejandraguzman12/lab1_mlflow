# adidas-nike-model @ challenger

- URI: `models:/adidas-nike-model@challenger`
- Versión: 2
- Endpoint: `POST http://127.0.0.1:5001/invocations`

## Esquema de entrada

```json
[
  {
    "type": "double",
    "name": "Listing Price",
    "required": true
  },
  {
    "type": "long",
    "name": "Brand",
    "required": true
  },
  {
    "type": "double",
    "name": "Rating",
    "required": true
  },
  {
    "type": "double",
    "name": "Reviews",
    "required": true
  }
]
```

## Esquema de salida

```json
[
  {
    "type": "double",
    "required": true
  }
]
```

## Petición

```bash
curl http://127.0.0.1:5001/invocations \
  -H 'Content-Type: application/json' \
  -d '{"dataframe_split": {"columns": ["Listing Price", "Brand", "Rating", "Reviews"], "data": [[-0.5460848583844848, 1.0, -1.0881601104517644, 0.738138425178467]]}}'
```

```json
{
  "dataframe_split": {
    "columns": [
      "Listing Price",
      "Brand",
      "Rating",
      "Reviews"
    ],
    "data": [
      [
        -0.5460848583844848,
        1.0,
        -1.0881601104517644,
        0.738138425178467
      ]
    ]
  }
}
```

## Respuesta

```json
{
  "predictions": [
    3447.4
  ]
}
```
