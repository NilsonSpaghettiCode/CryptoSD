'''
Register: Main Register
-----------------------------

This module run the register app
'''

import config
from service_register import run_service_register
def main():
    '''
    This function allows the user to start the app Blockchain
    with or without debug mode, and put the ip and port
    of the register app
    '''
    host = config.host
    port = config.port
    run_service_register(host, port)

if __name__ == '__main__':
    main()
    