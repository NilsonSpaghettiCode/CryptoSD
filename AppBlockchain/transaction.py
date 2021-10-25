'''
Blockchain: Class Transaction
-----------------------------

This module saves the transaction in a Object
'''

class Transaction():
    '''
    This class belongs to a transaction that is going to 
    save in a block, then when the block is full, the block
    is going to be part of the blockchain
    '''
    def __init__(self, from_u:str, to_u:str, amount:int):
        '''
        This is the constructor of transaction
        
        :param from_u: the wallet who sends the money
        :type from_u: str
        :param to_u: the person who receives the crypto money
        :type to_u: str
        :param amount: the total of money that is going to send
        :type amount: int
        '''
        self.from_u = from_u
        self.to_u = to_u
        self.amount = amount

    def __str__(self):

        return {'from_wallet':self.from_u,'to_wallet':self.to_u,'amount':self.amount}

    def get_amount(self):
        '''
        This function allows to get the money of a transaction
        '''
        return self.amount

    def get_from_u(self):
        '''
        This function allows to get the user who sends the money
        '''
        return self.from_u
        
    def get_to_u(self):
        '''
        This function allows to get the user who receives the money
        '''
        return self.to_u