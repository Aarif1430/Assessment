from unittest import TestCase
from unittest.mock import patch
from p1_time_zone_difference import *


class TestDiffZoneSeconds(TestCase):

    def test_diff_in_seconds_tz(self):
        user_input = [
            3,
            'Sun 10 May 2015 13:54:36 -0700',
            'Sun 10 May 2015 13:54:36 -0000',
            'Sat 02 May 2015 19:54:36 +0530',
            'Fri 01 May 2015 13:54:36 -0000',
            'wed 05 Jun 2015 13:54:36 -0900',
            'wed 05 Jun 2015 13:54:36 -0000'
        ]
        expected_result = [
            25200,
            88200,
            32400
        ]
        with patch('sys.stdin.readline', side_effect=user_input):
            result = diff_in_seconds_tz()
            for i, res in enumerate(result):
                self.assertEqual(res, expected_result[i])

