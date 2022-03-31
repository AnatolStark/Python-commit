from tkinter import *

root_window = Tk()


red_label = Label(root_window, text='Red Text!', bg='red', fg='white', width=20, height=5)
red_label.grid(row=0, column=0)
green_label = Label(root_window, text='Green Text!', bg='green', fg='white', width=20, height=5)
green_label.grid(row=0, column=1)
yellow_label = Label(root_window, text='Yellow Text!', bg='yellow', fg='black', width=20, height=5)
yellow_label.grid(row=0, column=2)

red_label_1 = Label(root_window, text='Red Text!', bg='red', fg='white', width=20, height=5)
red_label_1.grid(row=1, column=0)
green_label_1 = Label(root_window, text='Green Text!', bg='green', fg='white', width=20, height=5)
green_label_1.grid(row=1, column=1)
yellow_label_1 = Label(root_window, text='Yellow Text!', bg='yellow', fg='black', width=20, height=5)
yellow_label_1.grid(row=1, column=2)

button_1 = Button(root_window, text='Some Button 1')
button_1.grid(row=2, column=0)
button_2 = Button(root_window, text='Some Button 1')
button_2.grid(row=2, column=1)
button_3 = Button(root_window, text='Some Button 1')
button_3.grid(row=2, column=2)


root_window.mainloop()



