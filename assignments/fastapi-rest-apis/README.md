# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will build a REST API using the FastAPI framework. You will practice creating endpoints, validating request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create Core API Endpoints

#### Description
Set up a FastAPI app and implement basic CRUD-style endpoints for managing a simple resource called `books`.

#### Requirements
Completed program should:

- Create a FastAPI app instance and run it with Uvicorn.
- Implement `GET /books` to return a list of all books.
- Implement `GET /books/{book_id}` to return one book by id.
- Implement `POST /books` to add a new book to an in-memory list.
- Return JSON responses with clear field names.


### 🛠️ Add Validation And Error Handling

#### Description
Improve your API by validating request bodies and handling invalid input or missing records.

#### Requirements
Completed program should:

- Use a Pydantic model for request body validation.
- Return a `404` response when `book_id` does not exist.
- Return a validation error when required fields are missing.
- Include at least one field type constraint (for example, `year: int`).
- Provide readable response messages for success and errors.
