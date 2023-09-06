#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:parameter>")
def print_string(parameter):
    print (parameter)
    return parameter

@app.route("/count/<int:parameter>")
def count(parameter):
    r = ""
    for num in range(0, parameter):
        print(f"{num}")
        r = r + str(num) + "\n"
    return r

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math (num1, operation, num2):
    answer = 0
    if operation == 'div':
        answer = num1/num2
    elif operation == '+':
        answer = num1+num2
    elif operation == '-':
        answer = num1-num2
    elif operation == '*':
        answer = num1*num2
    else:
        answer = num1%num2
    return str(answer)
        

if __name__ == '__main__':
    app.run(port=5555, debug=True)
