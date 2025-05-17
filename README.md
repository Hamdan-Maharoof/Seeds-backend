# README.md
# Seeds Platform Backend

This repository provides a simple Flask-based RESTful API for the Seeds platform. It exposes three endpoints:

- **List courses per student**: `GET /students/<student_id>/courses`
- **List courses per teacher**: `GET /teachers/<teacher_id>/courses`
- **List all data**: `GET /all-data`

---

## Prerequisites

- Python 3.7 or higher  
- `pip` package manager  

---

## Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/seeds-backend.git
   cd seeds-backend
   ```

2. **Create a virtual environment** (optional, but recommended)  
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**  
   ```bash
   python app.py
   ```
   By default, the app runs on `http://localhost:5000`

---

## API Usage

### 1. List Student Courses

- **Request**  
  ```http
  GET /students/{student_id}/courses
  ```
- **Example**  
  ```bash
  curl http://localhost:5000/students/3/courses
  ```

### 2. List Teacher Courses

- **Request**  
  ```http
  GET /teachers/{teacher_id}/courses
  ```
- **Example**  
  ```bash
  curl http://localhost:5000/teachers/2/courses
  ```

### 3. List All Data

- **Request**  
  ```http
  GET /all-data
  ```
- **Example**  
  ```bash
  curl http://localhost:5000/all-data
  ```

---

## Notes

- The root path (`/`) is not implemented and will return a 404.  
- All data is stored in-memory for demonstration purposes.  
- Feel free to extend with a database backend or authentication as needed.
