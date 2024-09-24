from tkinter import *

#Button
def button_clicked():
    print("I got clicked")
    value = input.get()
    my_label.config(text=value)

window = Tk()
window.title("My First Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label.", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Button
new_button = Button(text="New buttton", command=button_clicked)
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)




window.mainloop()

