'''
Coordinator: Config
-----------------------------

This module contains the config
'''
# Web services
services = {
            # Blockchain services
            'blockchain_show':'http://127.0.0.1:5002/',
            'blockchain_register_data':'http://127.0.0.1:5002/register_data',
            'blockchain_consult_address':'http://127.0.0.1:5002/consult_address',
            'blockchain_new_account':'http://127.0.0.1:5002/new_account',
            'blockchain_show_users':'http://127.0.0.1:5002/users',
            # Register services
            'register':'http://127.0.0.1:5004/register_transaction',
            # OpenCloser servicess
            'opencloser':'http://127.0.0.1:5003/closer_block'}

# Host and port
host = '0.0.0.0'
port = 5001