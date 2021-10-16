'''
Blockchain: Class Block
-----------------------------

This module create the instance of a block with the common atributes
'''

from transaction import Transaction

class Block():
    '''
    This class contains the block who's going to add in the blockchain
    when the transactions has three records with valid money transferences
    '''
    def __init__(self, number_block:int, nonce:int, transactions:list, hash_preview, hash):
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
        self.number_block = number_block
        self.nonce = nonce
        self.transactions:list = transactions
        self.hash_preview = hash_preview
        self.hash = hash
    
    def add_transaction(self, transaction:Transaction):
        '''
        This function adds the transaction to the block
        :param transaction: receives the object Transaction
        :type transaction: Object<Transaction>
        '''
        if self.count_transactions() <= 3:
            self.transactions.append(transaction)

    
    def count_transactions(self):
        '''
        This function counts the length of transactions in the
        block
        '''
        return len(self.transactions)

    def add_hashes(self, hash_preview_t, hash_t):
        '''
        This function add the hashes to the block
        :param hash_preview_t: the hash of the last block in the blockchain
        :type hash_preview_t: hash
        :param hash_t: the hash of the current block
        :type hash_t: hash
        '''
        self.hash_preview = hash_preview_t
        self.hash = hash_t