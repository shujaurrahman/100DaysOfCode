from tkinter import *
def miles_to_km():
    miles=float(miles_input.get())
    km=1.609*miles
    kilometer_resul_label.config(text=f"{km}")

window=Tk()
window.title("Mile to km ")
window.config(padx=20,pady=20)
miles_input=Entry(width=7)
miles_input.grid(column=1,row=0)

mile_lable=Label(text="Miles")
mile_lable.grid(column=2,row=0)
isequal_lable=Label(text="is equal to ")
isequal_lable.grid(column=0,row=1)

kilometer_resul_label=Label(text="0")
kilometer_resul_label.grid(column=1,row=1)



km_label=Label(text="Km")
km_label.grid(column=2,row=1)

btn=Button(text="Calculate",command=miles_to_km)
btn.grid(column=1,row=2)

window.mainloop()