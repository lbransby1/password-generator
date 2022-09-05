import tkinter as tk

def destroy():
  for widget in root.winfo_children():
    widget.destroy()

def home(root):
  destroy()
  page = tk.Frame(root)
  page.grid()
  tk.Label(page, text = 'This is the home page of the program').grid(row = 0, columnspan=2)
  tk.Button(page, text = 'Enter new details', command = lambda:new(root)).grid(row = 1)
  tk.Button(page, text = 'View previous passwords', command = lambda:view(root)).grid(row = 1, column=1)

def new(root):
  destroy()
  page = tk.Frame(root)
  page.grid()
  tk.Label(page, text = 'This is where the new details will be added').grid(row = 0)
  tk.Button(page, text = 'Back to home', command = lambda:home(root)).grid(row = 1)

def view(root):
  destroy()
  page = tk.Frame(root)
  page.grid()
  tk.Label(page, text = 'This is the page for viewing details').grid(row = 0)
  tk.Button(page, text = 'Back', command = lambda:home(root)).grid(row = 1)

def changepage(page):
  global root
  for widget in root.winfo_children():
    widget.destroy()
  if page == new:
    new(root)
  elif page == home:
    home(root)
    

root = tk.Tk()
home(root)
root.mainloop()