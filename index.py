# Generate random password
import string
import random
import pyperclip

def password_gen():
  s1 = string.ascii_uppercase #uppercase strings
  s2 = string.ascii_lowercase #lowercase strings
  s3 = string.digits #string digits
  s4 = string.punctuation #string punctuation

  passlen = int(input('Please input how many characters you would like in your password? '))
  s = []
  s.extend(list(s1))
  s.extend(list(s2))
  s.extend(list(s3))
  s.extend(list(s4))

  random.shuffle(s)
  newpass = ("".join(s[0:passlen]))
  # Copy new password to clipboard
  pyperclip.copy(newpass)
  # Print password to terminal
  print(f'Your new password is: {newpass}')

password_gen()