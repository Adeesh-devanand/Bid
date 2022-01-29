import tkinter as tk
import frontend.login

root = tk.Tk()
frame =frontend.login.AuthScreen(root)
frame.loginScreen()

root.mainloop()