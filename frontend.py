import tkinter as tk
from password import * 

def destroy():
  for widget in root.winfo_children():
    widget.destroy()



# home 
def home(root):
  destroy()
  page = tk.Frame(root)
  page.grid()

  tk.Label(page, text = 'This is the home page of the program').grid(row = 0, columnspan=2)
  
  tk.Button(page, text = 'Enter new details', command = lambda:new(root)).grid(row = 2)
  
  tk.Button(page, text = 'View previous passwords', command = lambda:view(root)).grid(row = 2, column=1)

# end of home 


#new
def new(root):
  destroy()
  page = tk.Frame(root)
  page.grid()
  
  tk.Label(page, text = 'This is where the new details will be added').grid(row = 0, columnspan=3)
  
  website = tk.StringVar()
  tk.Label(page, text = 'Website').grid(column=0, row=1)
  tk.Entry(page, textvariable=website).grid(column=1, row=1)

  username = tk.StringVar()
  tk.Label(page, text = 'Username').grid(column=0, row=2)
  tk.Entry(page, textvariable=username).grid(column=1, row=2)

  password = tk.StringVar()
  tk.Label(page, text = 'Password').grid(column=0, row=3)
  tk.Entry(page, textvariable=password, show='#').grid(column=1, row=3)
  tk.Button(page, text='Generate password', command=lambda:passwordPage()).grid(column=2, row=3)


  tk.Button(page, text = 'Back to home', command = lambda:home(root)).grid(row = 100)

#end of new

#view
def view(root):
  destroy()
  page = tk.Frame(root)
  page.grid()
  
  tk.Label(page, text = 'This is the page for viewing details').grid(row = 0)
  
  tk.Button(page, text = 'Back', command = lambda:home(root)).grid(row = 1)
#end of view







root = tk.Tk()
root.title('Password Manager')
home(root)
root.mainloop()