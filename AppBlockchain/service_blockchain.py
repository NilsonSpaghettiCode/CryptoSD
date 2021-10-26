'''
Blockchain: Service Blockchain
---------------------------------

This a package that contains the main function for the service blockchain
'''

from blockchain import Blockchain
from transaction import Transaction
from flask import Flask, jsonify,request
  
app = Flask(__name__)
blockchain_s = Blockchain()

@app.route('/register_data', methods = ['POST'])
def register_data():
    '''
    This web service add the transaction to the
    block, and then when the block is full, the block is 
    aggregated to the blockchain

    .. parsed-literal::
        # show Blockchain
        curl http://localhost:5201/register_data/

    .. code-block:: json

        {
        "status_transaction": 0,
        "Transaction": [
                    {
                    "from_u": "account_send",
                    "to_u": "account_receive",
                    "amount": "amount"
                    }
                ]
        }

    '''
    if(request.method == 'POST'):
        new_transaction = Transaction(request.form['from_wallet'],request.form['to_wallet'],request.form['amount'])
        return blockchain_s.register_transaction_block(new_transaction)

@app.route('/')
def block_chain():
    '''
    This web service show the blockchain

    .. parsed-literal::
        # show Blockchain
        curl http://localhost:5201/

    .. code-block:: json

        {
        "Cantidad": 0,
        "blockchain": []
        }

    '''
    return blockchain_s.__str__()


@app.route('/consult_address', methods = ['POST'])
def consult_address():
    '''
    This web service consult with the blockchain the
    address, if exists in the blockchain

    .. parsed-literal::
        # show the account amount if it has funds in the blockchain
        curl http://localhost:5201/consult_address

    .. code-block:: json

        {
        "amount": 0,
        "exists": false,
        "request_wallet": "address"
        }

    '''

    if (request.method == 'POST'):
        return blockchain_s.consult_founds_wallet(request.form['wallet'])
        
@app.route('/new_account', methods = ['POST'])
def new_account():
    '''
    This web service create a new account for a user, this service return
    a number of wallet and that has
    
    .. parsed-literal::
        # create the wallet account
        curl http://localhost:5201/new_account

    .. code-block:: json

        {
        "error": "User exists",
        "exist": true,
        "user": "name_user"
        }

    '''
    response_user = blockchain_s.generate_wallet(request.form['name_user'])
    return jsonify(response_user)

@app.route('/users', methods = ['GET'])
def users():
    '''
    This web service return a list of user in the public ledger with format json

    .. parsed-literal::
        # show the user list
        curl http://localhost:5201/users

    .. code-block:: json

        {
                [
            {
            "user": "name_user",
            "account": "new_account"
            }
                ]
        }

    '''

    return  jsonify(blockchain_s.users())
  
def run_services_blockchain(ip, port):
    '''
    This function getup the service blockchain
    '''
    app.run(ip, port, debug = True)