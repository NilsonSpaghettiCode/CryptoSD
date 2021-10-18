'''
Blockchain: Class Blockchain
-----------------------------

This module create the instance of a block with the common atributes
'''

from flask.json import jsonify
from service import Services
from block import Block
from transaction import Transaction
from wallet import Wallet
class Blockchain():
    '''
    This class contains all the blockchain functions with
    the list of blocks, instance this class once to create
    the blockchain
    '''
    def __init__(self):
        '''
        This is the constructor of the blockchain
        :param blockchain: receives a list of blocks
        :type blockchain: list
        :param amount: the amount of crypto money in the blockchain
        :type amount: int
        '''
        self.blockchain =  []
        self.hash_blockchain = ''
        self.amount = 0
        self.block_instanted = Block()
        self.public_ledger = []
        self.generator_wallets = Wallet()
    
    def __str__(self):
        '''
        toString function for Blockchain
        '''
        lista_bloques = []
        for block in self.blockchain:
            lista_bloques.append(block.__str__())

        return  {'blockchain':lista_bloques, 'Cantidad':len(self.blockchain)}     

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
        if not self.verify_block_length():
            self.block_instanted.add_transaction(transaction)
            if(self.verify_block_length()):
                self.close_block()
                self.add_new_block()
            
        return {'status_transaction':1,
                'Transaction':transaction.__dict__,
                }
    
    def verify_block_length(self):
        '''
        This function verify the block length
        '''
       
        return (len(self.block_instanted.transactions) == 3)
        
    def close_block(self):
        '''
        This function receives a response from OpenCloser across Coordinator
        and close the block, adding the nonce with the hashes, only if this is full. 
        '''
        
        request_tempo = self.block_instanted.__str__()
        jsonify()
        print("Enviando",request_tempo)
        services = Services()
        hash_actual = services.service_close_block(request_tempo)
        print("Recibido", hash_actual)
        hash_actual = hash_actual['hash_of_the_block']
        if len(self.blockchain) == 0:
            self.block_instanted.add_hashes(hash_t = hash_actual)
        else:
            last_block = self.blockchain[len(self.blockchain)-1]
            self.block_instanted.add_hashes(last_block.hash, hash_actual)

        self.block_instanted.add_nonce()
        
    def add_new_block(self):
        '''
        This function reset the instance of block, where is going to write the
        transactions 
        '''
        self.blockchain.append(self.block_instanted)
        self.block_instanted = Block()
        self.block_instanted.transactions = []
    
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
        
    def consult_founds_wallet(address:str):
        '''
        This function allows to consult if a wallet address exists in
        the blockchain
        :param address: the address to consult
        :type address: str
        :returns:
        :rtype:
        '''
        
    def generate_wallet(self, name_user):
        '''
        This function create the wallet of the user with a name
        and a random hashed account
        :param name_user: the name of the user account
        :type name_user: str
        '''
        response = {'user':name_user, 'error':'User Exists'}
        
        if not self.user_exists(name_user):
            new_account = self.generator_wallets.generate_new_wallet()
            new_user = {'user':name_user,'account':new_account}
            self.public_ledger.append(new_user)
            response = new_user

        return response 
    
    def user_exists(self,user):

        '''
        This function search a user in public ledger
        :param user: user to search
        :returns:
        :rtype: boolean
        '''
        for user_account in self.public_ledger:
            if user_account['user'] == user:
                return True 
        return False
    
    def users(self):
        '''
        Return a dictionary of users on the public ledger
        :returns: the public ledger
        :rtype: list
        '''
        return self.public_ledger