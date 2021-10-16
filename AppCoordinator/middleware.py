'''
Coordinator: Middleware
-----------------------------

This module has functions that coordinate all the blockchain system
'''

import config as service
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
    
    def add_web_service(self, name, url):
        '''
        This function allows the middleware add new web service
        with a minimum of information belongs to each web service
        in the dictionary
        :param name: the name or key of the web service
        :type name: str
        :param url: the url where the web service is or will be host
        :type url: str
        '''
        self.web_service_url[name] = url
    
    def load_services(self):
        '''
        This function execute with the instance 
        of Middleware, so allows to add the principals web services
        '''
        self.add_web_service('blockchain', service.blockchain)
        self.add_web_service('register', service.register)
        self.add_web_service('opencloser', service.opencloser)
    
    def __str__(self):
        '''
        This function is used to get the dictionary with the information 
        of the web service in a string format
        '''
        return str(self.web_service_url)

    def consume_service(self, type_method, uri, dict_parameter:dict):
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
        response_unformat = {'url': uri,'status': 503, 'content': ''}
        try:
            data = requests.request(method=type_method, url=uri, headers=headers, data=payload)
            response_unformat['status'] = data.status_code
            response_unformat['content'] = data.json()
        except Exception:
            pass
        print("Servicio consumido: ",response_unformat)
        return response_unformat
    
    def consult_found_block_chain_service(self, dict_parameters):
        '''
        This function allow consume consult_found blockchain service that use the method POST
        :param dict_paramteres: this parameter hava all parameters for use the service blockchain
        :type dict_paramteres: dict
        :returns: this function return a response with format JSON
        :rtype: dict[str, Any] 
        '''
        return self.consume_service('POST', self.web_service_url['blockchain'], dict_parameters)
        
