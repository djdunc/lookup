# Notes on setting up

Hardware: FLIR Lepton 2.5 on dev board 1.4 with RPi 4

Based on info from:

https://learn.sparkfun.com/tutorials/flir-lepton-hookup-guide/all 

https://github.com/groupgets/pylepton 

Connected camera using pin out diagram - note the sparkfun shows a smaller GPIO connector so make sure to get correct pins

## Setup up std RPi 
used raspi-config to enable VNC, SPI and I2C (latter two are for Lepton connection)

installed opencv and numpy

```
sudo pip install numpy
sudo pip install opencv-python
```

downloaded pylepton module and ran install:
```
wget https://github.com/groupgets/pylepton/archive/refs/heads/master.zip
```

unzipped it into home/pi folder, moved into pylepton-master folder and installed:

```
cd pylepton-master/
sudo python setup.py install
```

couldnt get simple python example working so installed qt5 

```
sudo apt install qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools
```

and then tried 
https://github.com/groupgets/LeptonModule 
all worked fine (after getting GPIO wired up correctly!)

back to getting python version working - was getting message to long error - tried this:
https://github.com/groupgets/pylepton/issues/52 

Edit /boot/cmdline.txt and add in the end:
```
spidev.bufsiz= 65535
```
Then reboot your raspberry and check it worked with:

```
cat /sys/module/spidev/parameters/bufsiz
```


added in second ssid to:
```
/etc/wpa_supplicant/wpa_supplicant.conf
```

used: 
wpa_passphrase YOURSSID YOURPASSWORD
to generate passphrase on pi

also added in UCL_IoT

## Autorun

Getting to run on start up - didnt use crontab since needed to have GUI running first to use cv2

```
/usr/bin/python /home/pi/pylepton-master/exhibition_lepton.py
sudo chmod a+x 
```

needed to wait for GUI to start up so ran as part of LXDE startup:
https://www.raspberrypi-spy.co.uk/2014/05/how-to-autostart-apps-in-rasbian-lxde-desktop/ 

added the following to bottom of:
```
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```

```
@lxterminal -e /usr/bin/python /home/pi/pylepton-master/exhibition_lepton.py
```