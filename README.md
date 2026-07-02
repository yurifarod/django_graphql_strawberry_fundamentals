# Django GraphQL Strawberry Query Fundamentals

Udemy course "Django GraphQL Strawberry Query Fundamentals" available in ["Udemy Web"](https://www.udemy.com/course/python-django-graphql-strawberry-fundamentals)

A simple educational project demonstrating how to build GraphQL APIs with **Django** and **Strawberry GraphQL**. The goal is to introduce the core concepts of GraphQL while following Django best practices. Strawberry uses Python type annotations and dataclasses to create a clean and type-safe GraphQL schema. :contentReference[oaicite:0]{index=0}

## Topics Covered

- Project structure
- Strawberry GraphQL setup
- GraphQL schema creation
- Queries
- Mutations
- Input types
- Custom types
- Resolvers
- Django model integration
- Basic CRUD operations
- Testing GraphQL endpoints with GraphiQL

## Technologies

- Python 3
- Django
- Strawberry GraphQL
- SQLite (default)

## Learning Objectives

By completing this project, you will learn how to:

- Configure Strawberry in a Django project
- Create GraphQL schemas using Python type annotations
- Implement queries and mutations
- Connect GraphQL with Django models
- Build a simple CRUD API
- Explore and test the API using GraphiQL

## Project Structure

```text
project/
├── app/
│   ├── models.py
│   ├── schema.py
│   ├── queries.py
│   ├── mutations.py
│   └── types.py
├── config/
├── manage.py
└── requirements.txt
```

## Running the Project

```bash
git clone https://github.com/yurifarod/django_graphql_strawberry_fundamentals.git
cd django_graphql_strawberry_fundamentals

python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

## Accessing GraphiQL

After starting the server, open the GraphQL playground in your browser:

```
http://127.0.0.1:8000/graphql/
```

## Example Query

```graphql
query {
  books {
    id
    title
    author
  }
}
```

## Example Mutation

```graphql
mutation {
  createBook(data: {
    title: "Clean Code"
    author: "Robert C. Martin"
  }) {
    id
    title
  }
}
```

## Purpose

This repository is intended for students and developers who want to learn the fundamentals of GraphQL with Django using Strawberry in a practical, beginner-friendly way.
