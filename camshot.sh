#!/bin/bash

web_cam="/dev/video0";

scale="640x480";

photo_path="/home/swpi/webcam_photo";

if [[ -f `which fswebcam` ]]; then

if ! [[ -d $photo_path ]] ; then

mkdir -p $photo_path ;
fi

fswebcam -d $web_cam -S $s -F $f -r $scale -q $photo_path/`date +%d-%m-%y_%H-%M-%S`_$HOSTNAME.jpg
else
sudo apt install fswebcam
fi

exit 0;
