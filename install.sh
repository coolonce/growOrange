#!/bin/bash
echo fff
echo http://downloads.arduino.cc/arduino-1.5.7-linux64.tgz
if [[ -f `which picocom` && -f `which arduino` ]]; then
    arduino latest/latest.ino --verify --upload --port /dev/ttyS3
else
    sudo apt install picocom && cd /tmp &&
    tar -zxvf arduino-1.5.7-linux64.tgz && mv arduino-1.5.7 ~/arduino-ide && chmod +x ~/arduino-ide/arduino ## &&
##    ln -s  /usr/bin/arduino ~/arduino-ide/arduino
fi
### wget http://downloads.arduino.cc/arduino-1.5.7-linux64.tgz
