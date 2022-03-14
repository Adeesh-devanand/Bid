import tkinter as tk
from PIL import Image, ImageTk
from Database import CreateUser, checkIfUserExists, login
from UtilityClasses import TaaCoin, User
from blockchain import Transaction
from components import makeTransactionPage, mineTransactions
import mysql.connector as c

root = tk.Tk()

usericon_imageH = ImageTk.PhotoImage(Image.open("assets/User-Icon-White.png").resize((100, 100)))
usericon_imageL = ImageTk.PhotoImage(Image.open("assets/User-Icon-White.png").resize((100, 100)))
background_image = ImageTk.PhotoImage(Image.open("assets/landscape.png").resize((int(2488/1.8), int(1400/1.8))))

frames = {}
framesDim = {}

db= c.connect(host="localhost", user="root", passwd="Development16")
mc=db.cursor()
mc.execute("create database if not exists bid")
mc .execute("use bid")

try:
    mc.execute("create table user(id int primary key AUTO_INCREMENT,name varchar(15),password varchar(255))")
    db.commit()
except:
    print("table already created")


def create_frame(fType):
   frame = frames[fType]
   dim = framesDim[fType]
   frame.place(relx=dim[0], rely=dim[1], relheight=dim[2], relwidth=dim[3])

# Login frame
def initialize_login():

    def create_home():
         username, password = username_entryL.get(), password_entryL.get()
         if(checkIfUserExists(username, mc)):
            if(login(username,password, mc)):
               user= User(username)
               initialize_home(user)
               login_frame.place_forget()
               create_frame("H-frame-1")
               create_frame("H-frame-2")
               create_frame("H-frame-3")
         else:
            create_frame("invalid-User")

        
    login_frame = tk.Frame(root)
    frames["login"] = login_frame
    framesDim["login"] = (0.25, 0.2, 0.6, 0.5)
    
    usericon_labelL = tk.Label(login_frame, image=usericon_imageL)
    usericon_labelL.place(relx = 0.35, rely = 0.15, relheight= 0.3, relwidth = 0.3)

    username_entryL = tk.Entry(login_frame, fg='#B3B6B7')
    username_entryL.place(relx=0.1, relwidth= 0.8, rely = 0.57, relheight=0.1 )
    username_entryL.insert(0, 'username')

    password_entryL = tk.Entry(login_frame, fg='#B3B6B7')
    password_entryL.place(relx=0.1, relwidth= 0.8, rely = 0.72, relheight=0.1 )
    password_entryL.insert(0, 'password')
<<<<<<< HEAD
=======


>>>>>>> 754fb182af530d6d5e61658d06c4833bf1efc415

    signUp = tk.Button(login_frame, text = "Sign up", bg="#D6DBDF", font =("Courier", 8), command = lambda: create_frame("signup"))
    signUp.place(relx = 0.7, rely = 0.85, relheight= 0.03, relwidth = 0.2)

    Login = tk.Button(login_frame, text = "Login", bg="#315a6e", font =("Courier", 8), command=create_home)
    Login.place(relx = 0.4, rely = 0.85, relheight= 0.075, relwidth = 0.15)

# Signup frame
def initialize_signup():


   def create_user():
      username, password, confirm_password = username_entryS.get(), password_entryS.get(), password_entryS1.get()
      if password == confirm_password:   
         CreateUser(username,password, mc)
         if(login(username,password, mc)):
            User(username)
         create_frame("Created-User")
      else:
         create_frame("nonMatching-pass")

   signup_frame = tk.Frame(root)
   frames["signup"] = signup_frame
   framesDim["signup"] = (0.25, 0.2, 0.6, 0.5)

   username_entryS = tk.Entry(signup_frame, fg='#B3B6B7')
   username_entryS.insert(0, 'username')
   username_entryS.place(relx=0.1, relwidth= 0.8, rely = 0.25, relheight=0.1 )
<<<<<<< HEAD

=======
   
>>>>>>> 754fb182af530d6d5e61658d06c4833bf1efc415
   password_entryS = tk.Entry(signup_frame, fg='#B3B6B7')
   password_entryS.insert(0, 'password')
   password_entryS.place(relx=0.1, relwidth= 0.8, rely = 0.45, relheight=0.1 )

   password_entryS1 = tk.Entry(signup_frame, fg='#B3B6B7')
   password_entryS1.insert(0, 'confirm password')
   password_entryS1.place(relx=0.1, relwidth= 0.8, rely = 0.65, relheight=0.1 )
<<<<<<< HEAD
=======





>>>>>>> 754fb182af530d6d5e61658d06c4833bf1efc415


   createAcc = tk.Button(signup_frame, text = "Create account", bg="#D6DBDF", font =("Courier", 8), command=create_user)
   createAcc.place(relx = 0.3, rely = 0.88, relheight= 0.06, relwidth = 0.4)

   back = tk.Button(signup_frame, text = "<<", bg="#CB4335", font =("Courier", 8), command=signup_frame.place_forget)
   back.place(relx = 0.1, rely = 0.88, relheight= 0.06, relwidth = 0.08)

# Created-User frame
def initialize_createdU():

   createdU_frame = tk.Frame(root, bg="#315a6e")
   frames["Created-User"] = createdU_frame
   framesDim["Created-User"] = (0.3, 0.4, 0.2, 0.4)

   frame1 = tk.Frame(createdU_frame)
   frame1.place(relx=0.025, rely=0.05, relheight=0.9, relwidth=0.95)

   ok = tk.Button(frame1, text = "OK", bg="#CB4335", font =("Courier", 8), command=createdU_frame.place_forget)
   ok.place(relx = 0.25, rely = 0.43, relheight= 0.33, relwidth = 0.5)

   Success = tk.Label(frame1, text="  Created Account Successfully!")
   Success.config(font =("Courier", 11))
   Success.place(relx = 0.05, rely = 0.2, relheight= 0.15, relwidth = 0.9)

# Invalid-User frame
def initialize_invalidU():

   invalidU_frame = tk.Frame(root, bg="#315a6e")
   frames["invalid-User"] = invalidU_frame
   framesDim["invalid-User"] = (0.3, 0.4, 0.2, 0.4)

   frame1 = tk.Frame(invalidU_frame)
   frame1.place(relx=0.025, rely=0.05, relheight=0.9, relwidth=0.95)

   ok = tk.Button(frame1, text = "OK", bg="#CB4335", font =("Courier", 8), command=invalidU_frame.place_forget)
   ok.place(relx = 0.25, rely = 0.43, relheight= 0.33, relwidth = 0.5)

   Success = tk.Label(frame1, text="Invalid Account")
   Success.config(font =("Courier", 11))
   Success.place(relx = 0.05, rely = 0.2, relheight= 0.15, relwidth = 0.9)

# Invalid-passsword frame
def initialize_invalidP():

   invalidP_frame = tk.Frame(root, bg="#315a6e")
   frames["invalid-passwod"] = invalidP_frame
   framesDim["invalid-password"] = (0.3, 0.4, 0.2, 0.4)

   frame1 = tk.Frame(invalidP_frame)
   frame1.place(relx=0.025, rely=0.05, relheight=0.9, relwidth=0.95)

   ok = tk.Button(frame1, text = "OK", bg="#CB4335", font =("Courier", 8), command=invalidP_frame.place_forget)
   ok.place(relx = 0.25, rely = 0.43, relheight= 0.33, relwidth = 0.5)

   Success = tk.Label(frame1, text="Invalid Password")
   Success.config(font =("Courier", 11))
   Success.place(relx = 0.05, rely = 0.2, relheight= 0.15, relwidth = 0.9)

# nonMatching-pass frame
def initialize_nonMatching_pass():

   nonMatching_pass_frame = tk.Frame(root, bg="#315a6e")
   frames["nonMatching-pass"] = nonMatching_pass_frame
   framesDim["nonMatching-pass"] = (0.3, 0.4, 0.2, 0.4)

   frame1 = tk.Frame(nonMatching_pass_frame)
   frame1.place(relx=0.025, rely=0.05, relheight=0.9, relwidth=0.95)

   ok = tk.Button(frame1, text = "OK", bg="#CB4335", font =("Courier", 8), command=nonMatching_pass_frame.place_forget)
   ok.place(relx = 0.25, rely = 0.43, relheight= 0.33, relwidth = 0.5)

   Success = tk.Label(frame1, text="Passwords don't match")
   Success.config(font =("Courier", 11))
   Success.place(relx = 0.05, rely = 0.2, relheight= 0.15, relwidth = 0.9)
   
# Home Page frames
def initialize_home(user):
   # frame 1
   def logout():
      frame1_borderH.place_forget()
      frame2_borderH.place_forget()
      frame3_borderH.place_forget()
      create_frame("login")
   

   frame1_borderH = tk.Frame(root, bg="#315a6e")
   frames["H-frame-1"] = frame1_borderH
   framesDim["H-frame-1"] = (0.1, 0.1, 0.57, 0.39)

   frame1H = tk.Frame(frame1_borderH, bg = "#AEB6BF")
   frame1H.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)

   usericon_labelL = tk.Label(frame1H, image=usericon_imageH, bg="#AEB6BF")
   usericon_labelL.place(relx = 0.3, rely = 0, relheight= 0.4, relwidth = 0.4)

   username = tk.Label(frame1H, text=(" Username: "+user.id), bg = "#AEB6BF")
   username.config(font =("Courier", 11))
   username.place(relx = 0, rely = 0.4, relheight= 0.1)

<<<<<<< HEAD
=======
   
>>>>>>> 754fb182af530d6d5e61658d06c4833bf1efc415
   balance = tk.Label(frame1H, text=("Balance:"+str(user.balance)), bg = "#AEB6BF", font =("Courier", 11))
   balance.place(relx = 0.03, rely = 0.6, relheight= 0.1)

   logoutB = tk.Button(frame1H, text = "Log out", bg= "#D6DBDF", font =("Courier", 8), command=logout)
   logoutB.place(relx = 0.3, rely = 0.9, relheight= 0.05, relwidth = 0.4)

   # frame 2
   def make_transaction():
      makeTransactionPage(root, user)

   def mine_transactions():
      mineTransactions(root, user, balance)

   frame2_borderH = tk.Frame(root, bg="#315a6e")
   frames["H-frame-2"] = frame2_borderH
   framesDim["H-frame-2"] = (0.1, 0.75, 0.2, 0.39)

   frame2 = tk.Frame(frame2_borderH, bg = "#AEB6BF")
   frame2.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)

   make_transactionB = tk.Button(frame2, text = "Make Transaction", bg= "#D6DBDF", font =("Courier", 11), command=make_transaction)
   make_transactionB.place(relx = 0.1, rely = 0.05, relheight= 0.4, relwidth = 0.8)

   mine_transactionsB = tk.Button(frame2, text = "Mine Dk Coins", bg= "#D6DBDF", font =("Courier", 11), command=mine_transactions)
   mine_transactionsB.place(relx = 0.1, rely = 0.55, relheight= 0.4, relwidth = 0.8)

   # frame 3
   def refresh():
      transactions = TaaCoin.getUserTransactionHistory(user.id)

      history = ""
      for transaction in transactions:
         history += transaction.senderAddress + " " + transaction.recAddress + " " + str(transaction.amount) + "\n"
      
      transaction_history.config(text=history)


   frame3_borderH = tk.Frame(root, bg="#315a6e")
   frames["H-frame-3"] = frame3_borderH
   framesDim["H-frame-3"] = (0.55, 0.1, 0.78, 0.39)

   frame3 = tk.Frame(frame3_borderH, bg = "#AEB6BF")
   frame3.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)

   title = tk.Label(frame3, bg= "#AEB6BF", font =("Courier", 11), text="Transaction History")
   title.place(relx = 0.15, rely = 0.1, relheight= 0.15, relwidth = 0.7)

   transaction_history = tk.Label(frame3, bg= "#AEB6BF", font =("Courier", 10), text="")
   transaction_history.place(relx = 0.15, rely = 0.35, relwidth = 0.7)


   refreshB = tk.Button(frame3, text = "Refresh", bg="#D6DBDF", font =("Courier", 8), command=refresh)
   refreshB.place(relx = 0.35, rely = 0.9, relheight= 0.05, relwidth = 0.3)


def main():
    TaaCoin.createTransaction(Transaction("Genesis","chandan",1000))
    TaaCoin.createTransaction(Transaction("Genesis","adeesh",1000))
    TaaCoin.createTransaction(Transaction("Genesis","Elon",1000))
    canvas = tk.Canvas(root, height=700, width=800)
    canvas.pack()

    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    initialize_login()
    initialize_signup()
    initialize_createdU()
    initialize_invalidU()
    initialize_invalidP()
    initialize_nonMatching_pass()
    create_frame("login")

    root.mainloop()

main()