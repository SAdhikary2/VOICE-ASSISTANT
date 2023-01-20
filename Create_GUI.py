from operation import *
from tkinter import *
from PIL import Image, ImageTk


root=Tk()
root.geometry("600x500+500+100")
root.resizable(False,False)
root.title("Voice Assistant | Developed By Sukalyan ")
root.config(background="black")

label=Label(root,width=100,height=100,bg="grey")
label.place(x=200,y=200)

#______________________________________________HEADING__________________________________________________________________

frame=Frame(root,background='grey')
frame.place(x=0,y=0,height=40,width=700)
Label(frame,text="VOICE ASSISTANT",font="courier 20",fg="white",bg="grey").place(x=175,y=8)

#_____________________________________________IMAGE FRAME______________________________________________________________

canvas1=Canvas(root,width=360,height=350,background="grey",bd=20,relief=RIDGE)
canvas1.place(x=100,y=50)
img=(Image.open("pepper.jpg"))
# Resizing the image
resize_image=img.resize((300,285),Image.LANCZOS)
new_image=ImageTk.PhotoImage(resize_image)
# Adding image in the canvas
canvas1.create_image(50,50,anchor=NW,image=new_image)

#_____________________________________________BUTTON SECTION__________________________________________________________

btn=Button(root,text="START",bg="red",fg="white",relief=RIDGE,bd=5,command=Gretting_user)
btn.place(x=250,y=455)
btn=Button(root,text="STOP",bg="red",fg="white",relief=RIDGE,bd=5)
btn.place(x=350,y=455)

#_______________________________________________MAIN  FUNTION_________________________________________________________


root.mainloop()

