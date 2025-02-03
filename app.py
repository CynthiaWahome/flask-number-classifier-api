from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables from .env
load_dotenv()

# Define constants for error messages, success messages, and instructions
ERROR_INVALID_INPUT = "Invalid input. Please provide a number."
ERROR_INVALID_NUMBER = "The number you provided is not valid."
ERROR_INVALID_RANGE = "The number is too large or negative. Please provide a valid integer or float."
SUCCESS_MESSAGE = "Number classified successfully."
INSTRUCTION = "To classify a number, provide a number value in the URL, e.g., /api/classify-number?number=42"

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Helper Functions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 0:
        return False  # 0 and negative numbers cannot be perfect
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    digits = [int(d) for d in str(abs(int(n)))]  # Handle negative numbers
    return n == sum(d**len(digits) for d in digits)

def digit_sum(n):
    return sum(int(d) for d in str(abs(int(n))))  # Handle negative numbers

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{int(n)}/math?json")
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json().get("text", "No fun fact available")
    except requests.exceptions.RequestException as e:
        return f"No fun fact found, error: {e}"

def create_error_response(message, status_code, number="alphabet", instruction=""):
    return jsonify({
        "number": number,
        "error": True,
        "message": message,
        "instruction": instruction
    }), status_code

# Routes
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    # Step 1: Get the 'number' parameter from query string
    number = request.args.get('number')

    # Step 2: Validate if the parameter is provided
    if not number:
        return create_error_response(ERROR_INVALID_INPUT, 400, "alphabet", INSTRUCTION)

    # Step 3: Try to convert the parameter to a float (to handle both integer and float values)
    try:
        number = float(number)
    except ValueError:
        return create_error_response(ERROR_INVALID_NUMBER, 400, "alphabet", INSTRUCTION)

    # Step 4: Additional validation for extreme values (optional, depending on project needs)
    if number < -10**6 or number > 10**6:  # Arbitrary range validation
        return create_error_response(ERROR_INVALID_RANGE, 400, "alphabet", "Number should be a valid integer or float within an acceptable range.")

    # Step 5: Process the number
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("odd" if number % 2 != 0 else "even")

    response = {
        "number": number,
        "is_prime": is_prime(int(number)) if number.is_integer() else False,  # Only integers can be prime
        "is_perfect": is_perfect(int(number)) if number.is_integer() else False,  # Only integers can be perfect
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number),
        "instruction": INSTRUCTION
    }

    return jsonify(response)

# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        "error": True,
        "message": "Resource not found. The endpoint may be incorrect.",
        "instruction": "Ensure the URL is correct and try again."
    }), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({
        "error": True,
        "message": "An unexpected error occurred. Please try again later.",
        "instruction": "Contact support if the issue persists."
    }), 500

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)