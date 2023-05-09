from tkinter import *

FONT =("arial", 15, "bold")
x = 10
y = 10
window = Tk()
window.title("mile to km converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

input = Entry()
input.grid(column=1, row=0)


miles = Label(text="Miles", font=FONT)
miles.grid(row=0, column=2)
miles.config(padx=x, pady=y)

label2 = Label(text="is equal to", font=FONT)
label2.grid(row=1, column=0)
label2.config(padx=x, pady=y)

kilometer_resutl = Label(text="0", font=FONT)
kilometer_resutl.grid(row=1, column=1)
kilometer_resutl.config(padx=x, pady=y)

lable4 = Label(text="Km", font=FONT)
lable4.grid(column=2, row=1)
lable4.config(padx=x, pady=y)


def button_clicked():
    data = input.get()
    data_km = round(float(data) * 1.689)
    kilometer_resutl.config(text=str(data_km))


button = Button(text="calculate", command=button_clicked)
button.grid(row=2, column=1)
button.config(padx=x, pady=y)







window.mainloop()
