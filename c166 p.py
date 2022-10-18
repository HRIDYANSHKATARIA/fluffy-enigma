from tkinter import *
from PIL import Image,ImageTk 

root = Tk()
root.title("Canvas")
root.geometry("600x600")

label_color = Label(root,text="startx")
label_color.place(relx=0.6,rely=0.9,anchor=CENTER)

input_box_starx = Entry(root)
input_box_starx.insert(0,"                200")
input_box_starx.place(relx=0.8,rely=0.9,anchor=CENTER)

label_color = Label(root,text="starty")
label_color.place(relx=0.6,rely=0.9,anchor=CENTER)


input_box_stary = Entry(root)
input_box_stary.insert(0,"                200")
input_box_stary.place(relx=0.8,rely=0.9,anchor=CENTER)

label_color = Label(root,text="endx")
label_color.place(relx=0.6,rely=0.9,anchor=CENTER)


input_box_endx = Entry(root)
input_box_endx.insert(0,"                20")
input_box_endx.place(relx=0.8,rely=0.9,anchor=CENTER)

label_color = Label(root,text="endy")
label_color.place(relx=0.6,rely=0.9,anchor=CENTER)


input_box_endy = Entry(root)
input_box_endy.insert(0,"                20")
input_box_endy.place(relx=0.8,rely=0.9,anchor=CENTER)

label_color = Label(root,text="Enter a Color")
label_color.place(relx=0.6,rely=0.9,anchor=CENTER)


input_box = Entry(root)
input_box.insert(0,"                Black")
input_box.place(relx=0.8,rely=0.9,anchor=CENTER)

canvas = Canvas(root,width=590,height=510,bg="white",highlightbackground="lightgray")
canvas.pack()

img = ImageTk.PhotoImage(Image.open("start_point1.png"))
my_image = canvas.create_image(50,50,image = img)
 
direction = ""
oldx = input_box_starx.get()
oldy = input_box_stary.get()
newx = input_box_endx.get()
newy = input_box_endy.get()

def draw(direction,oldx,oldy,newx,newy):
    fill_color = input_box.get()
    
def line(direction,oldx,oldy,newx,newy):
    Line(endx,endy,starx,stary)
    
line = Button(root,text="line",command="line")

root.mainloop()