'''
OpenCloser: Service OpenCloser
---------------------------------

This module contains the web service function
for OpenCloser
'''

from flask import Flask, jsonify, request
from opencloser import OpenCloser
app = Flask(__name__)

@app.route('/closer_block', methods=['POST'])
def closer_block():
    '''
    The web service of OpenCloser hashed the block
    for blockchain and allows to close it
    
    
    .. parsed-literal::
        # close the block
        curl http://localhost:5203/closer_block

    .. code-block:: json

        {
        "hash_of_the_block": "hash_block"
        }

    '''
    hash_block = OpenCloser.hashBlock(request.form)
    result = {'hash_of_the_block': hash_block}
    return jsonify(result)

def run_service_opencloser(host:str, port:int):
    '''
    This function allows to run the service OpenCloser 
    '''
    app.run(host,port, debug=True)
    