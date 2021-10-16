'''
Coordinator: Main coordinator
-----------------------------

This module run the coordinator app
'''

from service_coordinator import run_service_coordinator
import config

def main():
    '''
    This function allows the user to start the app
    with or without debug mode, and put the ip and port
    of the coordinator app
    '''
    host = config.host
    port = config.port
    run_service_coordinator(host, port)

if __name__ == '__main__':
    main()
