from tkinter import *

# 1. Zapolnenie konteinera.

main_window = Tk()
main_window.geometry('800x600+50+50')

my_label = Label(main_window, text='My Text!', bg='green', fg='white')
my_label.pack(fill=X)  # zapolnjaetsja stroka
# my_label.pack(fill=Y, expand=1) # zapolnjaetsja vertikal
# my_label.pack(fill=BOTH, expand=1) # zapolnjaetsja polnostiu conteiner

red_label = Label(main_window, text='Red Text!', bg='red', fg='white')
red_label.pack(fill=BOTH, expand=1, padx=10)
green_label = Label(main_window, text='Green Text!', bg='green', fg='white')
green_label.pack(fill=BOTH, expand=1, pady=10)
yellow_label = Label(main_window, text='Yellow Text!', bg='yellow', fg='black')
yellow_label.pack(fill=BOTH, expand=1, padx=10, pady=10)

listbox = Listbox(main_window)
listbox.pack(fill=BOTH, expand=1)

for i in range(20):
    listbox.insert(END, str(i))



main_window.mainloop()
# 2.Raspoloshenie vidshetov odin pod drugim
# 3. Raspoloshenie vidshetov rjadom drug s drugom

# red_label = Label(main_window, text='Red Text!', bg='red', fg='white')
# red_label.pack(ipadx=30, side=LEFT)
# green_label = Label(main_window, text='Green Text!', bg='green', fg='white')
# green_label.pack(ipady=30, side=LEFT)
# yellow_label = Label(main_window, text='Yellow Text!', bg='yellow', fg='black')
# yellow_label.pack(side=LEFT)

# red_label = Label(main_window, text='Red Text!', bg='red', fg='white')
# red_label.pack(ipadx=30, side=RIGHT)
# green_label = Label(main_window, text='Green Text!', bg='green', fg='white')
# green_label.pack(ipady=30, side=RIGHT)
# yellow_label = Label(main_window, text='Yellow Text!', bg='yellow', fg='black')
# yellow_label.pack(side=RIGHT)

