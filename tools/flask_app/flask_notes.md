# Flask – Notes & Learnings

## What is Flask?

Flask is a **lightweight Python web framework** used to build:
- Web applications
- REST APIs
- Microservices

Flask is called a **micro-framework** because it provides only the core features:
- URL routing
- Request/response handling
- Basic templating

Flask does **not** directly handle network communication.  
It runs **inside a WSGI server**.

Everything else (database, authentication, validation, etc.) is added explicitly when needed.

---

## features

- Simple and minimal
- Easy to learn
- Highly flexible
- Great for APIs and small to medium applications
- Gives full control over architecture

---

## What is WSGI?

WSGI stands for **Web Server Gateway Interface**.

It is a **standard** that defines how:
- A web server communicates with
- A Python web application

### Why WSGI Exists
Before WSGI, each server and framework had its own communication style.  
WSGI provides a **common interface**.

### In Simple Terms
- Server receives HTTP request
- WSGI converts it to Python objects
- Flask processes the request
- Flask returns a response
- WSGI sends it back to the client

Flask uses **Werkzeug** internally as its WSGI toolkit.

---

## Flask vs Web Server (Important Difference)

### Flask (Application Layer)
- URL routing
- Business logic
- Request processing
- Response generation

### Web Server (Runtime Layer)
Examples:
- Werkzeug (development only)
- Gunicorn
- uWSGI

Responsibilities:
- Listen on ports (80 / 443)
- Handle concurrency
- Pass requests to Flask via WSGI

`app.run(debug=True)` is **not for production use**.

---

## Request → Response Lifecycle

1. Client sends HTTP request
2. Flask parses the request
3. URL is matched to a route
4. View function executes
5. Response is generated
6. Response is returned to client

## Request–Response Flow in Flask

```text
Client (Browser / API Client)
        ↓ HTTP Request
Web Server (Werkzeug / Gunicorn / uWSGI)
        ↓ WSGI
Flask Application
        ↓
View Function
        ↓
Response (HTML / JSON)
        ↓
Client



### Step-by-step Flow

1. Client sends an HTTP request
2. Web server receives the request
3. WSGI passes the request to Flask
4. Flask matches the route
5. View function executes
6. Response is created
7. Response is sent back to the client


