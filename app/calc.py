from flask import Flask, jsonify

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return jsonify({"Name":"Anish S Mahale","Reg No":"19BBS0007"})


@app.route('/add/<int:a>/<int:b>')
def addition(a,b):
    result = a + b
    return jsonify({'Addition':result})

@app.route('/subtract/<int:a>/<int:b>')
def subtraction(a,b):
    result = a - b
    return jsonify({'Subtraction':result})

@app.route('/multiply/<int:a>/<int:b>')
def multiplication(a,b):
    result = a * b
    return jsonify({'Multiplication':result})

@app.route('/divide/<int:a>/<int:b>')
def division(a,b):
    result = a / b
    return jsonify({'Division':result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
