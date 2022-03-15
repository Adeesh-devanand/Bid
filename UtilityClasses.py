# utilityclasses.py

from blockchain import BlockChain


class User:
    def __init__(self, id):
        self.id = id
        self.balance= TaaCoin.getBalanceof(id)
        
TaaCoin= BlockChain()
