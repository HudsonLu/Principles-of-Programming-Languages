# This implements a _very_ basic editor (a subset to Notepad) in
# Python using tkinter.
#
import tkinter
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.messagebox import askokcancel, showinfo
from tkinter import Menu

# Define each of the menu commands.
def new_cmd(self = None):
    '''Implement the New menu command.'''
    if maybe_ask_save():
        text.delete(1.0, tkinter.END)
        text.edit_modified(False)
    
def open_cmd(self = None):
    '''Implement the Open menu command.'''
    if maybe_ask_save():
        file = askopenfile(parent = root, mode = 'rb', title = 'Select a file')
        if file:
            text.delete("1.0", tkinter.END)
            text.insert("1.0", file.read())
            file.close()
            text.edit_modified(False)

def save_cmd(self = None):
    '''Implement the Save menu command.'''
    file = asksaveasfile(mode = 'w')
    if file:
        file.write(text.get("1.0", tkinter.END))
        file.close()
        text.edit_modified(False)

def exit_cmd(self = None):
    '''Implement the Exit menu command.'''
    if maybe_ask_save():
        root.destroy()

def about_cmd():
    '''Implement the About menu command.'''
    showinfo("About", "A simple Notepad clone.\n\nA tkinter sample program.")

def maybe_ask_save():
    '''Simple check to make sure we don't discard any edits.'''
    result = True
    if text.edit_modified():
        result = askokcancel('Discard Changes',
                             'File has been modified. OK to discard changes?')
    return result

def create_menu(root):
    '''Function to set up the menu for the Python Notepad.'''
    menubar = Menu(root)
    root.config(menu = menubar)
    filemenu = Menu(menubar, tearoff = False)
    menubar.add_cascade(label = "File", menu = filemenu)
    filemenu.add_command(label = "New", command = new_cmd,
                         accelerator = "Ctrl-N")
    filemenu.add_command(label = "Open...", command = open_cmd,
                         accelerator = "Ctrl-O")
    filemenu.add_command(label = "Save", command = save_cmd,
                         accelerator = "Ctrl-S")
    filemenu.add_separator()
    filemenu.add_command(label = "Exit", command = exit_cmd)
    helpmenu = Menu(menubar, tearoff = False)
    menubar.add_cascade(label = "Help", menu = helpmenu)
    helpmenu.add_command(label = "About...", command = about_cmd)
    
# Perform the basic initialization.
root = tkinter.Tk(className = 'tkNote')

# Create the menu.
create_menu(root)

# Set up keyboard shortcuts.
root.bind("<Control-n>", new_cmd)
root.bind("<Control-o>", open_cmd)
root.bind("<Control-s>", save_cmd)

# Create the scrolled text widget.
text = ScrolledText(root, width = 80, height = 40)
text.pack(side = "left", fill = "both", expand = True)

# Actually start handling keypresses and mouse clicks...
root.mainloop()
