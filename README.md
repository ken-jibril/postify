# Blogify API - Blogging Platform

A RESTful API for a blogging platform built with Django and Django REST Framework.

## 🚀 Live API

**Base URL:** `https://ken254.pythonanywhere.com/api/`

---

## 📋 Features

- ✅ User Registration & Authentication (Token-based)
- ✅ Blog Post CRUD (Create, Read, Update, Delete)
- ✅ Category Management
- ✅ Tag Management
- ✅ Search Posts (by title, content, author, tags, category)
- ✅ Filter Posts (by category, author, published date, tags)
- ✅ Sort Posts (by published date, created date)
- ✅ Pagination (5 posts per page)
- ✅ Permission System (only authors can edit/delete their posts)

---

## 🔐 Authentication

This API uses **Token Authentication**. To perform authenticated actions (create, update, delete posts), you must:

1. **Register a user** at `/api/users/` (POST)
2. **Login** to get a token at `/api/auth/token/login/` (POST)
3. **Include the token** in the `Authorization` header:
   ```
   Authorization: Token YOUR_TOKEN_HERE
   ```

---

## 📖 API Endpoints

### Users

| Method | Endpoint           | Description       | Auth Required |
| ------ | ------------------ | ----------------- | ------------- |
| GET    | `/api/users/`      | List all users    | No            |
| POST   | `/api/users/`      | Register new user | No            |
| GET    | `/api/users/{id}/` | Get user details  | No            |
| PUT    | `/api/users/{id}/` | Update user       | Yes           |
| DELETE | `/api/users/{id}/` | Delete user       | Yes           |

### Posts

| Method | Endpoint                             | Description                | Auth Required    |
| ------ | ------------------------------------ | -------------------------- | ---------------- |
| GET    | `/api/posts/`                        | List all posts (paginated) | No               |
| POST   | `/api/posts/`                        | Create new post            | Yes              |
| GET    | `/api/posts/{id}/`                   | Get post details           | No               |
| PUT    | `/api/posts/{id}/`                   | Update post                | Yes (Owner only) |
| DELETE | `/api/posts/{id}/`                   | Delete post                | Yes (Owner only) |
| GET    | `/api/posts/by_category/?category=1` | Filter by category         | No               |
| GET    | `/api/posts/by_author/?author=1`     | Filter by author           | No               |

### Categories

| Method | Endpoint                | Description          | Auth Required |
| ------ | ----------------------- | -------------------- | ------------- |
| GET    | `/api/categories/`      | List all categories  | No            |
| POST   | `/api/categories/`      | Create category      | Yes           |
| GET    | `/api/categories/{id}/` | Get category details | No            |
| PUT    | `/api/categories/{id}/` | Update category      | Yes           |
| DELETE | `/api/categories/{id}/` | Delete category      | Yes           |

### Tags

| Method | Endpoint          | Description     | Auth Required |
| ------ | ----------------- | --------------- | ------------- |
| GET    | `/api/tags/`      | List all tags   | No            |
| POST   | `/api/tags/`      | Create tag      | Yes           |
| GET    | `/api/tags/{id}/` | Get tag details | No            |
| PUT    | `/api/tags/{id}/` | Update tag      | Yes           |
| DELETE | `/api/tags/{id}/` | Delete tag      | Yes           |

---

## 🔍 Search & Filter Examples

### Search Posts

```
GET /api/posts/?search=python
GET /api/posts/?search=django&search=tutorial
```

### Filter by Category

```
GET /api/posts/?category=1
```

### Filter by Author

```
GET /api/posts/?author=1
```

### Filter by Tags

```
GET /api/posts/?tags=1
GET /api/posts/?tags=1&tags=2
```

### Sort Posts

```
GET /api/posts/?ordering=published_date
GET /api/posts/?ordering=-published_date  (newest first)
GET /api/posts/?ordering=created_date
```

### Pagination

```
GET /api/posts/?page=1
GET /api/posts/?page=2
```

---

## 📝 Request/Response Examples

### Register User (POST /api/users/)

```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

### Login (POST /api/auth/token/login/)

```json
{
  "username": "johndoe",
  "password": "securepassword123"
}
```

**Response:**

```json
{
  "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### Create Post (POST /api/posts/)

```json
{
  "title": "My First Blog Post",
  "content": "This is the content of my first blog post...",
  "category": 1,
  "tags": [1, 2],
  "published_date": "2024-01-15T10:30:00Z"
}
```

### Get Posts List (GET /api/posts/)

```json
{
  "count": 10,
  "next": "https://ken254.pythonanywhere.com/api/posts/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "My First Blog Post",
      "content": "This is the content...",
      "author": "johndoe",
      "category": 1,
      "tags": [1, 2],
      "published_date": "2024-01-15T10:30:00Z",
      "created_date": "2024-01-15T10:00:00Z"
    }
  ]
}
```

---

## ⚠️ Error Codes

| Code | Description                             |
| ---- | --------------------------------------- |
| 400  | Bad Request - Invalid input             |
| 401  | Unauthorized - Invalid or missing token |
| 403  | Forbidden - You don't have permission   |
| 404  | Not Found - Resource doesn't exist      |

---

## 🛠️ Setup Local Development

```bash
# Clone the repository
git clone <repo-url>
cd postify

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
# source venv/bin/activate    # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

API will be available at `http://127.0.0.1:8000/api/`

---

## 📦 Tech Stack

- **Backend:** Django 6.0
- **API Framework:** Django REST Framework
- **Database:** SQLite (default)
- **Authentication:** Token Authentication

---

## 📄 License

This project is for educational purposes.

## Author
```
Built by Ken
```
