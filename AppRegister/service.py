'''
Register: Consume service
-----------------------------

This module consume the service from
the coordinator with the required data
'''

import requests
import config 

class Services():
    def __init__(self):
        pass

    def consume_service(self, type_method, uri, dict_parameter):
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
        payload = dict_parameter
        print('Payload:', payload)
        headers = {}
        response = {}
        try:
            data = requests.request(method=type_method, url=uri, headers=headers, data=payload)
            response = data.json()
        except Exception:
            pass
        return response['content'] 
    
    def consume_register_data(self, dict_parameter):
        return self.consume_service('POST', config.services_c['register_data'], dict_parameter)
        
    def consume_consult_founds(self, dict_parameter):
        '''
        This function consume a service that consult blockchain of money of a wallet
        :format_response: {'amount': int, 'exists': bool, 'request_wallet': str}
        :returns: return a dictionry
        :rtype: dict[str, Any]
        '''
        return self.consume_service('POST', config.services_c['consult_founds'], dict_parameter)
        