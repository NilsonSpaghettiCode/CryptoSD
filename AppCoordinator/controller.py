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
    @staticmethod
    def consult_founds(dict_parameters):
        '''
        This function consume a service from Blockchain
        to get the money in a wallet, only if this wallet
        is valid

        :param account: the wallet of the user
        :type account: str
        :returns: a dictionary with the account, founds in the wallet and the exist of the account
        :rtype: dict 
        '''
        req = Middleware()
        req.load_services() 
        return req.consult_found_block_chain_service(dict_parameters)
    
    @staticmethod
    def close_block(block):
        '''
        This function makes all the logic to connect the Blockchain
        with the OpenCloser component

        :param block: the block to close
        :type block: dict
        :returns: a dict with the response
        :rtype: dict
        '''
        req = Middleware()
        req.load_services() 
        return req.close_block(block)

    @staticmethod
    def register_transaction(dict_transaction):
        '''
        This function allows to the blockchain receive the transaction
        and add to the current block

        :returns: a dict with the response
        :rtype: dict
        '''
        req = Middleware()
        req.load_services()

        return req.consume_register_transaction(dict_transaction)

    @staticmethod    
    def register_data(dict_parameters):
        '''
        This function register and validate the data

        :params dict_parameters:
        :type dict_parameters:
        :returns: return a dictionary with the valid transaction
        :rtype: dict
        '''
        req = Middleware()
        req.load_services()
        return req.consume_register_data(dict_parameters)
        
    @staticmethod
    def show_block_chain():
        '''
        This method static, load services and consume the service show_block_chain

        :returns: return a dictionary with status information and the blockchain
        :rtype: dict
        '''
        req = Middleware()
        req.load_services()

        return req.get_block_chain()
    
    @staticmethod
    def create_user(user):
        '''
        This static method, load services and consume the service from Blockchain
        where is going to storage the wallets of the users

        :param user: the name of the user 
        :type user: dict
        :returns: the wallet with the message
        :rtype: dict
        '''
        req = Middleware()
        req.load_services()

        return req.get_wallet(dict_parameters=user)
    
    @staticmethod
    def show_wallets():
        '''
        This static method, load the services and consume the service from Blockchain
        to show all the users in the public ledger

        :returns: all the wallets
        :rtype: dict
        '''
        req = Middleware()
        req.load_services()
        
        return req.get_user_list()