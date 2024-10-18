# import tkinter

# window=tkinter.Tk()
# window.title("My first GUI program")
# window.minsize(width=500,height=300)

# # Label

# label1=tkinter.Label(text="I am label",font=("Arial",24,"bold"))
# label1.pack(expand=True)

# window.mainloop()


# second lesson import everything if using many classes

from tkinter import *

window=Tk()
window.title("GUI Practice")

window.minsize(width=500,height=300)

label1=Label(text="Who are you?",font=("Arial",24))
label1.pack()

# def btnclicked():
#     print("I got clicked!")
# def newlabel():
#     label1["text"]="New label after btn clicked "
    # label1.config(text="new text")

# label1["text"]="New label"
# label1.config(text="new text")
# button=Button(text="btn",command=btnclicked)

def btnclick():
    print("i got clicked")
    new_text=input.get()
    label1.config(text=new_text)
    # or 
    # label1["text"]="New label"

button=Button(text="btn",command=btnclick)
button.pack()


# Entry datat 
input=Entry()
input.pack()

print(input.get()) #returns the entered text in the input cont 



window.mainloop()