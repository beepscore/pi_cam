#!/usr/bin/env python3

import unittest
import re
import file_utils


class TestFileUtils(unittest.TestCase):

    def setUp(self):
        pass
       
    def test_timestamp_string(self):
        actual = file_utils.FileUtils.timestamp_string()
        # TODO: Update test by year 2020
        self.assertEqual("201", actual[0:3])
        self.assertTrue("T" in actual)

    def test_timestamp_string_ending(self):
        actual = file_utils.FileUtils.timestamp_string()
        # seconds decimal point . followed by 6 digits at end of string
        regex = re.compile(r"\.\d{6}$")
        # use findall to get list
        # alternatively could use search not match when not matching beginning of string
        # https://docs.python.org/3.3/howto/regex.html 
        matches = regex.findall(actual)
        self.assertEqual(1, len(matches))


if __name__ == "__main__":
    unittest.main()
