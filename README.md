Steve Baker Beepscore LLC

# Purpose
Record info about using Raspberry Pi camera with Python.

# References

## Python picamera
https://www.raspberrypi.org/documentation/usage/camera/python/README.md

## MotionEyeOS
Web front end for motion, designed for single board computer like Raspberry Pi
Dependencies motion, tornado
https://github.com/ccrisan/motioneyeos/wiki

https://www.raspberrypi.org/magpi/raspberry-pi-night-vision-camera-hack/
https://www.raspberrypi.org/magpi-issues/MagPi46.pdf

### Add push notifications to MotionEyeOS
requires a paid subscription to service "Pushover" $4.99
https://www.raspberrypi.org/magpi-issues/MagPi43.pdf

## Motion detection via camera image diff

## PIL Python Imaging Library
last commit 2011, no Python 3 support
https://en.wikipedia.org/wiki/Python_Imaging_Library

## Pillow
http://pillow.readthedocs.io/en/latest/
active fork of PIL Python Imaging Library
supports Raspbian Jessie Python 3.4

### python-imaging-tk made by raspberry pi community
sudo apt-get install python-imaging-tk

### motion
https://www.maketecheasier.com/setup-motion-detection-webcam-ubuntu/
https://github.com/Motion-Project/motion

#### maybe this is a similar library with the same name
http://bogdanmarian.com/motion/


#### surveillance camera
http://www.codeproject.com/Articles/665518/Raspberry-Pi-as-low-cost-HD-surveillance-camera

#### baby monitor
https://www.raspberrypi.org/blog/raspberry-pi-baby-monitor/
http://stuffbabiesneed.com/blog/building-raspberry-pi-baby-monitor-part-one/

http://shallowsky.com/blog/tags/crittercam/

## Motion detection via PIR sensor
https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/

https://learn.adafruit.com/adafruits-raspberry-pi-lesson-12-sensing-movement


## Equipment

### Raspberry Pi 2 - Model B - ARMv7 with 1G RAM
http://www.adafruit.com/products/2358

### Camera
Raspberry Pi NoIR Camera Board - Infrared-sensitive Camera
http://www.adafruit.com/products/1567

### PIR (motion) sensor
Vetco VUPN5943  
TODO check output voltage
similar to Adafruit 189  
http://www.adafruit.com/products/189  
Adafruit sensor output is 3.3 V, compatible with pi


# Results

## install python camera module
    sudo apt-get install python3-picamera

python3-picamera was already installed.
May have been installed by raspi-config when I enabled camera.

## Run unit tests
To run tests in terminal, cd to top level directory that contains subdirectory test

    pi@pika:~/beepscore/pi_cam $ python3 -m unittest discover test
    .......
    ----------------------------------------------------------------------
    Ran 7 tests in 1.174s

## Copy files from pi images directory to mac
From macOS terminal

    cd ~/Desktop
    scp -r pi@192.168.2.3:~/beepscore/pi_cam/images .
