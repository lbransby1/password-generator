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
