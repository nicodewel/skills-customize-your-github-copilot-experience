# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a simple REST API using the FastAPI framework to manage a collection of items, practice routing, and return JSON data in a clean and structured way.

## 📝 Tasks

### 🛠️ Build the API foundation

#### Description
Set up a FastAPI application that serves as a basic API for managing items. The app should have endpoints for reading and creating records using HTTP methods and response data in JSON format.

#### Requirements
Completed program should:

- Create a FastAPI app with a meaningful application title
- Define at least one GET endpoint that returns a list of items
- Define at least one POST endpoint that accepts item data
- Return JSON responses in a clear, consistent structure
- Use Pydantic models to validate incoming request data

### 🛠️ Add item management logic

#### Description
Extend your API so it can store and retrieve simple item records, such as task names or product entries. Include basic validation and clear handling for created items.

#### Requirements
Completed program should:

- Store items in an in-memory list or dictionary
- Assign a unique ID to each new item
- Accept item fields such as name and optional status
- Return the newly created item after successful submission
- Keep the API simple, readable, and easy to test locally with FastAPI
