
import  tkinter as tk #this creates the GUI
from tkinter import  filedialog, Text  #filedialog picks the app, text helps to display some text
import os


root = tk.Tk() #the root is like the htmlwhich holds the entire application. whenever you want to attach a btn you do it here.

apps = []

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read()
        #print(tempApps)
        #apps = tempApps.split(',')
        #print(apps)
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addapps(): #This creates a function that when invoked opens up the files directory for all executables .exe files
    for widget in frame.winfo_children(): #this deletes all the labels that were previously added to the frame to allow for the new ones
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir = "/", title = "Select File", filetypes = (("executables", "*.exe"), ("All Files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg = "gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height = 600, width = 600, bg = "#263D42")
canvas.pack() #to attach it to the root

frame = tk.Frame(root, bg = "white") #this one adds  a white frame to the middle
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1) #relx and rely make it to be centered and have equal padding

openfile = tk.Button(root, text = "open file", fg = "white", bg = "#263D42", padx = 10, pady = 5, command = addapps )
openfile.pack()

runapps = tk.Button(root, text = "Run Apps", fg = "white", bg = "#263D42", padx = 10, pady = 5, command = runApps)
runapps.pack()

for app in apps: #what this for loop does is makes sure that when we reopen our app, it displays the files stored in the
    #save.txt file on the frame
    label = tk.Label(frame, text = app)
    label.pack()


root.mainloop()

with open('save.txt','w') as f: #when we close our GUI app i want my apps that are in the frame stored here.
    for app in apps: #this so that i dont forget which app directory i was at before closing my application.
        f.write(app + ',')





