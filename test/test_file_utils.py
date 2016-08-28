#!/usr/bin/env python3

import unittest
import re
import file_utils


class TestFileUtils(unittest.TestCase):

    def setUp(self):
        # seconds decimal point . followed by 6 digits at end of string
        # self.regex_timestamp_end = re.compile(r"\.\d{6}$")
        self.regex_timestamp_end = re.compile(r"\d{8}T\d{6}\.\d{6}$")
        self.regex_filename_end = re.compile(r"\d{8}T\d{6}\.\d{6}\.jpg$")

    def test_timestamp_string(self):
        actual = file_utils.FileUtils.timestamp_string()
        # TODO: Update test by year 2020
        self.assertEqual("201", actual[0:3])

    def test_timestamp_string_end(self):
        actual = file_utils.FileUtils.timestamp_string()
        # use findall to get list
        # alternatively could use search not match when not matching beginning of string
        # https://docs.python.org/3.3/howto/regex_timestamp_end.html 
        matches = self.regex_timestamp_end.findall(actual)
        self.assertEqual(1, len(matches))

    def test_filename_with_timestamp_start(self):
        base_name = "bar"
        actual = file_utils.FileUtils.filename_with_timestamp(base_name)
        self.assertEqual(base_name, actual[0:len(base_name)])

    def test_filename_with_timestamp_end(self):
        base_name = "grizzly"
        actual = file_utils.FileUtils.filename_with_timestamp(base_name)
        matches = self.regex_filename_end.findall(actual)
        self.assertEqual(1, len(matches))

if __name__ == "__main__":
    unittest.main()
