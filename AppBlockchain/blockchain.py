'''
Blockchain: Class Blockchain
-----------------------------

This module create the instance of a block with the common atributes
'''

from block import Block
from transaction import Transaction

class Blockchain():
    '''
    This class contains all the blockchain functions with
    the list of blocks, instance this class once to create
    the blockchain
    '''
    def __init__(self, blockchain:list = [], amount:int = 0):
        '''
        This is the constructor of the blockchain
        :param blockchain: receives a list of blocks
        :type blockchain: list
        :param amount: the amount of crypto money in the blockchain
        :type amount: int
        '''
        self.blockchain = blockchain
        self.hash_blockchain = ''
        self.amount = amount
        self.block_instanted = Block()
    
    def set_blockchain_hash(self, hash_blockchain):
        '''
        This function adds the hash of the blockchain
        each time a block is added
        :param hash_blockchain: the hash of the list of blocks in the blockchain
        :type hash_blockchain: hash
        '''
        self.hash_blockchain = hash_blockchain
    
    def register_transaction_block(self, transaction:Transaction):
        '''
        This function register the object transaction in the current block
        :param transaction: the transaction to be added to the block
        :type transaction: Object<Transaction>
        '''
        self.block_instanted.add_transaction(transaction)
    
    def verify_block_length(self):
        '''
        This function verify the block length
        '''
        pass
    
    def close_block(self):
        '''
        This function receives a response from OpenCloser across Coordinator
        and close the block, only if this is full
        '''
        pass
    
    def add_new_block(self):
        '''
        This function reset the instance of block, where is going to write the
        transactions 
        '''
        self.block_instanted = Block()
    
    def calculate_founds_blockchain(self):
        '''
        This functions calculate the current founds in the blockchain
        '''
        '''
        total = 0
        for block in self.blockchain:
            for money in block.transactions:
                total += money.amount
        '''