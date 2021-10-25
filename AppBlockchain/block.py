'''
Blockchain: Class Block
-----------------------------

This module create the instance of a block with the common atributes
'''

from transaction import Transaction
from random import randint
class Block():
    '''
    This class contains the block who's going to add in the blockchain
    when the transactions has three records with valid money transferences
    '''
    number_block_static = 0

    def __init__(self, nonce:int = 0, transactions:list = [], hash_preview = str('0'*64), hash = ''):
        '''
        The constructor of the block
        
        :param number_block: the current number of the block
        :type number_block: int
        :param nonce: the random nonce which is created to consolidate the block
        :type nonce: int
        :param transactions: the list of the transactions in the block
        :type transactions: list
        :param hash_preview: the hash of the previous block
        :type hash_preview: hash
        :param hash: the hash of the current block
        :type hash: hash
        '''
        self.number_block = self.number_block_static
        self.nonce = nonce
        self.transactions:list = transactions
        self.hash_preview = hash_preview
        self.hash = hash
        Block.number_block_static +=1
    
    def __str__(self):
        
        transaction_list = []
        for transaction in self.transactions:
            transaction_list.append(transaction.__str__())
        
        return {
                'block':self.number_block,
                'nonce':self.nonce,
                'transactions': str(transaction_list),
                'hash_preview':self.hash_preview,
                'hash':self.hash
                }

    def add_transaction(self, transaction:Transaction):
        '''
        This function adds the transaction to the block

        :param transaction: receives the object Transaction
        :type transaction: Object<Transaction>
        '''
        
        self.transactions.append(transaction)
    
    def count_transactions(self):
        '''
        This function counts the length of transactions in the
        block
        '''
        return len(self.transactions)

    def add_hashes(self, hash_preview_t = str('0'*64), hash_t=''):
        '''
        This function add the hashes to the block

        :param hash_preview_t: the hash of the last block in the blockchain
        :type hash_preview_t: hash
        :param hash_t: the hash of the current block
        :type hash_t: hash
        '''
        self.hash_preview = hash_preview_t
        self.hash = hash_t
    
    def add_nonce(self):
        '''
        This function add the nonce of the block
        a random int
                '''
        self.nonce = randint(1, 1000)

    def get_transaction_list(self):
        '''
        This function return the list of transactions
        in the block
        '''    
        return self.transactions