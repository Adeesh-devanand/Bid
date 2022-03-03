# import the libraries required for cryptography
import hashlib

# importing date for measuring the time when the block was added to the Blockchain.
import datetime

# Note: everything will be serialized to string!

# Lets define a Transaction

class Transaction:
    def __init__(self, senderAdderess, recAddress, amount):
        self.time = datetime.datetime.now()
        self.senderAddress = senderAdderess
        self.recAddress = recAddress
        self.amount = amount

# this is the class that defines a particular block of the blockchain
class Block:
    def __init__(self, transactions,prevHash=""):
        self.prevHash = prevHash
        self.transactions = transactions
        self.nonce = 0
        self.blockHash = self.calculateHash()
        self.time = datetime.datetime.now()
       
    def calculateHash(self):
        return hashlib.sha256(str( self.prevHash + str(self.transactions)+ str(self.nonce)).encode()).hexdigest()
    

    #mining the block, else any spammer can create multiple blocks without validation!!

    def mineBlock(self):
        while (self.blockHash[0:4]!="0000"):
            self.nonce +=1
            self.blockHash = self.calculateHash()

        #adeesh+nonce => adjfnkldjfmal;dsjfads ==> 0000kdsfnkadnfklsn


# this is the class that defines the blockchain
class BlockChain:
    
    def __init__(self):

        # only property of the blockchain is the chain
        self.chain = [self.createGenesis()]
        self.peningTransactions = []
        self.miningReward = 100
      
    

    # the first block of the blockchain should be added mannualy
    def createGenesis(self):
        return Block([Transaction("Genesis", "Genesis",21000000000)], "Genesis")


    # function to get the latest block
    def getLatestBlock(self):
        return self.chain[-1]  

    # Mining pending transactions and add the block!
    def minePendingTransactions(self, reciverAddress):
        newBlock = Block( self.peningTransactions, self.getLatestBlock().blockHash)
        newBlock.mineBlock()
        self.chain.append(newBlock)
        self.peningTransactions = [Transaction("Genesis",reciverAddress,self.miningReward)]
    
    # verifying the blockchain
    def isValid(self):
        for i in range(1,len(self.chain)):
            currentBlock = self.chain[i]
            prevBlock = self.chain[i-1]
            # check if the blockHash is valid and has not been tampered
            if(currentBlock.blockHash != currentBlock.calculateHash()):
                return False, "hash issue", i
            
            if(currentBlock.prevHash != prevBlock.blockHash):
                return False, "chain issue"

        return True
    
    def createTransaction(self,transaction):
        if(transaction.amount>self.getBalanceof(transaction.senderAddress)):
            print("you a broke piece of shit")
            return False
        self.peningTransactions.append(transaction)
        return True

    # get the current balance of an account
    def getBalanceof(self, address):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if(transaction.senderAddress == address):
                    balance -= transaction.amount
                if(transaction.recAddress == address):
                    balance += transaction.amount
        return balance
            
    def getUserTransactionHistory(self,user):
        a=[]
        for blocks in self.chain:
            for transaction in blocks.transactions:
                if (transaction.senderAddress == user or transaction.recAddress == user):
                    a.append(transaction)
                
        return a
    def checkIfUserHasPendingTransanctions(self,user):
        for transanction in self.peningTransactions:
            if(transanction.senderAddress== user):
                return True
        return False