
# 🛠️ API Documentation

This document contains the API endpoints for **Product**, **Order**, and **Recommendation** management.

---

## 📦 Product APIs

### 🔹 `POST /insert_product/`
Insert a new product into the database.

**Request Body**
```json
[{
  "name": "Air City",
  "description": "Particularly friend lead community gas remember set. Make no idea television decision well hundred. Especially administration together.",
  "price": "595.79"
}]
```
**Response Body**
```json
{
  "message": [
    {
      "id": 106,
      "name": "Air City",
      "description": "Particularly friend lead community gas remember set. Make no idea television decision well hundred. Especially administration together.",
      "price": "599.79",
      "created_at": "2025-05-16T07:06:15.863465Z",
      "updated_at": "2025-05-16T07:06:15.863465Z"
    }
  ]
}
```
### 📦 `GET /get_product/` or `GET /get_product/<int:id>/`

**Description:**  
Retrieve all products or a specific product by its ID from the database.

---

#### 🧾 Request

- **Method:** `GET`
- **URL Parameters (optional):**
  - `<int:id>` – The ID of the product to retrieve
- **Request Body:** `None`

---

#### ✅ Example Request

```http
GET /get_product/
```

```http
GET /get_product/56
```

---

#### 📤 Sample Response

```json
[
  {
    "id": 56,
    "name": "Something Finish",
    "description": "Fear much spend market. Important west feel wait whatever magazine keep. Where term hand make.",
    "price": "745.20",
    "created_at": "2025-05-15T05:15:38.542549Z",
    "updated_at": "2025-05-15T05:15:38.542549Z"
  },
  {
    "id": 57,
    "name": "Tv Value",
    "description": "Me president west could yourself bit rate beyond. Sit top learn either pattern thousand politics. Senior fill father class.",
    "price": "470.97",
    "created_at": "2025-05-15T05:15:38.549205Z",
    "updated_at": "2025-05-15T05:15:38.549205Z"
  }
]
```
### ✏️ `PUT /update_product/<int:id>/`

**Description:**  
Update the details of an existing product in the database by its ID.

---

#### 🧾 Request

- **Method:** `PUT`
- **URL Parameters:**
  - `<int:id>` – The ID of the product to update
- **Request Body:**

```json
{
  "name": "Something Finish Also",
  "description": "Fear much spend market. Important west feel wait whatever magazine keep. Where term hand make.",
  "price": "745.20"
}
```

---

#### ✅ Example Request

```http
PUT /update_product/56
```

---

#### 📤 Sample Response

```json
{
  "message": {
    "id": 56,
    "name": "Something Finish Also",
    "description": "Fear much spend market. Important west feel wait whatever magazine keep. Where term hand make.",
    "price": "745.20",
    "created_at": "2025-05-15T05:15:38.542549Z",
    "updated_at": "2025-05-16T07:11:45.069116Z"
  }
}
```
### 🗑️ `DELETE /delete_product/<int:id>/`

**Description:**  
Delete a specific product from the database using its ID.

---

#### 🧾 Request

- **Method:** `DELETE`
- **URL Parameters:**
  - `<int:id>` – The ID of the product to delete
- **Request Body:** `None`

---

#### ✅ Example Request

```http
DELETE /delete_product/56
```

---

#### 📤 Sample Response

```json
{
  "message": "Product deleted successfully"
}
```
---
## 🛒 Order APIs

### ➕ `POST /insert_order/`

**Description:**  
Insert a new order into the database.

---

#### 🧾 Request

- **Method:** `POST`
- **Request Body:**

```json
[
  {
    "products": [
      61,
      74
    ]
  }
]
```

> 💡 *Product IDs in the `products` array refer to existing product entries.*

---

#### 📤 Sample Response

```json
{
  "message": [
    {
      "id": 64,
      "total_price": "1005.08",
      "created_at": "2025-05-16T07:29:58.027280Z",
      "products": [
        61,
        74
      ]
    }
  ]
}
```

---

### 📦 `GET /get_order/` OR `GET /get_order/<int:id>/`

**Description:**  
Retrieve all orders or a specific order by ID.

---

#### 🧾 Request

- **Method:** `GET`
- **Request Body:** `None`

---

#### ✅ Example Requests

```http
GET /get_order/
GET /get_order/10
```

---

#### 📤 Sample Response

```json
[
  {
    "id": 9,
    "total_price": "470.97",
    "created_at": "2025-05-16T04:07:12.427535Z",
    "products": [57]
  },
  {
    "id": 10,
    "total_price": "832.35",
    "created_at": "2025-05-16T04:07:12.447977Z",
    "products": [64, 74, 78, 102]
  }
]
```

---

### ✏️ `PUT /update_order/<int:id>/`

**Description:**  
Update the list of products in an existing order by ID.

---

#### 🧾 Request

- **Method:** `PUT`
- **URL Parameters:**  
  `<int:id>` – ID of the order to update
- **Request Body:**

```json
{
  "products": [57, 64]
}
```

---

#### 📤 Sample Response

```json
{
  "message": {
    "id": 9,
    "total_price": "1066.76",
    "created_at": "2025-05-16T04:07:12.427535Z",
    "products": [57, 64]
  }
}
```

---

### 🗑️ `DELETE /delete_product/<int:id>/`

**Description:**  
Delete an order from the database by its ID.

---

#### 🧾 Request

- **Method:** `DELETE`
- **Request Body:** `None`

---

#### ✅ Example Request

```http
DELETE /delete_product/9
```

---

#### 📤 Sample Response

```json
{
  "message": "Order deleted successfully"
}
```

## 🎯 Recommendation API

---

### 💡 `GET /recommend_products/<int:id>`

**Description:**  
Get top 3 product recommendations based on past orders of the given product ID.

---

#### 🧾 Request

- **Method:** `GET`
- **URL Parameter:**  
  `<int:id>` – ID of the product to base recommendations on
- **Request Body:** `None`

---

#### ✅ Example Request

```http
GET /recommend_products/56
```

---

#### 📤 Sample Response

```json
{
  "recommendations": [
    {
      "product_id": 59,
      "count": 3
    },
    {
      "product_id": 74,
      "count": 2
    },
    {
      "product_id": 78,
      "count": 2
    }
  ]
}
```

> 🔎 *Each item in the response includes the recommended `product_id` and how many times it was ordered together (`count`).*

