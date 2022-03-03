import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

usericon_imageH = ImageTk.PhotoImage(Image.open("assets/User-Icon-White.png").resize((100, 100)))
usericon_imageL = ImageTk.PhotoImage(Image.open("assets/User-Icon-White.png").resize((100, 100)))
background_image = ImageTk.PhotoImage(Image.open("assets/landscape.png").resize((int(2488/1.8), int(1400/1.8))))

frames = {}
framesDim = {}

def create_frame(fType):
   frame = frames[fType]
   dim = framesDim[fType]
   frame.place(relx=dim[0], rely=dim[1], relheight=dim[2], relwidth=dim[3])

# Login frame
def initialize_login():

   def create_home():
      username, password = username_entryL.get(), password_entryL.get()
      login_frame.place_forget()
      create_frame("H-frame-1")
      create_frame("H-frame-2")
      create_frame("H-frame-3")

   login_frame = tk.Frame(root)
   frames["login"] = login_frame
   framesDim["login"] = (0.25, 0.2, 0.6, 0.5)
   
   usericon_labelL = tk.Label(login_frame, image=usericon_imageL)
   usericon_labelL.place(relx = 0.35, rely = 0.15, relheight= 0.3, relwidth = 0.3)

   username_entryL = tk.Entry(login_frame, fg='#B3B6B7')
   username_entryL.insert(0, 'username')
   username_entryL.place(relx=0.1, relwidth= 0.8, rely = 0.57, relheight=0.1 )

   password_entryL = tk.Entry(login_frame, fg='#B3B6B7')
   password_entryL.insert(0, 'password')
   password_entryL.place(relx=0.1, relwidth= 0.8, rely = 0.72, relheight=0.1 )

   signUp = tk.Button(login_frame, text = "Sign up", bg="#D6DBDF", font =("Courier", 8), command = lambda: create_frame("signup"))
   signUp.place(relx = 0.7, rely = 0.85, relheight= 0.03, relwidth = 0.2)

   Login = tk.Button(login_frame, text = "Login", bg="#315a6e", font =("Courier", 8), command=create_home)
   Login.place(relx = 0.4, rely = 0.85, relheight= 0.075, relwidth = 0.15) 

# Signup frame
def initialize_signup():

   def create_user():
      username, password = username_entryS.get(), password_entryS.get()
      create_frame("Created-User")

   signup_frame = tk.Frame(root)
   frames["signup"] = signup_frame
   framesDim["signup"] = (0.25, 0.2, 0.6, 0.5)

   username_entryS = tk.Entry(signup_frame, fg='#B3B6B7')
   username_entryS.insert(0, 'username')
   username_entryS.place(relx=0.1, relwidth= 0.8, rely = 0.25, relheight=0.1 )

   password_entryS = tk.Entry(signup_frame, fg='#B3B6B7')
   password_entryS.insert(0, 'password')
   password_entryS.place(relx=0.1, relwidth= 0.8, rely = 0.45, relheight=0.1 )

   password_entryS1 = tk.Entry(signup_frame, fg='#B3B6B7')
   password_entryS1.insert(0, 'confirm password')
   password_entryS1.place(relx=0.1, relwidth= 0.8, rely = 0.65, relheight=0.1 )

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
   
# Home Page frames
def initialize_home():

   # frame 1
   def logout():
      frame1_borderH.place_forget()
      frame2_borderH.place_forget()
      frame3_borderH.place_forget()
      create_frame("login")
   
   def refresh():
      pass

   frame1_borderH = tk.Frame(root, bg="#315a6e")
   frames["H-frame-1"] = frame1_borderH
   framesDim["H-frame-1"] = (0.1, 0.1, 0.57, 0.39)

   frame1H = tk.Frame(frame1_borderH, bg = "#AEB6BF")
   frame1H.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)

   usericon_labelL = tk.Label(frame1H, image=usericon_imageH, bg="#AEB6BF")
   usericon_labelL.place(relx = 0.3, rely = 0, relheight= 0.4, relwidth = 0.4)

   username = tk.Label(frame1H, text=" Username:", bg = "#AEB6BF")
   username.config(font =("Courier", 11))
   username.place(relx = 0, rely = 0.4, relheight= 0.1, relwidth = 0.4)

   unique_ID = tk.Label(frame1H, text="  Unique ID:", bg = "#AEB6BF", font =("Courier", 11))
   unique_ID.place(relx = 0, rely = 0.5, relheight= 0.1, relwidth = 0.4)

   balance = tk.Label(frame1H, text="Balance:", bg = "#AEB6BF", font =("Courier", 11))
   balance.place(relx = 0, rely = 0.6, relheight= 0.1, relwidth = 0.4)

   refreshB = tk.Button(frame1H, text = "Refresh", bg="#D6DBDF", font =("Courier", 8), command=refresh)
   refreshB.place(relx = 0.075, rely = 0.9, relheight= 0.05, relwidth = 0.4)


   logoutB = tk.Button(frame1H, text = "Log out", bg= "#D6DBDF", font =("Courier", 8), command=logout)
   logoutB.place(relx = 0.55, rely = 0.9, relheight= 0.05, relwidth = 0.4)

   # frame 2
   def make_transaction():
      pass

   def mine_transactions():
      pass

   frame2_borderH = tk.Frame(root, bg="#315a6e")
   frames["H-frame-2"] = frame2_borderH
   framesDim["H-frame-2"] = (0.55, 0.1, 0.35, 0.35)

   frame2 = tk.Frame(frame2_borderH, bg = "#AEB6BF")
   frame2.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)

   make_transactionB = tk.Button(frame2, text = "Make Transaction", bg= "#D6DBDF", font =("Courier", 11), command=make_transaction)
   make_transactionB.place(relx = 0.1, rely = 0.05, relheight= 0.4, relwidth = 0.8)

   mine_transactionsB = tk.Button(frame2, text = "Mine Dk Coins", bg= "#D6DBDF", font =("Courier", 11), command=mine_transactions)
   mine_transactionsB.place(relx = 0.1, rely = 0.55, relheight= 0.4, relwidth = 0.8)

   # frame 3
   frame3_borderH = tk.Frame(root, bg="#315a6e")
   frames["H-frame-3"] = frame3_borderH
   framesDim["H-frame-3"] = (0.1, 0.75, 0.2, 0.8)

   frame3 = tk.Frame(frame3_borderH, bg = "#AEB6BF")
   frame3.place(relheight=0.8, relwidth=0.95, relx=0.025, rely=0.1)

   transaction_history = tk.Label(frame3, bg= "#D6DBDF", font =("Courier", 11), text="Transaction History")
   transaction_history.place(relx = 0.3, rely = 0.1, relheight= 0.15, relwidth = 0.4)

def main():
   canvas = tk.Canvas(root, height=700, width=800)
   canvas.pack()

   background_label = tk.Label(root, image=background_image)
   background_label.place(x=0, y=0, relwidth=1, relheight=1)

   initialize_login()
   initialize_signup()
   initialize_createdU()
   initialize_home()

   create_frame("login")
   root.mainloop()

main()
