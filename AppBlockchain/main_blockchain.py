'''
Blockchain: Main Blockchain
-----------------------------

This module run the blockchain app
'''


from service_blockchain import run_services_blockchain
import config_blockchain as config

def main():
    '''
    This function allows the user to start the app Blockchain
    with or without debug mode, and put the ip and port
    of the blockchain app
    '''
    host = config.host
    port = config.port
    run_services_blockchain(host, port)

if __name__ == '__main__':
    main()
    