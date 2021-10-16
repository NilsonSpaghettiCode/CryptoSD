'''
Blockchain: Class Wallet
-----------------------------

This module create the wallet for the users, an unique number account,
but this number is anonymous, then use the user name to describe the 
transactions
'''

import hashlib
from random import randint

class Wallet():
    '''
    This class create the wallet for the user
    '''
    def __init__(self):
        '''
        The constructor of the wallet
        '''
        self.counter = 0

    def generate_new_wallet(self):
        '''
        This function generated a number account random
        using a function hash with a especial concat for valid
        the form
        '''     
        wallet = self.counter
        encrypt = hashlib.md5() 
        encrypt.update(str(wallet).encode('utf-8'))
        wallet = encrypt.hexdigest()
        self.counter += 1
        return "ACC"+wallet+"BCX"

