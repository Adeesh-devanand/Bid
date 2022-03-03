import tkinter as tk
from PIL import Image, ImageTk
from UtilityClasses import TaaCoin

from components import makeTransactionPage, mineTransactions



def Home_page(user):
    root = tk.Tk()

    canvas = tk.Canvas(root, height=700, width=800)
    canvas.pack()

    background_image = ImageTk.PhotoImage(Image.open("assets/landscape.png"))
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)



    frame1_border = tk.Frame(root, bg="#315a6e")
    frame1_border.place(relheight=0.57, relwidth=0.39, relx=0.1, rely=0.1)

    frame1 = tk.Frame(frame1_border, bg = "#AEB6BF")
    frame1.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)

    usericon_image = ImageTk.PhotoImage(Image.open("assets/User-Icon-White.png").resize((100, 100)))
    usericon_label = tk.Label(frame1, image=usericon_image, bg="#AEB6BF")
    usericon_label.place(relx = 0.3, rely = 0, relheight= 0.4, relwidth = 0.4)

    username = tk.Label(frame1, text=(" Username:"+user.id), bg = "#AEB6BF")
    username.config(font =("Courier", 11))
    username.place(relx = 0, rely = 0.4, relheight= 0.1, )

    unique_ID = tk.Label(frame1, text="  Unique ID:", bg = "#AEB6BF", font =("Courier", 11))
    unique_ID.place(relx = 0, rely = 0.5, relheight= 0.1, relwidth = 0.4)

    balance = tk.Label(frame1, text=("Balance:"+str(user.balance)), bg = "#AEB6BF", font =("Courier", 11))
    balance.place(relx = 0, rely = 0.6, relheight= 0.1)

    refresh = tk.Button(frame1, text = "Refresh", bg="#D6DBDF", font =("Courier", 8))
    refresh.place(relx = 0.075, rely = 0.9, relheight= 0.05, relwidth = 0.4)


    logout = tk.Button(frame1, text = "Log out", bg= "#D6DBDF", font =("Courier", 8))
    logout.place(relx = 0.55, rely = 0.9, relheight= 0.05, relwidth = 0.4)


    frame2_border = tk.Frame(root, bg="#315a6e")
    frame2_border.place(relheight=0.35, relwidth=0.35, relx=0.55, rely=0.1)

    frame2 = tk.Frame(frame2_border, bg = "#AEB6BF")
    frame2.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)

    make_transaction = tk.Button(frame2, text = "Make Transaction", bg= "#D6DBDF", font =("Courier", 11), command=lambda:makeTransactionPage(user))
    make_transaction.place(relx = 0.1, rely = 0.05, relheight= 0.4, relwidth = 0.8)

    
    mine_transactions = tk.Button(frame2, text = "Mine Taa Coins", bg= "#D6DBDF", font =("Courier", 11), command= lambda: mineTransactions(user,balance))
    mine_transactions.place(relx = 0.1, rely = 0.55, relheight= 0.4, relwidth = 0.8)

    frame3_border = tk.Frame(root, bg="#315a6e")
    frame3_border.place(relheight=0.2, relwidth=0.8, relx=0.1, rely=0.75)

    frame3 = tk.Frame(frame3_border, bg = "#AEB6BF")
    frame3.place(relheight=0.8, relwidth=0.95, relx=0.025, rely=0.1)

    transaction_history = tk.Label(frame3, bg= "#D6DBDF", font =("Courier", 11), text="Transaction History")
    transaction_history.place(relx = 0.3, rely = 0.1, relheight= 0.15, relwidth = 0.4)


    root.mainloop()
