'''
Coordinator: Middleware
-----------------------------

This module has functions that coordinate all the blockchain system
'''

from config import services
import requests
from werkzeug.wrappers import response

class Middleware:
    '''
    This class register the required web service to 
    coordinate all the functions of CryptoSD:Blockchain 
    '''
    def __init__(self):
        '''
        The constructor of the middleware where is going to
        storage all the web services
        '''
        self.web_service_url = {}
    
    def load_services(self):
        '''
        This function execute with the instance 
        of Middleware, so allows to add the principals web services
        '''
        self.web_service_url = services
    
    def __str__(self):
        '''
        This function is used to get the dictionary with the information 
        of the web service in a string format
        '''
        return str(self.web_service_url)

    def consume_service(self, type_method, uri, dict_parameter:dict={}):
        '''
        This function is used to consume a web service, and return a response, no matter
        if the communication fails
        :param type_method: the method where is going to pass the communication (POST/GET)
        :type param: str
        :param uri: the url where is located the web service to consume
        :type uri: str
        :param dict_parameter: the content of the payload
        :type dict_parameter: dict
        :returns: returns a custom dict with the url, status and content. The "Any" return is a JSON content
        :rtype: dict[str, Any] 
        '''
        payload = dict(dict_parameter)
        headers = {}
        response_unformat = {'url': uri,'status': 503, 'content': '', 'active': False}
        try:
            data = requests.request(method=type_method, url=uri, headers=headers, data=payload)
            response_unformat['status'] = data.status_code
            response_unformat['content'] = data.json()
            response_unformat['active'] = True
        except Exception:
            pass
        return response_unformat
    
    def consult_found_block_chain_service(self, dict_parameters):
        '''
        This function allows to consume consult_found blockchain service that use the method POST
        :param dict_parameters: this parameter hava all parameters for use the service blockchain
        :type dict_parameters: dict
        :returns: this function return a response with format JSON
        :rtype: dict[str, Any] 
        '''
        return self.consume_service('POST', self.web_service_url['blockchain_consult_address'], dict_parameters)
        
    def get_block_chain(self):
        '''
        This function allows to the user to see the blockchain, this function has the purpose of
        debug the code
        '''
        return self.consume_service('GET', self.web_service_url['blockchain_show'])

    def close_block(self, dict_parameters):
        '''
        This function allows to the blockchain, close a block through a hash
        :param dict_parameters: the block which is going to close the opencloser
        :type dict_parameters: dict
        :returns: the hash of the block
        :rtype: dict
        '''
        return self.consume_service('POST',self.web_service_url['opencloser'], dict_parameters)
    
    def get_wallet(self, dict_parameters):
        '''
        This function allows to the user request a account from the class wallet in 
        Blockchain
        :param dict_parameters: the user name
        :type dict_parameters: dict
        :returns: the account of the user
        :rtype: dict 
        '''
        return self.consume_service('POST', self.web_service_url['blockchain_new_account'], dict_parameters)
    
    def get_user_list(self):
        '''
        This function allows to the developers to see the users in the Blockchain
        across the public ledger
        :returns: the list of the user accounts
        :rtype: dict
        '''
        return self.consume_service('GET', self.web_service_url['blockchain_show_users'])