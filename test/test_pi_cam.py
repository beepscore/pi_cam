#!/usr/bin/env python3

import unittest
import pi_cam


class TestPiCam(unittest.TestCase):

    def setUp(self):
        self.pi_cam = pi_cam.PiCam()
       
    def tearDown(self):
        """ close camera to avoid error picamera.exc.PiCameraMMALError
	Camera component couldn't be enabled: Out of resources (other than memory)
        http://stackoverflow.com/questions/27468543/
	picamera-cannot-be-initialized-as-a-class-member-when-the-script-is-run-from-com
	"""
        self.pi_cam.camera.close()

    def test_init(self):
        self.assertIsNotNone(self.pi_cam)

    def test_camera(self):
        self.assertIsNotNone(self.pi_cam.camera)
        self.assertTrue(self.pi_cam.camera.hflip)
        self.assertTrue(self.pi_cam.camera.vflip)

    def test_take_picture(self):
        self.pi_cam.take_picture(self.pi_cam.camera, "images", "test_image")

if __name__ == "__main__":
    unittest.main()
