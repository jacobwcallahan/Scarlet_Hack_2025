from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Endpoint 1: Simple Hello API
@app.route("/hello/", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!"})

# Endpoint 2: Multiply two numbers
@app.route("/multiply/", methods=["GET"])
def multiply():
    a = int(request.args.get('a', 1))
    b = int(request.args.get('b', 1))
    result = a * b
    return jsonify({"result": result})

# Endpoint 3: Reverse a given string
@app.route("/reverse/", methods=["GET"])
def reverse_string():
    text = request.args.get('text', '')
    reversed_text = text[::-1]  # Reverse the string
    return jsonify({"reversed_text": reversed_text})

# Endpoint 4: Sum an array of numbers
@app.route("/sum/", methods=["POST"])
def sum_numbers():
    data = request.get_json()
    numbers = data.get("numbers", [])
    result = sum(numbers)
    return jsonify({"sum": result})

if __name__ == "__main__":
    app.run(debug=True)
