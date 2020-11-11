# ---------------  YouTube Downloader  -------------- #
# author: Sayed Mohammad Rezaie -- 10.Nov.2020
# github: @cdied --- email: cdiedwbh@gmail.com

# --------------------  imports  -------------------- #
from tkinter import *
import pytube
import subprocess

# -------------------  Functions  ------------------- #
def download():
    link = str(entry.get())
    yt = pytube.YouTube(link)
    stream = yt.streams.get_highest_resolution()
    stream.download(".\\Downloads")

    entry.delete(0, END)
    
    Label(frame, text="Video Downloaded Succsesfully", background="#1A3D56", foreground="green", font=("Arial", 12)).place(relx=0.5, rely=0.6, anchor=CENTER)
    button = Button(frame, text="Open in File Explorer", command=lambda:opendir())
    button.place(relx=0.5, rely=0.8, width=130, height=30, anchor=CENTER)
    

def opendir():
    subprocess.call("explorer .\\Downloads", shell=True)

# ---------  GUI(Graphical user interface)  --------- #
root = Tk()
root.title("YouTube Downloader")
root.geometry("500x250")

frame = Frame(root, background="#1A3D56", width=5000, height=3200)
frame.pack(expand=True)

entry_lable = Label(frame, text="Enter a URL", background="#1A3D56", foreground="white")
entry_lable.place(relx = 0.05, rely = 0.1, height=30)

entry = Entry(frame)
entry.place(relx = 0.25, rely = 0.1, width=340, height=30)

button = Button(frame, text="Download", command=lambda:download())
button.place(relx=0.5, rely=0.4, width=100, height=30, anchor=CENTER)


root.mainloop()
