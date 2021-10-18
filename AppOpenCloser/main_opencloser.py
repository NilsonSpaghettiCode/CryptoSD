'''
OpenCloser: Main OpenCloser
-----------------------------

This module run the OpenCloser app
'''
from service_opencloser import run_service_opencloser
import config

def main():
    '''
    This function allow the user to start the web service 
    OpenCloser app in a specific host and port assigned 
    to the OpenCloser app
    '''
    host = config.host
    port = config.port
    run_service_opencloser(host, port)


if __name__ == '__main__':
    main()
