#!/usr/bin/python

# complex python one-liner, by Jim Shaffer
# better to run this with green text on black background, for obvious reasons
# chmod 755 digital_world_screensaver.py
# run this script as ./digital_world_screensaver.py

import datetime as d,shutil,time,sys,random as r;sys.tracebacklimit=0;v=lambda k,v:globals().__setitem__(k,v);v('c',shutil.get_terminal_size());print('\n'*c[1]);l=lambda :v('t',d.datetime.now()) or r.seed(t.hour) or v('a',r.randint(1,10**c[0])) or r.seed() or print(''.join('    '[:int(x)%3]+(' '[:t.minute%2]+chr(r.randint(35,91))+' ')[min(1,int(t.second/((int(x)+1)*6)))] for x in str(a))[:c[0]-1]) or time.sleep(1) or l();l()

"""
or copy and paste this one-liner to the linux command line:

python -c "import datetime as d,shutil,time,sys,random as r;sys.tracebacklimit=0;v=lambda k,v:globals().__setitem__(k,v);v('c',shutil.get_terminal_size());print('\n'*c[1]);l=lambda :v('t',d.datetime.now()) or r.seed(t.hour) or v('a',r.randint(1,10**c[0])) or r.seed() or print(''.join('    '[:int(x)%3]+(' '[:t.minute%2]+chr(r.randint(35,91))+' ')[min(1,int(t.second/((int(x)+1)*6)))] for x in str(a))[:c[0]-1]) or time.sleep(1) or l();l()"
"""

# below is the one-liner streched out and explaned. this is fully functional, to use just comment the one-liner above

import datetime as d,shutil, time, sys, random as r

sys.tracebacklimit=0                         # don't display all the traceback junk with a keyboard interrupt
v=lambda k,v:globals().__setitem__(k,v)      # use this lambda to create/assign a variable without using x=3 notation, because we can't use x=3 inside a lambda
                                             # k = variable name, v = value to assign
v('c',shutil.get_terminal_size())            # assign the terminal size to the variable 'c', c = [width, height]
print('\n'*c[1])                             # clear the screen by printing blank lines, c[1] = terminal height

# to maintain a one-liner, we must combine a bunch of commands into a recursive lambda
# traditionally lambdas can only call one command, we can get around this limitation by separating with 'or'
# each iteration of this recursive lambda will print an entire line of falling characters
l=lambda :(
           v('t',d.datetime.now()) or        # assign a timestamp to the variable 't'
           r.seed(t.hour) or                 # make a random.seed based on hour, this causes the seed and random int to be the same for the whole hour
           v('a',r.randint(1,10**c[0])) or   # generate a really long integer with same number of digits as the screen width. each digit will determine what char to print in that column
           r.seed() or                       # reset the seed so that we can randomize falling chars
           print(
                 ''.join(                    # create a list of spaces and falling chars, then use join to convert to a string
                         '    '[:int(x)%3] + (' '[:t.minute%2]+chr(r.randint(35,91))+' ')[min(1,int(t.second/((int(x)+1)*6)))]
#                        ^----^^---------^   ^------------------------------------------^^-----------------------------------^
#                        add space padding and possibly a random char. for a reducing effect: spacing and char is weighted per minute, second, and a column/digit from the really long int 'a'
                         for x in str(a)             # loop through the really long random int 'a', the step above generates spacing and chars based on the digit and time
                         )[:c[0]-1]          # slice of the total line for just the screen width
                 ) or
          time.sleep(1) or                   # pause per iteration
          l()                                # make recursive to keep looping
          )

l()                                          # start our recursive lambda
