from cgitb import text
import tkinter as tk

from UtilityClasses import TaaCoin
from blockchain import Transaction

def makeTransactionPage(user):
    root= tk.Tk()
    root.geometry("500x500")
    tk.Label(root,text="add transaction pop up").pack()
    tk.Label(root,text=("sender address: "+ user.id)).pack()
    if(TaaCoin.checkIfUserHasPendingTransanctions(user.id)):
        tk.Label(root,text="please wait untill your pending transanctions are processed").pack() 
    else:
        inp= tk.Entry(root, width=50, borderwidth=3)
        inp.pack()
        amount = tk.Entry(root,width=50, borderwidth=3)
        amount.pack()
        button =tk.Button(root,text="make transaction",command= lambda: TaaCoin.createTransaction(Transaction(user.id,inp.get(),int(amount.get()))))
        button.pack()
    root.mainloop()

def mineTransactions(user,updateComponent):
    root= tk.Tk()
    root.geometry("500x500")
    tk.Label(root,text="We love you for maintaining the network!!").pack()
    tk.Label(root,text="mining!!").pack()
    TaaCoin.minePendingTransactions(user.id)
    tk.Label(root,text="done mining!!").pack()
    user.balance = TaaCoin.getBalanceof(user.id)
    tk.Label(root,text=("as a token of appreciation we added"+str(TaaCoin.miningReward)+"to your account")).pack()
    print(user.balance)
    updateComponent.config(text=("Balance:"+str(user.balance)))
    root.mainloop()
    