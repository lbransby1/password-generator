import tkinter as tk
import random

def baseLetters():
  letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  pw = ""
  for i in range(0, 8):
    newLetter = letters[random.randrange(0, len(letters))]
    pw = str(pw + newLetter)
    i = i+1 
  return pw
  
def addNumbers():
  newPassword = ''
  for i in range(3):
    newPassword += str(random.randrange(0,9))
    i = i+1
  return(newPassword)

def capPassword(pw):
  return(pw.capitalize())

def specialChar():
  letters = ['!','£','$','.',',','@',':',';','/','?','#']
  pw = str(letters[random.randint(0, len(letters)-1)])
  return pw





def passwordPage():
  pw=tk.Tk()
  pw.resizable(False, False)
  pw.title('Password Generator and Validator')
  pw.columnconfigure(0)
  pw.rowconfigure(0)



  numBool= ''
  tk.Checkbutton(pw, text="Add numbers", onvalue="True", offvalue="False", variable= numBool).grid(column=0, row = 0)

  capBool= ''
  tk.Checkbutton(pw, text="Capitalize", onvalue="True", offvalue="False", variable= capBool).grid(column=1, row = 0)

  charBool= ''
  tk.Checkbutton(pw, text="special character", onvalue="True", offvalue="False", variable= charBool).grid(column=2, row = 0)

  tk.Button(pw, text="Generate Password", command=lambda:generatePassword()).grid(column=0, row=1)

  def generatePassword():
    password = baseLetters()
    if numBool.get() == 'True':
      password += addNumbers()
    if capBool.get() =='True':
      password = capPassword(password)
    if charBool.get() == 'True':
      password += specialChar()
    print(password)

  def printIfClicked():
    if numBool:
      print(numBool)
    

  pw.mainloop()



