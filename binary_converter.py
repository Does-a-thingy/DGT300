# define all var's
From = 1
INTO = 1
holder = 0
deci_number = 0
bina_number = 0
hexa_number = 0
octa_number = 0
final_number = 0

import os

# ask for from
def form_fetch():
  while True:
    FROM = int(input('''What would you like to convert from?:
    '1' for Decimal
    '2' for Binary
    '3' for Hexadecimal
    '4' for Octal
    '''))
    if FROM > 5 or < 0:
      print('please try again')
    else:
      break

# ask for into
into_fetch():
  while True:
    INTO = int((input'''What would you like to convert into?:
    '1' for Decimal
    '2' for Binary
    '3' for Hexadecimal
    '4' for Octal
    '''))
    if FROM > 5 or < 0:
      print('please try again')
   else:
      break

# getting

# get decimal number
def deci_get():
  while True:
    deci_number = int(input('Please enter an integer more than -1: '))
    if deci_number < 0:
      print('Try again')
    else:
      holder = deci_number
      break

# get binary number
def bina_get():
  while True:
    bina_number = int(input('Please enter a binary number: '))
    for x in bina_number:
      if x > 1 or x < 0:
        print('Try again')
        break
      else:
        continue
      holder = int(bina_number, 2)
      break

# get hex number
def hexa_get():
  while True:
    hexa_number = input('Please enter a hexadecimal number: ')
    for x in hexa_number:
      if x < 10 and x > -1:
        continue
      elif x == 'a' or x == 'A':
        continue
      elif x == 'b' or x == 'B':
        continue
      elif x == 'c' or x == 'C':
        continue
      elif x == 'd' or x == 'D':
        continue
      elif x == 'e' or x == 'E':
        continue
      elif x == 'f' or x == 'F':
        continue
      else:
        print('Try again') 
        break
      holder = int(haxa_number, 16)
      break
        
# get octal number
def octa_get():
  while True:
    octa_number = int(input('Please enter a octal number: '))
    for x in octa_number:
      if x > 7 or x < 0:
        print('Try again')
        break
      else:
        continue
      holder = int(octa_number, 8)
      break
    
# converting

# convertion into binary
def bina_convert(numb, mode):
  final_number = bin(numb)
  if mode == 1:
    print('{} in binary is {}'.format(numb, final_number))
  if mode == 3:
    print('{} in binary is {}'.format(hexa_number.get(), final_number))
  if mode == 4:
    print('{} in binary is {}'.format(octa_number.get(), final_number))

def hexa_convert(numb, mode):
  final_number = hex(numb)
  if mode == 1:
    print('{} in hexadecimal is {}'.format(numb, final_number))
  if mode == 2:
    print('{} in hexadecimal is {}'.format(bina_number.get(), final_number))
  if mode == 4:
    print('{} in hexadecimal is {}'.format(octa_number.get(), final_number))
  
def deci_convert(numb, mode):
  final_number = numb
  if mode == 2:
    print('{} in decimal is {}'.format(bina_number.get(), final_number))
  if mode == 3:
    print('{} in decimal is {}'.format(hexa_number.get(), final_number))
  if mode == 4:
    print('{} in decimal is {}'.format(octa_number.get(), final_number))

def octa_convert(numb, mode):
  final_number = oct(numb)
  if mode == 1:
    print('{} in octal is {}'.format(numb, final_number))
  if mode == 2:
    print('{} in octal is {}'.format(bina_number.get(), final_number))
  if mode == 3:
    print('{} in octal is {}'.format(hexa_number.get(), final_number))


# just to be safe I have put the main at the bottom :)
# numbers and presenting:
while loop is True:
  os.system('cls')
  form_fetch()
  into_fetch()
  if FROM == 1:
    deci_get()
  elif FROM == 2:
    bina_get()
  elif FROM == 3:
    hexa_get()
  elif FROM == 4:
    octa_get()
  else:
    print('This is a catastrophe!')
  
  if INTO == 1:
    deci_convert(holder, FROM)
  elif INTO == 2:
    bina_convert(holder, FROM)
  elif INTO == 3:
    hexa_convert(holder, FROM)
  elif INTO == 4:
    octa_convert(holder, FROM)
  else:
    print('This is another catastrophe!')
    
  check = int(input('''To try another number type '1'.
                   To to exit type '2'.'''))
  if check == 1:
    loop == True
    os.system('cls')
    print('Restarting')
  elif check == 2:
    loop == False
    print('Goodbye')
    os.system('cls')
    
