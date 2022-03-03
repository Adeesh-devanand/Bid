from glob import glob
from Home_Page import Home_page
from UtilityClasses import *
from blockchain import *

print("welcome to the TAA Network!!")
user = User("chandan")
Home_page(user)

# while True:
#     print("#################################################")
#     print("1. create transaction")
#     print("2. get Balance of")
#     print("3. check pending transactions")
#     print("4. mine!!!")
#     print("5. get latest block")
#     print("6. show blockchain")
#     print("#################################################")

#     choice= int(input("enter your choice"))
#     if(choice==1):
#         TaaCoin.createTransaction(Transaction(input("enter sender address"),input("enter receiver address"),int(input("enter amount"))))
#         print("transaction created, the money will be transfered very soon")
#     elif(choice==2):
#         print(TaaCoin.getBalanceof(input("enter user id")))

#     elif(choice==3):
#         pendingT= TaaCoin.peningTransactions
#         print(TaaCoin.peningTransactions)
#         for transaction in pendingT:
#             print(transaction.senderAddress)
#     elif(choice==4):
#         print("we love you for maintaining the network!!!")
#         TaaCoin.minePendingTransactions(input("enter your id"))
#         print("you received ", TaaCoin.miningReward,"as a thank you token")
#     elif(choice==5):
#         a=TaaCoin.getLatestBlock()
#         print(a)
#     elif(choice==6):
#         print("we are still working on making the blockchain look beautiful loll")
#     else:
#         print("you had one job")

