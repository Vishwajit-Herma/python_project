# Python Async Activity Tracker

## Project Overview

This project is a **pure Python mini-application** created to practice and demonstrate core Python concepts in a real-world–like scenario. The application fetches data from **public REST APIs**, processes it using **object-oriented programming**, **functional programming**, and **concurrency techniques**, and stores the processed results in **JSON files**.

---

## APIs Used

Public APIs from JSONPlaceholder:

* Users API: [https://jsonplaceholder.typicode.com/users](https://jsonplaceholder.typicode.com/users)
* Posts API: [https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts)

---

## Folder Structure

```
python_project/
│
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── sync.py          # requests-based API calls
│   │   └── async_.py        # aiohttp-based API calls
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── models.py        # BaseModel, User, Post
│   │   ├── mapper.py        # JSON → objects
│   │   └── processor.py    # filter / map / reduce / generators
│   │
│   ├── concurrency/
│   │   ├── __init__.py
│   │   ├── threads.py       # threading logic
│   │   └── processes.py    # multiprocessing logic
│   │
│   ├── storage/
│   │   ├── __init__.py
│   │   ├── sync.py          # JSON storage
│   │   └── async_.py        # async-safe storage
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   └── exceptions.py
│   │
│   └── __init__.py
│
├── data/
├── logs/
├── main.py
├── requirements.txt
└── README.md


```

---

## Application Flow

### Synchronous Main Flow (`main.py`)

1. Fetch users and posts data from APIs using **threading**
2. Convert raw JSON data into **Python objects** (`User`, `Post`)
3. Process data using functional programming techniques:

   * Filtering
   * Mapping
   * Reducing
4. Perform CPU-bound aggregation using **multiprocessing**
5. Store processed data into JSON files
6. Log all important actions and errors

### Asynchronous Reference Flow (`main.py`)

1. Fetch data from public APIs using **asyncio + aiohttp**
2. Perform lightweight processing
3. Store data using async-safe storage with `asyncio.to_thread`

This async flow is included for demonstration purposes and does not replace the main pipeline.

---

## Key Concepts Used

### Object-Oriented Programming

* Abstract base classes
* Inheritance
* Encapsulation
* Method overriding
* Operator overloading (`__str__`)

### Functional Programming

* `map` (extract user names)
* `filter` (filter users by email domain)
* `reduce` (count total posts)
* `generator` (filter users by email domain)

### Concurrency

#### Threading

* Used for I/O-bound API calls
* Fetches users and posts concurrently using blocking libraries

#### Multiprocessing

* Used for CPU-bound operations
* Counts users and posts in parallel

#### Asyncio

* Demonstrates non-blocking API calls using `aiohttp`
* Demonstrates async-safe file storage using `asyncio.to_thread`
* Implemented in a separate async entry point

---

## Error Handling

Custom exceptions are used for clarity and separation of concerns:

* `APIError` – API failures
* `DataProcessingError` – filtering, mapping, or reduce errors
* `StorageError` – file system or JSON serialization errors

All errors are logged using a centralized logger.

---

## Logging

* Logs are written to `logs/app.log`
* Includes timestamps, log levels, and messages
* Used instead of print statements for debugging and traceability

---

## How to Run the Project

### Prerequisites

* Python 3.9 or higher

### Create and Activate Virtual Environment

```bash
python -m venv venv
```

#### On Linux / macOS

```bash
source venv/bin/activate
```

#### On Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Synchronous Application

```bash
python main.py
```

## Output Files

Generated inside the `data/` directory:

* `users.json`
* `posts.json`
* `filtered_users.json`
* `user_names.json`

Async reference outputs (if enabled):

* `users_async.json`
* `posts_async.json`
* `filtered_users_async.json`
* `comments_async.json`

---

## Final Notes

* The main pipeline uses synchronous code with threading and multiprocessing for clarity.
* Async functionality is included via a separate entry point to demonstrate non-blocking I/O.
* The design prioritizes readability, correctness, and concept demonstration over premature optimization.

---

## Author

Internship Project – Python Async Activity Tracker
