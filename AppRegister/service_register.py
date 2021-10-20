'''
Register: Service Register
-----------------------------

This module contains the web service function
for register
'''
from register import Register
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def register_home():
    return '<h1>Register</h1>'

@app.route('/register_transaction', methods=['POST'])
def register_transaction():
    '''
    This web services allows to process the request
    for validate the transactions with type method POST
    url: 'http://127.0.0.1:5004/register_transaction'
    '''
    return Register.register_transaction(request.form['from_wallet'],request.form['to_wallet'],request.form['amount'])

def run_service_register(host:str, port:int):
    '''
    This function allows run the service register 
    '''
    app.run(host,port, debug=True)