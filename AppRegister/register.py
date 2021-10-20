'''
Register: Register class
-----------------------------

This module contains the class register
with the functions required for validate
the transactions
'''

from service import Services
class Register():
    '''
    The class Register is the responsible of
    validate the transactions and the stuff related
    with make the confirmations
    '''
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def register_transaction(wallet_from:str, wallet_to:str, amount:int):
        '''
        This function redirect to the consume for all the required
        web service to validate the transaction
        :param wallet_from: the wallet who sends the money
        :type wallet_from: str
        :param wallet_to: the wallet who receives the money
        :type wallet_to: str
        :param amount: the amount of money
        :type amount: int
        :returns: the transaction validation
        :rtype: dict
        '''
        servicies  = Services()
        wallet_format_from = {'wallet':wallet_from}
        information_wallet_from = servicies.consume_consult_founds(wallet_format_from) #{'content': 'content':
        print("WALLET",information_wallet_from)
        wallet_format_to = {'wallet': wallet_to}
        information_wallet_to = servicies.consume_consult_founds(wallet_format_to) 
        print("WALLET",information_wallet_to)
        transaction = {
                        'from_wallet':wallet_from,
                        'to_wallet':wallet_to,
                        'amount': amount
                        }
        response_t = {
                    'transaction_valid': False,
                    'error': 'No error',
                    'transaction_done': False ,
                    'transaction': transaction
                    }
        
        error_message = ''
        amount = int(amount)
        if information_wallet_from['exists'] == True and information_wallet_to['exists'] == True :
            print("WF_A",type(information_wallet_from['amount']))
            print("amount", type(amount))
            if information_wallet_from['amount'] >= amount and amount > -1:
                response_t['transaction_valid'] = True
                status_transaction = servicies.consume_register_data(transaction)
                print("Status transaction",status_transaction)

                if status_transaction['status_transaction'] == 1:
                    response_t['transaction_done'] = True
                else:
                    error_message += "Transaction fail, " 
            #Realiza transaccion
            else:
                error_message += "The amount doesn't exist, "        
        else:
            error_message += "Any of the wallets doesn't exists, "
            
        response_t['error'] = error_message
        return response_t


