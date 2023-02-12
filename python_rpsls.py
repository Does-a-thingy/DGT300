#importing commands from the 'random' module in a way so I don't have to write 'random.' every time.
from random import *

# 0 = rock > 3, > 2, < 1, < 4
# 1 = paper < 3, < 2, > 0, > 4
# 2 = scissor > 3, > 1, < 0, < 4 
# 3 = lizard > 4, > 1, < 2, < 0
# 4 = spock < 3, < 1, > 0, > 2

# variable set up
player_option = 0
comp_option = randint(0,4)

# first command prompt
while True:
  player_option = int(input('''Please type:
  '0' for rock
  '1' for paper
  '2' for scissor
  '3' for lizard
  '4' for spock
  '''))
  if player_option <= 4 and player_option >= 0:
    break
  else:
    print('Please try again')

# results
if player_option == 0 and (comp_option == 3 or comp_option == 2):
  print('player wins')
elif player_option == 0 and (comp_option == 1 or comp_option == 4):
  print('computer wins')
elif player_option == 1 and (comp_option == 0 or comp_option == 4):
  print('player wins')
elif player_option == 1 and (comp_option == 3 or comp_option == 2):
  print('computer wins')
elif player_option == 2 and (comp_option == 1 or comp_option == 3):
  print('player wins')
elif player_option == 2 and (comp_option == 0 or comp_option == 4):
  print('computer wins')
elif player_option == 3 and (comp_option == 1 or comp_option == 4):
  print('player wins')
elif player_option == 3 and (comp_option == 2 or comp_option == 0):
  print('computer wins')
elif player_option == 4 and (comp_option == 0 or comp_option == 2):
  print('player wins')
elif player_option == 4 and (comp_option == 1 or comp_option == 3):
  print('computer wins')
else:
  print('If your seeing this then it means that my spagetti is Al dente')
