import random

import connect_database
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

# set window
window = tk.Tk()
window.geometry("1000x700")
# to maximize window
# w, h = window.winfo_screenwidth(), window.winfo_screenheight()
# window.geometry("%dx%d+0+0" % (w, h))


frame_picture = tk.Frame(master=window, width=900, height=700, bg="white")

frame_toolbar = tk.Frame(master=window, width=300, height=700, bg="white")

frame_picture.pack(fill=tk.Y, side=tk.LEFT)
frame_toolbar.pack(fill=tk.Y, side=tk.RIGHT)

label = tk.Label(master=frame_toolbar, text="Toolbar           ", foreground="black")

label.pack()

path = "rpi_buildings.png"

# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
image = Image.open(path)
image = image.resize((820, 700), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
user_admin = "a"
user_password = "a"

# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
background_picture = tk.Label(frame_picture, image=img)

# The Pack geometry manager packs widgets in rows or columns.
background_picture.place(x=0, y=0, relwidth=1, relheight=1)


class Building:
    def __init__(self, name, button, people=20, capacity=100, ratio=0.2, schedule=[0, 24]):
        self.name = name
        self.people = people
        self.button = button
        self.capacity = capacity
        self.ratio = ratio
        self.schedule = schedule
        self.auto_color()

    def change_color(self, color):
<<<<<<< HEAD
        self.button.configure(background = color)#For windows system
        # self.button.configure(highlightbackground = color)#For Mac system
=======
        self.button.configure(highlightbackground=color)
        self.button.configure(bg=color)
>>>>>>> 5140f0f5676510f4f9cc79ba875bde23e5a62ff9
        self.color = color

    def auto_color(self):
        self.ratio = float(self.people) / float(self.capacity)
        if self.ratio <= 0.1:
<<<<<<< HEAD
            self.button.configure(background = "green")#For windows system
            # self.button.configure(highlightbackground = "green")#For Mac system
            self.color = "green"
        elif self.ratio > 0.1 and self.ratio <= 0.3:
            self.button.configure(background = "yellow")#For windows system
            # self.button.configure(highlightbackground = "yellow")#For Mac system
            self.color = "yellow"
        else:
            self.button.configure(background = "red")#For windows system
            # self.button.configure(highlightbackground = "red")#For Mac system
=======
            self.button.configure(highlightbackground="green")
            self.button.configure(bg="green")
            self.color = "green"
        elif self.ratio > 0.1 and self.ratio <= 0.3:
            self.button.configure(highlightbackground="yellow")
            self.button.configure(bg="yellow")
            self.color = "yellow"
        else:
            self.button.configure(highlightbackground="red")
            self.button.configure(bg="red")
>>>>>>> 5140f0f5676510f4f9cc79ba875bde23e5a62ff9
            self.color = "red"

    def add_button(self, button):
        self.button = button

    def change_schedule(self, open, close):
        self.schedule = [open, close]


def showdata(building):
    tk.messagebox.showinfo("Data Report",
                           "Building: " + building.name + "\n\nEmergency: " + building.color + "\nPeople in building: " + str(
                               building.people) + "\nCapacity:" + str(building.capacity)
                           + "\n\nOpening time: " + str(building.schedule[0]) + ":00 ~ " + str(
                               building.schedule[1]) + ":00")


def updateData(all):
    for building in all:
        original = building.people
        building.people = random.randint(max(0, original-10), min(building.capacity, original+10))
        building.auto_color()


def showdata1(name):
    tk.messagebox.showinfo("Data Report",
                           "Building: " + str(name) + "\n\nEmergency: red\nPeople in building: 50\nCapacity:100")


def showdata2(name):
    tk.messagebox.showinfo("Data Report",
                           "Building: " + str(name) + "\n\nEmergency: green\nPeople in building: 30\nCapacity:500")


def showdata3(name):
    tk.messagebox.showinfo("Data Report",
                           "Building: " + str(name) + "\n\nEmergency: yellow\nPeople in building: 35\nCapacity:200")


<<<<<<< HEAD
def login():
    global login_screen
    login_screen = tk.Toplevel(frame_picture)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    tk.Label(login_screen, text="Please enter details below to login").pack()
    tk.Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry
 
    username_verify = tk.StringVar()
    password_verify = tk.StringVar()
 
   
    tk.Label(login_screen, text="Username * ").pack()
    username_login_entry = tk.Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    tk.Label(login_screen, text="").pack()
    tk.Label(login_screen, text="Password * ").pack()
    password_login_entry = tk.Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    tk.Label(login_screen, text="").pack()
    tk.Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, tk.END)
    password_login_entry.delete(0, tk.END)
    if username1 == user_admin:
        if password1 == user_password:
            login_success()
        else:
            wrong_password()
    else:
        user_not_found()
def login_success():
    global login_success_screen
    login_success_screen = tk.Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    tk.Label(login_success_screen, text="Login Success").pack()
    tk.Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def wrong_password():
    global password_not_recog_screen
    password_not_recog_screen = tk.Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    tk.Label(password_not_recog_screen, text="Invalid Password ").pack()
    tk.Button(password_not_recog_screen, text="OK", command=delete_wrong_password).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = tk.Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    tk.Label(user_not_found_screen, text="User Not Found").pack()
    tk.Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_wrong_password():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

tk.Button(master=frame_toolbar,text="Login", height="2", width="30", command=login).pack() 
tk.Label(text="").pack() 

#bg does'nt work for mac, I use highlightbackgroun instead
button = tk.Button(text = "West" )
button.place(x = 100, y = 55)
=======
# bg does'nt work for mac, I use highlightbackgroun instead
button = tk.Button(text="West")
button.place(x=100, y=55)
>>>>>>> 5140f0f5676510f4f9cc79ba875bde23e5a62ff9
west = Building("West", button)
west.people = 40
west.auto_color()
button.configure(command=lambda: showdata(west))

button = tk.Button(text="Walker")
button.place(x=155, y=167)
walker = Building("Walker", button)
button.configure(command=lambda: showdata(walker))

button = tk.Button(text="Sage")
button.place(x=265, y=150)
sage = Building("Sage", button)
sage.people = 6
sage.auto_color()
button.configure(command=lambda: showdata(sage))

button = tk.Button(text="Troy")
button.place(x=370, y=145)
troy = Building("Troy", button)
button.configure(command=lambda: showdata(troy))

button = tk.Button(text="Richetts")
button.place(x=445, y=155)
richetts = Building("Richetts", button)
button.configure(command=lambda: showdata(richetts))

button = tk.Button(text="Wrestling")
button.place(x=535, y=175)
wrestling = Building("Wrestling", button)
button.configure(command=lambda: showdata(wrestling))

button = tk.Button(text="Quad")
button.place(x=635, y=200)
quad = Building("Quad", button)
quad.capacity = 200
quad.auto_color()
button.configure(command=lambda: showdata(quad))

button = tk.Button(text="Pittsburgh")
button.place(x=70, y=130)
pittsburgh = Building("Pittsburgh", button)
button.configure(command=lambda: showdata(pittsburgh))

button = tk.Button(text="Lally")
button.place(x=230, y=270)
lally = Building("Lally", button)
lally.capacity = 30
lally.auto_color()
button.configure(command=lambda: showdata(lally))

button = tk.Button(text="AE")
button.place(x=175, y=260)
ae = Building("AE", button)
button.configure(command=lambda: showdata(ae))

button = tk.Button(text="Greene")
button.place(x=310, y=280)
greene = Building("Greene", button)
greene.change_schedule(8, 17)
button.configure(command=lambda: showdata(greene))

button = tk.Button(text="Carnegie")
button.place(x=100, y=220)
carnegie = Building("Carnegie", button)
button.configure(command=lambda: showdata(carnegie))

button = tk.Button(text="Library")
button.place(x=160, y=380)
library = Building("Library", button)
library.capacity = 300
library.change_schedule(7, 3)
library.auto_color()
button.configure(command=lambda: showdata(library))

button = tk.Button(text="VCC")
button.place(x=255, y=390)
vcc = Building("VCC", button)
vcc.capacity = 60
vcc.auto_color()
button.configure(command=lambda: showdata(vcc))

button = tk.Button(text="EMPAC", command=lambda: showdata2("EMPAC"))
button.place(x=50, y=440)
empac = Building("EMPAC", button)
empac.capacity = 300
empac.auto_color()
button.configure(command=lambda: showdata(empac))

button = tk.Button(text="J_ROWL")
button.place(x=350, y=450)
j_rowl = Building("J_ROWL", button)
button.configure(command=lambda: showdata(j_rowl))

button = tk.Button(text="Cogswell")
button.place(x=255, y=550)
cogswell = Building("Cogswell", button)
button.configure(command=lambda: showdata(cogswell))

button = tk.Button(text="JEC")
button.place(x=390, y=350)
jec = Building("JEC", button)
button.configure(command=lambda: showdata(jec))

button = tk.Button(text="LOW")
button.place(x=520, y=380)
low = Building("LOW", button)
button.configure(command=lambda: showdata(low))

button = tk.Button(text="UNION", command=lambda: showdata3("UNION"))
button.place(x=760, y=300)
union = Building("UNION", button)
union.capacity = 200
union.change_schedule(8, 23)
union.auto_color()
button.configure(command=lambda: showdata(union))

button = tk.Button(text="Mueller Center")
button.place(x=720, y=500)
Mueller = Building("Mueller Center", button)
Mueller.change_schedule(10, 22)
button.configure(command=lambda: showdata(Mueller))

button = tk.Button(text="Center for Biotechnology")
button.place(x=480, y=520)
cbis = Building("Center for Biotechnology", button)
button.configure(command=lambda: showdata(cbis))

button = tk.Button(text="Ballroom")
button.place(x=550, y=640)
ballroom = Building("Ballroom", button)
ballroom.people = 50
ballroom.auto_color()
button.configure(command=lambda: showdata(ballroom))

button = tk.Button(text="Sage Dining Hall")
button.place(x=550, y=310)
sage_dining = Building("Sage Dining Hall", button)
button.configure(command=lambda: showdata(sage_dining))

allbuilding = [west, walker, sage, troy, richetts, wrestling, quad,
               pittsburgh, lally, ae, greene, carnegie, library, vcc,
               empac, j_rowl, cogswell, jec, low, union, Mueller, cbis,
               ballroom, sage_dining]

button = tk.Button(frame_toolbar, text="UPDATE")
button.place(x=0, y=60)
button.configure(command=lambda: updateData(allbuilding))

if __name__ == "__main__":
    # restrict the user to resize window
    window.resizable(width=False, height=False)
    window.mainloop()
