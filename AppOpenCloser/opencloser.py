'''
OpenCloser: Class OpenCloser
-----------------------------

This module contains the class OpenCloser
'''

import hashlib

class OpenCloser():
    '''
    This class is for OpenCloser, the in charge of 
    close the blockchain blocks and response to the 
    class blockchain across the coordinator
    '''

    @staticmethod
    def hashBlock(block):
        '''
        This function generate the hash (sha256) for the block
        and return it
        
        :param block: the block to close
        :type block: Object  
        :returns: the hash of the block using the function sha256
        :rtype: hash
        '''
        print("REQ", block)
        string_block = str(dict(block))
        print(str(string_block))
        
        crypt = hashlib.sha256()
        crypt.update(str(string_block).encode('utf-8'))
        return crypt.hexdigest()

#print(OpenCloser.hashBlock(1))
