from tkinter import *
from tkinter import ttk

root = Tk()

frame = ttk.Frame(root, width=200, height=200, padding=5)
frame['borderwidth'] = 10
frame['relief'] = 'sunken'
frame.grid()

label = ttk.Label(frame, text='Full name:')
label.grid()

resultsContents = StringVar()
label['textvariable'] = resultsContents
resultsContents.set('New value to display')

button = Button(frame, text='GO!', font=('MS Sans Serif', 20, 'bold'), fg='green', bg='yellow', relief='flat')
button.grid()
button_1 = Button(root, text='Okay', fg='white', bg='blue')
button_1.grid()
button_2 = Button(root, text='Cancel', font=('MS Sans Serif', 20, 'bold'), fg='green', bg='yellow', relief='flat')
button_2.grid()
button_3 = Button(root, text='Print', bg='green', fg='white')
button_3.grid()

s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
ttk.Frame(frame, width=100, height=50, style='Danger.TFrame').grid()

phone = StringVar()
home = ttk.Radiobutton(root, text='Home', variable=phone, value='home')
office = ttk.Radiobutton(frame, text='Office', variable=phone, value='office')
cell = ttk.Radiobutton(frame, text='Mobile', variable=phone, value='cell')

username = StringVar()
name = ttk.Entry(frame, textvariable=username)







root.mainloop()


