from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()


# This section builds the inital display for the calculator
display_value = "This is where your text will be displayed!"
ttk.Label(frm, text=F"{display_value}").grid(column=0, columnspan=3, row=0)
row_num = 1
column_num = 0
bwid = 5
for i in range(10):
    ttk.Button(frm, text=F"{i}", padding=20).grid(column=column_num, row=row_num)
    column_num += 1
    if (i + 1) % 3 == 0:
        row_num += 1
        column_num = 0
ttk.Button(frm, text="+", command=root.destroy, width=bwid).grid(column=4, row=1)
ttk.Button(frm, text="-", command=root.destroy, width=bwid).grid(column=4, row=2)
ttk.Button(frm, text="X", command=root.destroy, width=bwid).grid(column=4, row=3)
ttk.Button(frm, text="/", command=root.destroy, width=bwid).grid(column=4, row=4)
ttk.Button(frm, text="D", command=root.destroy, width=bwid).grid(column=1, row=4)
ttk.Button(frm, text="L", command=root.destroy, width=bwid).grid(column=2, row=4)

root.mainloop()