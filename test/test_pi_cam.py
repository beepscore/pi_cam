#!/usr/bin/env python3

import unittest
import pi_cam


class TestPiCam(unittest.TestCase):

    def setUp(self):
        self.pi_cam = pi_cam.PiCam()

    def test_init(self):
        self.assertIsNotNone(self.pi_cam)

    def test_camera(self):
        self.assertIsNotNone(self.pi_cam.camera)
        self.assertTrue(self.pi_cam.camera.hflip)
        self.assertTrue(self.pi_cam.camera.vflip)

    def test_take_picture(self):
        self.pi_cam.take_picture(self.pi_cam.camera, "test_image.jpg")

if __name__ == "__main__":
    unittest.main()
