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

## Jinja2 – Flask Templating Engine

Flask uses **Jinja2** to generate **dynamic HTML** for web applications.

Jinja2 is mainly used when building **server-rendered web pages**.  
It is **not required** when building pure REST APIs that return JSON.

---

### What is Jinja2?

Jinja2 is a **template engine** for Python.

It allows you to:
- Write HTML files
- Embed Python-like logic inside them
- Render dynamic content using data from Flask

---

### Why Jinja2 is Needed

Without Jinja2:
- You would have to write static HTML files
- No dynamic content (user names, lists, conditions)

With Jinja2:
- HTML can change based on data
- Same template can be reused multiple times
- Cleaner separation between logic and UI

---

### How Jinja2 Works with Flask

1. Flask receives a request
2. Flask prepares data (Python variables)
3. Flask passes data to a Jinja2 template
4. Jinja2 renders HTML
5. Rendered HTML is sent to the client

---

### Basic Example

#### Flask Code
```python
from flask import render_template

@app.route("/hello")
def hello():
    return render_template("hello.html", name="User")
