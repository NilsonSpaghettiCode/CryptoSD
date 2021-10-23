'''
Blockchain: Services class
-----------------------------

This module consume the service
'''

import requests
import config_blockchain as config 

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
        print("Payload:", payload)
        headers = {}
        response = {}
        try:
            data = requests.request(method=type_method, url=uri, headers=headers, data=payload)
            response = data.json()
        except Exception:
            pass
        return response['content'] 
    
    
    def service_close_block(self, dict_parameters):
        return self.consume_service('POST', config.open_closer, dict_parameters)