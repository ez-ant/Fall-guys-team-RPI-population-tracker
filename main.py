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

#bg does'nt work for mac, I use highlightbackgroun instead
west = tk.Button(text = "West", highlightbackground  = "red")
west.place(x = 100, y = 55)

walker = tk.Button(text = "Walker", highlightbackground  = "red")
walker.place(x = 155, y = 167)

sage = tk.Button(text = "Sage", highlightbackground  = "red")
sage.place(x = 265, y = 150)

troy = tk.Button(text = "Troy", highlightbackground  = "red")
troy.place(x = 370, y = 145)

richetts = tk.Button(text = "Richetts", highlightbackground  = "red")
richetts.place(x = 445, y = 155)

wrestling = tk.Button(text = "Wrestling", highlightbackground  = "red")
wrestling.place(x = 535, y = 175)

quad = tk.Button(text = "Quad", highlightbackground  = "red")
quad.place(x = 635, y = 200)

pittsburgh = tk.Button(text = "Pittsburgh", highlightbackground  = "red")
pittsburgh.place(x = 70, y = 130)

lally = tk.Button(text = "Lally", highlightbackground  = "red")
lally.place(x = 230, y = 270)

amos = tk.Button(text = "AE", highlightbackground  = "red")
amos.place(x = 175, y = 260)

greene = tk.Button(text = "Greene", highlightbackground  = "red")
greene.place(x = 310, y = 280)

carnegie = tk.Button(text = "Carnegie", highlightbackground  = "red")
carnegie.place(x = 100, y = 220)

library = tk.Button(text = "Library", highlightbackground  = "red")
library.place(x = 160, y = 380)

vcc = tk.Button(text = "VCC", highlightbackground  = "red")
vcc.place(x = 255, y = 390)

empac = tk.Button(text = "EMPAC", highlightbackground  = "red")
empac.place(x = 50, y = 440)

j_rowl = tk.Button(text = "J_ROWL", highlightbackground  = "red")
j_rowl.place(x = 350, y = 450)

cogswell = tk.Button(text = "Cogswell", highlightbackground  = "red")
cogswell.place(x = 255, y = 550)

jec = tk.Button(text = "JEC", highlightbackground  = "red")
jec.place(x = 390, y = 350)

low = tk.Button(text = "LOW", highlightbackground  = "red")
low.place(x = 520, y = 380)

union = tk.Button(text = "Union", highlightbackground  = "red")
union.place(x = 760, y = 300)

mueller = tk.Button(text = "Mueller Center", highlightbackground  = "red")
mueller.place(x = 720, y = 500)

cbis = tk.Button(text = "Center for Biotechnology", highlightbackground  = "red")
cbis.place(x = 480, y = 520)

ballroom = tk.Button(text = "Ballroom", highlightbackground  = "red")
ballroom.place(x = 550, y = 640)

sage_dining = tk.Button(text = "Sage Dining Hall", highlightbackground  = "red")
sage_dining.place(x = 550, y = 310)


if __name__ == "__main__":
    #restrict the user to resize window
    window.resizable(width = False, height = False)
    window.mainloop()