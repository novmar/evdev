#/bin/bash
echo nec >/sys/class/rc/rc0/protocols
echo "@reboot echo nec | sudo tee /sys/class/rc/rc0/protocols" >> /var/spool/cron/crontabs/root
apt install python3-evdev
cp python_mpd.py /usr/bin/
cp mpdremote.service /etc/systemd/system
chmod +x /usr/bin/python_mpd.py
systemctl daemon-reload
systemctl enable pdremote.service
systemctl start pdremote.service
