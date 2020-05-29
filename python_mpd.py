#!/usr/bin/python3
from evdev import InputDevice
from time import time
import logging,os
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
KEY_0     = { "command":"", "repeat":300,"time":0}
KEY_1     = { "command":"", "repeat":300,"time":0}
KEY_2     = { "command":"", "repeat":300,"time":0}
KEY_3     = { "command":"", "repeat":300,"time":0}
KEY_4     = { "command":"", "repeat":300,"time":0}
KEY_5     = { "command":"", "repeat":300,"time":0}
KEY_6     = { "command":"", "repeat":300,"time":0}
KEY_7     = { "command":"", "repeat":300,"time":0}
KEY_8     = { "command":"", "repeat":300,"time":0}
KEY_9     = { "command":"", "repeat":300,"time":0}
KEY_UP    = { "command":"mpc volume +2", "repeat":200,"time":0}
KEY_DOWN  = { "command":"mpc volume -2", "repeat":200,"time":0}
KEY_LEFT  = { "command":"mpc prev", "repeat":500,"time":0}
KEY_RIGHT = { "command":"mpc next", "repeat":500,"time":0}
KEY_OK    = { "command":"mpc toggle", "repeat":300,"time":0}
KEY_STAR  = { "command":"", "repeat":300,"time":0}
KEY_SIGN  = { "command":"", "repeat":300,"time":0}

events = {
25: KEY_0,
69: KEY_1,
70: KEY_2,
71: KEY_3,
68: KEY_4,
64: KEY_5,
67: KEY_6,
7: KEY_7,
21: KEY_8,
9: KEY_9,
28: KEY_OK,
24: KEY_UP,
82: KEY_DOWN,
8: KEY_LEFT,
90: KEY_RIGHT,
22: KEY_STAR,
13: KEY_SIGN,
}

eventime={}
proc={}
irr = InputDevice('/dev/input/event0')


logging.debug("Press remote IR buttons, Ctrl-C to quit")

for event in irr.read_loop():
   if event.type == 4:
      try:
         if event.value == 25:
            print("test")
            logging.debug(proc)
         if event.value in events:
            if events[event.value]["command"] != "":
               now=int(time()*1000.0)
               if ((now - events[event.value]["time"]) > events[event.value]["repeat"] ):
                  os.system(events[event.value]["command"])
                  logging.debug (events[event.value]["command"])
                  events[event.value]["time"] = now
               else: logging.debug("too soon")
            else: logging.debug("nothing to do")
         else:
            logging.debug(event)
      except:
         logging.error("Problem key pressed...")
