#!/usr/bin/python

# fun python one-liner, by Jim Shaffer
# better to run with green text on black background, for obvious reasons
# chmod 755 digital_world_screensaver.py
# run this script as ./digital_world_screensaver.py

import datetime as d,shutil,time,sys,random as r;sys.tracebacklimit=0;v=lambda k,v:globals().__setitem__(k,v);v('c',shutil.get_terminal_size());print('\n'*c[1]);l=lambda :v('t',d.datetime.now()) or r.seed(t.hour) or v('a',r.randint(1,10**c[0])) or r.seed() or print(''.join('    '[:int(x)%3]+(' '[:t.minute%2]+chr(r.randint(35,91))+' ')[min(1,int(t.second/((int(x)+1)*6)))] for x in str(a))[:c[0]-1]) or time.sleep(1) or l();l()

"""
or copy and paste this one-liner to the linux command line:

python -c "import datetime as d,shutil,time,sys,random as r;sys.tracebacklimit=0;v=lambda k,v:globals().__setitem__(k,v);v('c',shutil.get_terminal_size());print('\n'*c[1]);l=lambda :v('t',d.datetime.now()) or r.seed(t.hour) or v('a',r.randint(1,10**c[0])) or r.seed() or print(''.join('    '[:int(x)%3]+(' '[:t.minute%2]+chr(r.randint(35,91))+' ')[min(1,int(t.second/((int(x)+1)*6)))] for x in str(a))[:c[0]-1]) or time.sleep(1) or l();l()"
"""
