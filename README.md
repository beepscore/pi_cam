Steve Baker Beepscore LLC

# Purpose
Record info about using Raspberry Pi camera with Python.

# References

## Python picamera
https://www.raspberrypi.org/documentation/usage/camera/python/README.md

# Results

## install python module
    sudo apt-get install python3-picamera

python3-picamera was already installed.
May have been installed by raspi-config when I enabled camera.

## Run unit tests
To run tests in terminal, cd to top level directory that contains subdirectory test

    pi-cam git:(master) ✗ python3 -m unittest discover test
    pi@pika ~/beepscore/pi-cam $ python3 -m unittest discover test
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 1.601s
