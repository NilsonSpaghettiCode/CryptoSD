'''
Coordinator: Service Coordinator
-----------------------------

This a package that contains the main function for the service coordinator
'''

from flask import Flask, request
from controller import Controller

app = Flask(__name__)

@app.route('/')
def get_something():
    '''
    Main page
    '''
    return "<h1>Coordinator</h1>"

@app.route('/register_transaction', methods=['POST'])
def transaction_register():
    '''
    Web service for the client, that execute all the required proccess
    to valid a transaction and add to the block the new transaction,
    before add the complete block to the blockchain
    url: http://127.0.0.1:5001/register_transaction

    '''
    pass

@app.route('/consult_founds', methods=['POST'])
def consult_founds():
    '''
    Web service for the client, that execute the required proccess,
    calling all the correspond web service from the others components
    to get the user founds in the wallet
    url: http://127.0.0.1:5001/consult_founds
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
