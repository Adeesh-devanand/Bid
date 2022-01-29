import tkinter as tk

from frontend.FrontendUtils import clearRoot

class AuthScreen:
    def __init__(self, root):
        self.root = root

    def loginScreen(self):
            
        tk.Label(self.root,text="enter public key",).pack()
        pb = tk.Text(self.root,borderwidth=2,height=2, width=40).pack()

        tk.Label(self.root,text="enter private key").pack()
        pv = tk.Text(self.root,borderwidth=2, height=2, width=40).pack()

        button = tk.Button(self.root,text="Login").pack()

        tk.Label(self.root,text="or").pack()
        button = tk.Button(self.root,text="sign up", command= self.signupScreen).pack()



    def signupScreen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="enter your name").pack()
        pb = tk.Text(self.root,borderwidth=2,height=2, width=40).pack()

        tk.Label(self.root, text="enter adhaar number").pack()
        adhaar = tk.Text(self.root,borderwidth=2,height=2, width=40).pack()

        tk.Label(self.root, text="enter address").pack()
        address = tk.Text(self.root,borderwidth=2,height=2, width=40).pack()

        tk.Label(self.root, text="enter officer public key").pack()
        opb = tk.Text(self.root,borderwidth=2,height=2, width=40).pack()

        signup = tk.Button(self.root, text="sign up").pack()
        
