import tkinter as tk

from UtilityClasses import TaaCoin
from blockchain import Transaction

def makeTransactionPage(root, user):
    def transact():
        TaaCoin.createTransaction(Transaction(user.id,inp.get(),int(amount.get())))
        makeTransaction.place_forget()

    makeTransaction = tk.Frame(root, bg="#315a6e")
    makeTransaction.place(relx = 0.25, rely = 0.43, relheight= 0.33, relwidth = 0.5)

    frame1 = tk.Frame(makeTransaction)
    frame1.place(relx=0.025, rely=0.05, relheight=0.9, relwidth=0.95)

    back = tk.Button(frame1, text = "<<", bg="#CB4335", font =("Courier", 8), command=makeTransaction.place_forget)
    back.place(relx = 0.1, rely = 0.88, relheight= 0.06, relwidth = 0.08)

    tk.Label(frame1,text=("Sender address: "+ user.id)).pack()
    if(TaaCoin.checkIfUserHasPendingTransanctions(user.id)):
        tk.Label(frame1,text="please wait until your pending transanctions are processed").pack() 
 
    else:
        inp= tk.Entry(frame1, width=50, borderwidth=3)
        inp.pack()
        amount = tk.Entry(frame1,width=50, borderwidth=3)
        amount.pack()
        confirm = tk.Button(frame1, text = "Make Transaction", bg="#CB4335", font =("Courier", 8), command=transact)
        confirm.place(relx = 0.25, rely = 0.43, relheight= 0.33, relwidth = 0.5)

    root.mainloop()

def mineTransactions(root, user, updateComponent):

    mineTransaction = tk.Frame(root, bg="#315a6e")
    mineTransaction.place(relx = 0.25, rely = 0.43, relheight= 0.33, relwidth = 0.5)

    frame1 = tk.Frame(mineTransaction)
    frame1.place(relx=0.025, rely=0.05, relheight=0.9, relwidth=0.95)

    back = tk.Button(frame1, text = "<<", bg="#CB4335", font =("Courier", 8), command=mineTransaction.place_forget)
    back.place(relx = 0.1, rely = 0.88, relheight= 0.06, relwidth = 0.08)

    tk.Label(frame1,text="We love you for maintaining the network!!").pack()
    if(len(TaaCoin.peningTransactions)<3):
        tk.Label(frame1, text= "please wait till pending transanction count reaches to 3+").pack()
        tk.Label(frame1, text="current pending transanctions: "+ str(len(TaaCoin.peningTransactions))).pack()
    else:
        tk.Label(frame1,text="mining!!").pack()
        TaaCoin.minePendingTransactions(user.id)
        tk.Label(frame1,text="done mining!!").pack()
        user.balance = TaaCoin.getBalanceof(user.id)
        tk.Label(frame1,text=("as a token of appreciation we added"+str(TaaCoin.miningReward)+"to your account")).pack()
        print(user.balance)
        updateComponent.config(text=("Balance:"+str(user.balance)))

    root.mainloop()
