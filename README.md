Small script for controlling mpd on orange pi zero 

intstruction:
============

* copy mpdremote.service and python_mpd.py to system (/etc/systemnd/system, and /usr/bin)
```bash
apt get install python3-evdev
systemctl daemon-reload
systemctl enable pdremote.service
systemctl start pdremote.service
```
