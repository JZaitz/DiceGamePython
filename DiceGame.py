"""This program allows a diceroll and game play versus the computer."""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Please guess a number."))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_value = number_of_sides * 2
  print "The max value is %d"% (max_value)
  if guess > max_value:
 		return "Your guess is invalid."
  else:
    print "Rolling..."
    sleep(2)
    print "The roll is %d"% (first_roll)
    sleep(1)
    print "The second roll is %d"% (second_roll)
    total_roll= first_roll + second_roll
    print total_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "You won!"
    else:
      print "You lost."



guess = get_user_guess()

roll_dice(6)
