from flask import Flask, request, Response, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Home of Flask"

# POST API - accepts JSON data
@app.route('/cal', methods=['POST'])
def calculator_post():
    data = request.get_json()
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')

    if not all([operation, isinstance(num1, (int, float)), isinstance(num2, (int, float))]):
        return "Invalid input data", 400

    if operation == 'add':
        return str(num1 + num2)
    elif operation == 'subtract':
        return str(num1 - num2)
    elif operation == 'multiply':
        return str(num1 * num2)
    elif operation == 'divide':
        if num2 != 0:
            return str(num1 / num2)
        else:
            return "Cannot divide by zero", 400
    else:
        return "Invalid operation", 400

# GET API - accepts URL params
@app.route('/cal_browser', methods=['GET'])
def calculator_get():
    operation = request.args.get('operation')
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except (TypeError, ValueError):
        return "Invalid numbers provided", 400

    if operation == 'add':
        return str(num1 + num2)
    elif operation == 'subtract':
        return str(num1 - num2)
    elif operation == 'multiply':
        return str(num1 * num2)
    elif operation == 'divide':
        if num2 != 0:
            return str(num1 / num2)
        else:
            return "Cannot divide by zero", 400
    else:
        return "Invalid operation", 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)
