from tkinter import *

# Raspoloshenie wigetov

root = Tk()
root.geometry('500x300+100+100')

red_label = Label(root, text='Red Text!', bg='red', fg='white')
red_label.place(x=150, y=250, width=200)
green_label = Label(root, text='Green Text!', bg='green', fg='white')
green_label.place(x=175, y=130, width=150, height=40)
yellow_label = Label(root, text='Yellow Text!', bg='yellow', fg='black')
yellow_label.place(x=100, y=135, height=30)

red_label_rel_height = Label(root, text='Red relheight=0.3!', bg='red', fg='white')
red_label_rel_height.place(relheight=0.3)
green_label_rel_width = Label(root, text='Green relwidth=0.7!', bg='green', fg='white')
green_label_rel_width.place(relwidth=0.7)
yellow_label_rel_x = Label(root, text='Yellow relx=0.2!', bg='yellow', fg='black')
yellow_label_rel_x.place(relx=0.2)
yellow_label_rel_y = Label(root, text='Yellow rely=0.4!', bg='yellow', fg='black')
yellow_label_rel_y.place(rely=0.4)

label = Label(root, text='Some Text', bg='red', fg='white')
label.place(width=400, height=100, x=50, y=100)
button = Button(root, text='Some Button')
button.place(in_=label, relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()



