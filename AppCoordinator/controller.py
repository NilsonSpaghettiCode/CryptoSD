'''
Coordinator: Class Controller
-----------------------------

This module perform like someone who makes
the mainstage for all the components
'''

from middleware import Middleware

class Controller():
    '''
    This controller perform like the driver
    of the app code
    '''
    def __init__(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def consult_founds(dict_parameters):
        '''
        This function consume a service from Blockchain
        to get the money in a wallet, only if this wallet
        is valid
        :param account: the wallet of the user
        :type account: str
        :returns: a dictionary with the account, founds in 
        the wallet and the exist of the account
        :rtype: dict 
        '''
        req = Middleware()
        req.load_services() 
        return req.consult_found_block_chain_service(dict_parameters)

    def close_block():
        pass
    def register_transaction():
        pass
    def register_data():
        pass
    