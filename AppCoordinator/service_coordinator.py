#from flask import Flask, request, jsonify

#app = Flask(__name__)
'''
Service coordinator Package
-----------------------------

This a package that contains the main function for the service coordinator
'''





def run_service_coordinator(host:str, port:int):
    ''' 
    This function runs the service coordinator that 
    allow comunicate diferents services
    
    :param host: the ip where the app will be host
    :type host: str
    :param port: port is a localport controled for specfic OS 
    :type port: int
    '''
    print("Hola mundo")
    #app.run(host, port, debug=True)

help(run_service_coordinator)
#__doc__(run_service_coordinator)