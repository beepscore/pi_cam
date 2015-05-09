#!/usr/bin/env python3

import picamera

camera = picamera.PiCamera()

# take a picture
image_name = 'image.jpg'
camera.capture(image_name)

