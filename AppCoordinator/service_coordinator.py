'''
Coordinator: Service Coordinator
-----------------------------------

This a package that contains the main function for the service coordinator
'''

from flask import Flask, request
from flask.json import jsonify
from controller import Controller
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADER'] = 'Content-Type'

@app.route('/')
def get_something():
    '''
    Main page
    '''
    return "<h1>Coordinator</h1>"

# <---------------------------- Service for client --------------------------------->
@cross_origin()
@app.route('/register_transaction', methods=['POST'])
def transaction_register():
    '''
    Web service for the client, that execute all the required proccess
    to valid a transaction and add to the block the new transaction,
    before add the complete block to the blockchain

    .. parsed-literal::
        # coordinator for transaction register
        curl http://localhost:5200/register_transaction

    .. code-block:: json
        
        {
        "active": false
        "url": "uri",
        "status": 503,
        "content" : {
            "status_transaction": 0,
            "Transaction": [
                    {
                    "from_u": "account_send",
                    "to_u": "account_receive",
                    "amount": "amount"
                    }
                        ]
            }
        }
        
    '''
    return Controller.register_transaction(request.form)
    

@app.route('/consult_founds', methods=['POST'])
@cross_origin()
def consult_founds():
    '''
    Web service for the client, that execute the required proccess,
    calling all the correspond web service from the others components
    to get the user founds in the wallet

    .. parsed-literal::
        # coordinator for consult_founds
        curl http://localhost:5200/consult_founds

    .. code-block:: json
        
        {
        "active": false
        "url": "uri",
        "status": 503,
        "content" : {
            "amount": 0,
            "exists": false,
            "request_wallet": "address"
                }
        }

    '''
    if request.method == 'POST':
        # response_json = {'account':account,
        #                 'founds':0,
        #                 'exists':False
        #                 }
        response_json = Controller.consult_founds(request.form)
        return response_json
    else:
        return f'<p>Algo salio mal...</p>'

@app.route('/show_block_chain', methods=['GET'])
def show_block_chain():
    '''
    This web service shows the blockchain

    .. parsed-literal::
        # coordinator for show blockchain
        curl http://localhost:5200/show_block_chain

    .. code-block:: json
        
        {
        "active": false
        "url": "uri",
        "status": 503,
        "content" : {
                "Cantidad": 0,
                "blockchain": []
                }
        }

    '''
    return jsonify(Controller.show_block_chain())

@app.route('/create_wallet', methods=['POST'])
@cross_origin()
def create_wallet():
    '''
    This web service create the wallet of the user

    .. parsed-literal::
        # coordinator for create wallet
        curl http://localhost:5200/create_wallet

    .. code-block:: json
        
        {
        "active": false
        "url": "uri",
        "status": 503,
        "content" : {
            "error": "User exists",
            "exist": true,
            "user": "name_user"
                }
        }

    '''

    return jsonify(Controller.create_user(request.form))

@app.route('/show_users', methods=['GET'])
def show_users():
    '''
    This web service has the purpose of debugging code,
    allows to show all the wallets in the public ledger

    .. parsed-literal::
        # coordinator for show users
        curl http://localhost:5200/show_users

    .. code-block:: json
        
        {
        "active": false
        "url": "uri",
        "status": 503,
        "content" : {
                [
            {
            "user": "name_user",
            "account": "new_account"
            }
                ]
            }
        }

    '''
    
    return jsonify(Controller.show_wallets())

# <--------------------------------- Service for components --------------------------------->

@app.route('/register_data', methods=['POST'])
def register_data():
    '''
    This web service is for valid the transaction
    which is going to the block, that means is the
    in carge of certificate the transactions

    .. parsed-literal::
        # coordinator for register data
        curl http://localhost:5200/register_data

    .. code-block:: json
        
        {
        "active": false
        "url": "uri",
        "status": 503,
        "content" : {
            "transaction_valid": false,
            "error": "No error",
            "transaction_done": false,
            "transaction": {
                    "from_wallet": "wallet_from",
                    "to_wallet": "wallet_to",
                    "amount": "amount"
                            }
                                
                    } 
        }

    '''
    return Controller.register_data(request.form)

@app.route('/close_block', methods=['POST'])
def close_block():
    '''
    This web service is for the blockchain, when a block is full
    the blockchain request this web service

    .. parsed-literal::
        # coordinator for close block
        curl http://localhost:5200/close_block

    .. code-block:: json
        
        {
        "active": false
        "url": "uri",
        "status": 503,
        "content" : {
                "hash_of_the_block": "hash_block"
                    }
        }

    '''
    return jsonify(Controller.close_block(request.form))

def run_service_coordinator(host:str, port:int):
    ''' 
    This function runs the service coordinator that 
    allow comunicate diferents services
    
    :param host: the ip where the app will be host
    :type host: str
    :param port: port is a localport controled for specfic OS 
    :type port: int
    '''
    app.run(host, port, debug=True)
