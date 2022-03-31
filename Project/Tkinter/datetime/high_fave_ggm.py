import tkinter as tk
from tkinter import ttk

def greeting():
    print(f'High five, {username.get()}!')


root = tk.Tk()
root.title('High five!')


root.columnconfigure(0, weight=1)

username = tk.StringVar()

input_frame = ttk.Frame(root, padding=(10, 5, 10, 0))
input_frame.grid(row=0, column=0, sticky='EW')
input_frame.columnconfigure(0, weight=1)

username_label = ttk.Label(input_frame, text='Name: ')
username_label.grid(row=0, column=0, padx=(5, 10))

username_entry = ttk.Entry(input_frame, width=20, textvariable=username)
username_entry.grid(row=0, column=1, padx=(0, 10))
username_entry.focus()

button_frame = ttk.Button(root, padding=(10, 5))
button_frame.grid(row=1, column=0, sticky='EW')
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)



greeting_button = ttk.Button(button_frame, text='Hello!', command=greeting)
greeting_button.grid(row=0, column=0, sticky='EW')


cancel_button = ttk.Button(button_frame, text='Cancel', command=root.destroy)
cancel_button.grid(row=0, column=1, sticky='EW')


root.mainloop()