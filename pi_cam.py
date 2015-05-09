#!/usr/bin/env python3

import picamera

camera = picamera.PiCamera()

# camera properties default values
# camera.sharpness = 0
# camera.contrast = 0
# camera.brightness = 50
# camera.saturation = 0
# camera.ISO = 0
# camera.video_stabilization = False
# camera.exposure_compensation = 0
# camera.exposure_mode = 'auto'
# camera.meter_mode = 'average'
# camera.awb_mode = 'auto'
# camera.image_effect = 'none'
# camera.color_effects = None
# camera.rotation = 0
# camera.hflip = False
camera.hflip = True
# camera.vflip = False
camera.vflip = True
# camera.crop = (0.0, 0.0, 1.0, 1.0)

# take a picture
image_name = 'image.jpg'
camera.capture(image_name)
