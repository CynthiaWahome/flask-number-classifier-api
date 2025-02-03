# Number Classification API

This is a **Number Classification API** built using **Flask** and deployed to a publicly accessible endpoint. The API takes a number as input and returns interesting mathematical properties about it, along with a fun fact fetched from the [Numbers API](http://numbersapi.com/).

---

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [API Endpoint](#api-endpoint)
4. [Request and Response Examples](#request-and-response-examples)
5. [How to Run Locally](#how-to-run-locally)
6. [Deployment](#deployment)
7. [Error Handling](#error-handling)
8. [Contributing](#contributing)
9. [License](#license)

---

## Features
- **Number Classification**: Determines if a number is prime, perfect, Armstrong, odd, or even.
- **Digit Sum**: Calculates the sum of the digits of the number.
- **Fun Fact**: Fetches a fun fact about the number from the Numbers API.
- **Error Handling**: Provides meaningful error messages for invalid inputs or server errors.
- **CORS Support**: Handles Cross-Origin Resource Sharing (CORS) for frontend compatibility.

---

## Technologies Used
- **Python**: The programming language used for the backend logic.
- **Flask**: A lightweight web framework for building the API.
- **Requests**: A library for making HTTP requests to the Numbers API.
- **Flask-CORS**: A Flask extension for handling CORS.
- **dotenv**: A library for loading environment variables from a `.env` file.

---

## API Endpoint
### **GET `/api/classify-number`**
Classifies a number and returns its properties.

#### Parameters
- **`number`**: The number to classify. Must be a valid integer.

#### Example Request
GET /api/classify-number?number=42

#### Example Response (200 OK)
```json
{
    "number": 42,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["even"],
    "digit_sum": 6,
    "fun_fact": "42 is the number of little squares forming the left side trail of Microsoft's Windows 98 logo.",
    "instruction": "Replace 'number' in the URL with a valid integer e.g. /api/classify-number/42"
}
```

#### Example Response (400 Bad Request)
```json
{
    "number": "alphabet",
    "error": true,
    "message": "Invalid input. Please provide an integer.",
    "instruction": "To classify a number, provide an integer value in the URL, e.g., /api/classify-number/42"
}
```

#### Example Response (500 Internal Server Error)
```json
{
    "error": true,
    "message": "An unexpected error occurred.",
    "instruction": "To classify another number, replace the value of the 'number' parameter in the URL, e.g., /api/classify-number/42"
}
```
## How to Run Locally
Clone the Repository:

```bash
git clone https://github.com/CynthiaWahome/flask-number-classifier-api.git
cd flask-number-classifier-api
```
Set Up a Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install Dependencies:

```bash
pip install -r requirements.txt
```
Run the Application:

```bash
python app.py
```
Access the API:
Open your browser or use a tool like Postman to access:

```bash
http://127.0.0.1:5000/api/classify-number?number=42
```
## Deployment
The API can be deployed to any platform that supports Python applications. Here are some options:

### Heroku
Install the Heroku CLI and log in:

```bash
brew install heroku/brew/heroku
heroku login


Create a new Heroku app and deploy:

```bash
heroku create
git push heroku main
```

### Render
1. Create a new web service on Render and connect your GitHub repository.
2. Set the build and start commands:
    - Build Command: `pip install -r requirements.txt`
    - Start Command: `gunicorn app:app`


The API provides meaningful error messages for the following scenarios:

- **Invalid Input**: If the input is not a valid integer, a 400 Bad Request response is returned.
- **Server Errors**: If an unexpected error occurs, a 500 Internal Server Error response is returned.
- **Resource Not Found**: If the requested resource is not found, a 404 Not Found response is returned.

## License
This project is licensed under the MIT License. See the LICENSE file for details.



