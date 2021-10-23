'''
Coordinator: Config
-----------------------------

This module contains the config
'''
# Web services
services = {
            # Blockchain services
            'blockchain_show':'http://172.18.0.4:5201/',
            'blockchain_register_data':'http://172.18.0.4:5201/register_data',
            'blockchain_consult_address':'http://172.18.0.4:5201/consult_address',
            'blockchain_new_account':'http://172.18.0.4:5201/new_account',
            'blockchain_show_users':'http://172.18.0.4:5201/users',
            # Register services
            'register':'http://172.18.0.5:5202/register_transaction',
            # OpenCloser servicess
            'opencloser':'http://172.18.0.2:5203/closer_block'
            }

# Host and port
host = '0.0.0.0'
port = 5200