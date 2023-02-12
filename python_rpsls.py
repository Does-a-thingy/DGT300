#importing commands from the 'random' module in a way so I don't have to write 'random.' every time.
from random import *

# 0 = rock
# 1 = paper
# 2 = scissor
# 3 = lizard
# 4 = spock

# variable set up
player_option = 0
comp_option = 0

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
