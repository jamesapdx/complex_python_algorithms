#!/usr/bin/python

# fun python one-liner, by Jim Shaffer
# chmod 755 starry_night_screensaver.py
# run this script as ./starry_night_screensaver.py

import random,time,shutil,sys;sys.tracebacklimit=0;c=shutil.get_terminal_size();print('\n'*c[1]);l=lambda :print(''.join(' .*^~+o'[random.choices(range(7),weights=[200]+[9]+[1]*5)[0]] for i in range(c[0]-1))) or time.sleep(2) or l(); l()

"""
or copy and paste this one-liner to the linux command line:

python -c "import random,time,shutil,sys;sys.tracebacklimit=0;c=shutil.get_terminal_size();print('\n'*c[1]);l=lambda :print(''.join(' .*^~+o'[random.choices(range(7),weights=[200]+[9]+[1]*5)[0]] for i in range(c[0]-1))) or time.sleep(2) or l(); l()"

"""
