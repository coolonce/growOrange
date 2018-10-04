#!/bin/bash
#echo fff
#echo http://downloads.arduino.cc/arduino-1.5.7-linux64.tgz
#if [[ -f `which picocom` && -f `which arduino` ]]; then
    echo upload arduino...
    ~/arduino/arduino --upload ~/growOrange/latest/latest.ino --port /dev/ttyUSB0
#else
#    cd /tmp && wget http://downloads.arduino.cc/arduino-1.5.7-linux64.tgz &&
#    tar -zxvf arduino-1.5.7-linux64.tgz && mv arduino-1.5.7 ~/arduino-ide && 
#    chmod +x ~/arduino-ide/arduino && ln -s  /usr/bin/arduino ~/arduino-ide/arduino
#fi
### wget http://downloads.arduino.cc/arduino-1.5.7-linux64.tgz
