# import the libraries required for cryptography
import crypt
import cryptography
import hashlib

# importing date for measuring the time when the block was added to the Blockchain.
import datetime

# Note: everything will be serialized to string!


# this is the class that defines a particular block of the blockchain
class Block:
    def __init__(self,index, transaction,prevHash=""):
        self.index = index
        self.prevHash = prevHash
        self.transaction = transaction
        self.nonce = 0
        self.blockHash = self.calculateHash()
        self.time = datetime.datetime.now()
       
    def calculateHash(self):
        return hashlib.sha256(str(str(self.index) + self.prevHash + str(self.transaction)+ str(self.nonce)).encode()).hexdigest()
    

    #mining the block, else any spammer can create multiple blocks without validation!!

    def mineBlock(self):
        while (self.blockHash[0:4]!="0000"):
            self.nonce +=1
            self.blockHash = self.calculateHash()


# this is the class that defines the blockchain
class BlockChain:
    
    def __init__(self):
        # only property of the blockchain is the chain
        self.chain = [self.createGenesis()]
    
    
    # the first block of the blockchain should be added mannualy
    def createGenesis(self):
        return Block(0, "Genesis")

    # function to get the latest block
    def getLatestBlock(self):
        return self.chain[-1]  

#  function to add blocks to the blockchain
    def addBlock(self, newBlock):
        newBlock.prevHash = self.getLatestBlock().blockHash
        newBlock.mineBlock()
        self.chain.append(newBlock)

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


# Define DinkuCoin
DinkuCoin = BlockChain()

# transaction 1
print("Mining block 1")
DinkuCoin.addBlock(Block(1,{"amount": 100}))
print(DinkuCoin.chain[1].blockHash)

# transaction 2
print("Mingng Block 2")
DinkuCoin.addBlock(Block(2,{"amount": 100}))
print(DinkuCoin.chain[2].blockHash)

# Check if Dinkucoin is valid
print("Is Dinku Coin valid?",DinkuCoin.isValid())