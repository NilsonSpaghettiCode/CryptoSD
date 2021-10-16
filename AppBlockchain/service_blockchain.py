'''
Blockchain: Service Blockchain
-----------------------------

This a package that contains the main function for the service blockchain
'''

from blockchain import Blockchain
from transaction import Transaction
from flask import Flask, json, jsonify, request
  
app = Flask(__name__)
blockchain_s = Blockchain()

@app.route('/register_data', methods = ['POST'])
def register_data():
    '''
    This web service add the transaction to the
    block, and then when the block is full, the block is 
    aggregated to the blockchain
    url: http://127.0.0.1:5002/register_transaction/<from,to,amount>
    '''
    if(request.method == 'POST'):
        new_transaction = Transaction(request.form['from_wallet'],request.form['to_wallet'],request.form['amount'])
        return blockchain_s.register_transaction_block(new_transaction)

@app.route('/')
def block_chain():
    return blockchain_s.__str__()


@app.route('/consult_address', methods = ['POST'])
def consult_address():
    '''
    This web service consult with the blockchain the
    address, if exists in the blockchain
    url: http://127.0.0.1:5002/consult_address
    '''
    if (request.method == 'POST'):
        #blockchain_s
        return jsonify({'data': 'Nilson puto'})
  
def run_services_blockchain(ip, port):
    '''
    This function getup the service blockchain
    '''
    app.run(ip, port, debug = True)