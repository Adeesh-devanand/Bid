import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=800)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open("assets/landscape.png").resize((int(2488/1.8), int(1400/1.8))))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root)
frame.place(relheight=0.6, relwidth=0.5, relx=0.25, rely=0.2)

usericon_image = ImageTk.PhotoImage(Image.open("assets/User-Icon-White.png").resize((100, 100)))
usericon_label = tk.Label(frame, image=usericon_image)
usericon_label.place(relx = 0.35, rely = 0.15, relheight= 0.3, relwidth = 0.3)

def click1(event):
   username_entry.configure(state='normal')
   username_entry.delete(0, 'end')
   username_entry.unbind('<Button-1>', clicked1)

username_entry = tk.Entry(frame, fg='#B3B6B7')
username_entry.insert(0, 'username')
username_entry.place(relx=0.1, relwidth= 0.8, rely = 0.57, relheight=0.1 )

clicked1 = username_entry.bind('<Button-1>', click1)


def click2(event):
   password_entry.configure(state='normal')
   password_entry.delete(0, 'end')
   password_entry.unbind('<Button-1>', clicked2)

password_entry = tk.Entry(frame, fg='#B3B6B7')
password_entry.insert(0, 'password')
password_entry.place(relx=0.1, relwidth= 0.8, rely = 0.72, relheight=0.1 )

clicked2 = password_entry.bind('<Button-1>', click2)

root.mainloop()