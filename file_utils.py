#!/usr/bin/env python3

import datetime

class FileUtils:
    """
    File utilities
    """

    def timestamp_string():
        """ return local time as a string of the form 20150510T152647.888360
        ignore time zone offset
        """
        # utc time
        #timestamp = datetime.datetime.utcnow().isoformat()

        # local time
        # 2015-05-10T15:26:47.888360
        timestamp = datetime.datetime.now().isoformat()

        time_string_no_dashes = timestamp.replace('-', '')
        time_string_no_dashes_no_colons = time_string_no_dashes.replace(':', '')
        return time_string_no_dashes_no_colons
    
    def filename_with_timestamp(basename):
        return basename + FileUtils.timestamp_string()
