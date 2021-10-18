'''
Register: Service Register
-----------------------------

This module contains the web service function
for register
'''

from flask import Flask

app = Flask(__name__)  

def run_service_register(host:str, port:int):
    '''
    This function allows to run the service register 
    '''
    app.run(host,port, debug=True)