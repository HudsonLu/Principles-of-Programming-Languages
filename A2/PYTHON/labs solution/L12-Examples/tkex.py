import tkinter
wnd = tkinter.Tk()
wnd.title('A simple example')

lbl = tkinter.Label(wnd,
        text='This is a very simple GUI')
lbl.pack()
btn = tkinter.Button(wnd,
        text="Cancel", command=wnd.quit)
btn.pack()
wnd.mainloop()
