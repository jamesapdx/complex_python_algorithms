#!/usr/bin/python

# fun python one-liner, by Jim Shaffer
# chmod 755 starry_night_screensaver.py
# run this script as ./starry_night_screensaver.py

##################################################################################################################################
# Python One-Liner
import random,time,shutil,sys;sys.tracebacklimit=0;c=shutil.get_terminal_size();print('\n'*c[1]);l=lambda :print(''.join(' .*^~+o'[random.choices(range(7),weights=[200]+[9]+[1]*5)[0]] for i in range(c[0]-1))) or time.sleep(2) or l(); l()

##################################################################################################################################
# Linux command line:
"""
or copy and paste this one-liner to the linux command line:

python -c "import random,time,shutil,sys;sys.tracebacklimit=0;c=shutil.get_terminal_size();print('\n'*c[1]);l=lambda :print(''.join(' .*^~+o'[random.choices(range(7),weights=[200]+[9]+[1]*5)[0]] for i in range(c[0]-1))) or time.sleep(2) or l(); l()"

"""

##################################################################################################################################
# below is the one-liner streched out and explaned. this is fully functional, to use just comment the one-liner above

import random,time,shutil,sys
sys.tracebacklimit=0
c=shutil.get_terminal_size()                 # assign the terminal size to the variable 'c', c = [width, height]
print('\n'*c[1])                             # clear the screen by printing blank lines, c[1] = terminal height

# to maintain a one-liner, we must combine a bunch of commands into a recursive lambda
# traditionally lambdas can only call one command, we can get around this limitation by separating with 'or'
# each iteration of this recursive lambda will print an entire line of stars and space objects
l=lambda :(
           print(
                 ''.join(
                         ' .*^~+o'[random.choices(range(7),weights=[200]+[9]+[1]*5)[0]]
#                        ^-------^^---------------------------------------------------^
#                        randomly pick a blank space or star object, manually weighted
                         for i in range(c[0]-1))    # loop through the screen width
                ) or
           time.sleep(2) or                  # sleep each iteration
           l()                               # make this lambda recursive
          )
l()                                          # start the lambda
