#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

fswebcam -r 1280x720 --no-banner --device /dev/video1 /home/pi/Seed/pictures/$DATE.jpg