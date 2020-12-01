import connect_database
import tkinter as tk
from PIL import ImageTk, Image
#set window
window = tk.Tk()
window.geometry("1000x700")
# to maximize window
#w, h = window.winfo_screenwidth(), window.winfo_screenheight()
#window.geometry("%dx%d+0+0" % (w, h))


frame_picture = tk.Frame(master = window, width = 900, height = 700, bg = "white")

frame_toolbar = tk.Frame(master = window, width = 300, height = 700, bg = "white")

frame_picture.pack(fill = tk.Y, side = tk.LEFT)
frame_toolbar.pack(fill = tk.Y, side = tk.RIGHT)

label = tk.Label(master = frame_toolbar, text = "Toolbar           ", foreground = "black")

label.pack()

path = "rpi_buildings.png"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
image = Image.open(path)
image = image.resize((820, 700), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)


#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
background_picture = tk.Label(frame_picture, image = img)

#The Pack geometry manager packs widgets in rows or columns.
background_picture.place(x=0, y=0, relwidth=1, relheight=1)

class Building:
    def __init__(self, name, button):
        self.name = name
        self.button = button
        self.button.configure(highlightbackground = "yellow")
    def change_color(self, color):
        self.button.configure(highlightbackground = color)

#bg does'nt work for mac, I use highlightbackgroun instead
button = tk.Button(text = "West")
button.place(x = 100, y = 55)
west = Building("West", button)

button = tk.Button(text = "Walker")
button.place(x = 155, y = 167)
walker = Building("Walker", button)

button = tk.Button(text = "Sage")
button.place(x = 265, y = 150)
sage = Building("Sage", button)

button = tk.Button(text = "Troy")
button.place(x = 370, y = 145)
troy = Building("Troy", button)

button = tk.Button(text = "Richetts")
button.place(x = 445, y = 155)
richetts = Building("Richetts", button)

button = tk.Button(text = "Wrestling")
button.place(x = 535, y = 175)
wrestling = Building("Wrestling", button)

button = tk.Button(text = "Quad")
button.place(x = 635, y = 200)
quad = Building("Quad", button)

button = tk.Button(text = "Pittsburgh")
button.place(x = 70, y = 130)
pittsburgh = Building("Pittsburgh", button)

button = tk.Button(text = "Lally")
button.place(x = 230, y = 270)
lally = Building("Lally", button)

button = tk.Button(text = "AE")
button.place(x = 175, y = 260)
ae = Building("AE", button)

button = tk.Button(text = "Greene")
button.place(x = 310, y = 280)
greene = Building("Greene", button)

button = tk.Button(text = "Carnegie")
button.place(x = 100, y = 220)
carnegie = Building("Carnegie", button)

button = tk.Button(text = "Library")
button.place(x = 160, y = 380)
library = Building("Library", button)

button = tk.Button(text = "VCC")
button.place(x = 255, y = 390)
vcc = Building("VCC", button)

button = tk.Button(text = "EMPAC")
button.place(x = 50, y = 440)
empac = Building("EMPAC", button)

button = tk.Button(text = "J_ROWL")
button.place(x = 350, y = 450)
j_rowl = Building("J_ROWL", button)

button = tk.Button(text = "Cogswell")
button.place(x = 255, y = 550)
cogswell = Building("Cogswell", button)

button = tk.Button(text = "JEC")
button.place(x = 390, y = 350)
jec = Building("JEC", button)

button = tk.Button(text = "LOW")
button.place(x = 520, y = 380)
low = Building("LOW", button)

button = tk.Button(text = "UNION")
button.place(x = 760, y = 300)
union = Building("UNION", button)

button = tk.Button(text = "Mueller Center")
button.place(x = 720, y = 500)
Mueller = Building("Mueller Center", button)

button = tk.Button(text = "Center for Biotechnology")
button.place(x = 480, y = 520)
cbis = Building("Center for Biotechnology", button)

button = tk.Button(text = "Ballroom")
button.place(x = 550, y = 640)
ballroom = Building("Ballroom", button)

button = tk.Button(text = "Sage Dining Hall")
button.place(x = 550, y = 310)
sage_dining = Building("Sage Dining Hall", button)


if __name__ == "__main__":
    #restrict the user to resize window
    window.resizable(width = False, height = False)
    window.mainloop()