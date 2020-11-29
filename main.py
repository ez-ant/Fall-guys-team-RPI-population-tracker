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
button = tk.Button(text = "West Hall", fg = "blue", highlightbackground  = "red")
button.place(x = 100, y = 50)

if __name__ == "__main__":
    #restrict the user to resize window
    window.resizable(width = False, height = False)
    window.mainloop()