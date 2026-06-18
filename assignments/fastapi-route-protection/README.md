# 📘 Assignment: FastAPI Route Protection with API Keys

## 🎯 Objective

In this assignment, you will secure a FastAPI application using API keys and simple role checks. You will practice protecting routes, validating request headers, and returning clear HTTP error responses.

## 📝 Tasks

### 🛠️ Implement API Key Authentication

#### Description
Add API key verification to your FastAPI app so only requests with a valid key can access protected endpoints.

#### Requirements
Completed program should:

- Read an API key from the `x-api-key` request header.
- Compare the key against allowed keys stored in the application.
- Protect at least two routes so unauthenticated requests are blocked.
- Return `401 Unauthorized` when the API key is missing or invalid.
- Keep one public route (for example, `GET /health`) that does not require authentication.


### 🛠️ Add Role-Based Access Rules

#### Description
Extend your authentication logic so different keys have different permissions, and only admin keys can access admin endpoints.

#### Requirements
Completed program should:

- Define at least two roles, such as `student` and `admin`.
- Create one admin-only endpoint (for example, deleting or resetting data).
- Return `403 Forbidden` when a valid key does not have permission.
- Return consistent JSON error responses with a readable `detail` message.
- Demonstrate role behavior with at least one example key for each role.
