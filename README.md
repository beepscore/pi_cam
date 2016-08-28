Steve Baker Beepscore LLC

# Purpose
Record info about using Raspberry Pi camera with Python.

# References

### Python picamera
https://www.raspberrypi.org/documentation/usage/camera/python/README.md

### Motion sensor
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
