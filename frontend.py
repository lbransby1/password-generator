import tkinter as tk
import tkinter.scrolledtext as st
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

  def returnData():
    data= str(website.get()) + ' | '+ str(username.get())+ ' | '+ str(password.get())
    with open("text.txt","a") as file:
      file.write(data+ '\n')
    clear(page)

    print('password saved')

  def clear(root):
    for widget in root.winfo_children():
        if not isinstance(widget, tk.Entry):
            clear(widget)
        elif isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)



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
  tk.Button(page, text = 'Save', command = returnData).grid(row = 99)
  tk.Button(page, text = 'Clear', command = lambda:clear(page)).grid(row = 99, column=1)

#end of new

#view
def view(root):
  destroy()
  page = tk.Frame(root)
  page.grid()
  
  tk.Label(page, text = 'This is the page for viewing details').grid(row = 0)
  text_area= st.ScrolledText(page).grid(row=1).insert(tk.INSERT,
  """\
  This is a scrolledtext widget to make tkinter text read only.
  Hi
  Geeks !!!
  Geeks !!!
  Geeks !!! 
  Geeks !!!
  Geeks !!!
  Geeks !!!
  Geeks !!!
  """)
  
  text_area.configure(state ='disabled')
  tk.Button(page, text = 'Back', command = lambda:home(root)).grid(row = 1)
#end of view







root = tk.Tk()
root.title('Password Manager')
home(root)
root.mainloop()