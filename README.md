# complex_python_algorithms
Python one-liners that I created from scratch utilizing complex algorithms and math.
Why just one line? The fun is in the challenge.

# Description
### [digital_world_screensaver.py](https://github.com/jamesapdx/fun_python/blob/master/digital_world_screensaver.py)

[![live](https://github.com/jamesapdx/fun_python/raw/master/screenshots/thumbnails/Screenshot_digital_world_th.png)](https://github.com/jamesapdx/fun_python/raw/master/screenshots/Screenshot_digital_world.png)

With a not so simple ***single line*** python command, run a falling characters screensaver in the terminal. Best viewed with
green text on a black background. A detailed explantion of the code is in the script.

Either run the python script or copy, paste, and run this bash command:
```
python -c "import datetime as d,shutil,time,sys,random as r;sys.tracebacklimit=0;v=lambda k,v:globals().__setitem__(k,v);v('c',shutil.get_terminal_size());print('\n'*c[1]);l=lambda :v('t',d.datetime.now()) or r.seed(t.hour) or v('a',r.randint(1,10**c[0])) or r.seed() or print(''.join('    '[:int(x)%3]+(' '[:t.minute%2]+chr(r.randint(35,91))+' ')[min(1,int(t.second/((int(x)+1)*6)))] for x in str(a))[:c[0]-1]) or time.sleep(1) or l();l()"
```

### [starry_night_screensaver.py](https://github.com/jamesapdx/fun_python/blob/master/starry_night_screensaver.py)

[![live](https://github.com/jamesapdx/fun_python/raw/master/screenshots/thumbnails/Screenshot_starry_night_th.png)](https://github.com/jamesapdx/fun_python/raw/master/screenshots/Screenshot_starry_night.png)

This ***single line*** python command will run an elegant starry night screensaver in the terminal.

Either run the python script or copy, paste, and run this bash command:
```
python -c "import random,time,shutil,sys;sys.tracebacklimit=0;c=shutil.get_terminal_size();print('\n'*c[1]);l=lambda :print(''.join(' .*^~+o'[random.choices(range(7),weights=[200]+[9]+[1]*5)[0]] for i in range(c[0]-1))) or time.sleep(2) or l(); l()"
```
