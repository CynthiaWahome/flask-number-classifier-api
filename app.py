from flask import Flask, request, jsonify
import requests
import os

from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return n == sum(d**len(digits) for d in digits)

def digit_sum(n):
    return sum(int(d) for d in str(n))

def  get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        return response.json().get("text", "No fun fact available")
    except:
        return "No fun fact found imagine that!"

@app.route('/api/classify-number/<number>', methods=['GET'])
def classify_number(number):
    try:
        number = int(number)
    except ValueError:
        return jsonify({
            "error": True,
            "message": "Invalid input. Please provide an integer.",
            "instruction": "To classify a number, provide an integer value in the URL, e.g., /api/classify-number/42 "
        }), 400
    try:
        properties = []
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("odd" if number % 2 != 0 else "even")

        response = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": digit_sum(number),
            "fun_fact": get_fun_fact(number),
            "instruction": "Replace 'number' in the URL with a valid integer e.g. /api/classify-number/42"
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({
            "error": True,
            "message": str(e),
            "instruction": "To classify another number, replace the value of the 'number' parameter in the URL, e.g., /api/classify-number?number=42"
        }), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)