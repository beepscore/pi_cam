#!/usr/bin/env python3

import picamera


class PiCam:
    """
    Uses Raspberry Pi camera.
    """

    def __init__(self):

        self.camera = picamera.PiCamera()

        """ PiCamera properties default values
        camera.sharpness = 0
        camera.contrast = 0
        camera.brightness = 50
        camera.saturation = 0
        camera.ISO = 0
        camera.video_stabilization = False
        camera.exposure_compensation = 0
        camera.exposure_mode = 'auto'
        camera.meter_mode = 'average'
        camera.awb_mode = 'auto'
        camera.image_effect = 'none'
        camera.color_effects = None
        camera.rotation = 0
        camera.hflip = False
        camera.vflip = False
        camera.crop = (0.0, 0.0, 1.0, 1.0)
        """
        self.camera.hflip = True
        self.camera.vflip = True

    def __del__(self):
        """ class destructor.
        Close camera to avoid error picamera.exc.PiCameraMMALError
        Camera component couldn't be enabled: Out of resources (other than memory)
        http://stackoverflow.com/questions/27468543/
        picamera-cannot-be-initialized-as-a-class-member-when-the-script-is-run-from-com
        """
        self.camera.close()

    def take_picture(self, camera, image_name):
        """ Use arguments for dependency injection.
        This way unit tests can call with a mock camera.
        """
        camera.capture(image_name)
