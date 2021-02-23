import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess

root = tk.Tk()
apps = []

with open('save.txt', 'r') as f:
    lines = f.read() 
    apps = [app.strip() for app in lines.split(',')]
    print(apps)

def show_apps():
    for app in apps:
        label = tk.Label(frame, text=app, bg="grey")
        label.pack()



def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File")
    apps.append(filename)
    show_apps()

def runApps():
    for app in apps:
        print(app)
        subprocess.call(app)


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

show_apps()

runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg="white", bg="#263D42", command=runApps)

runApps.pack()


root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
