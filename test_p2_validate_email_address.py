from unittest import TestCase
from unittest.mock import patch
from p2_validate_email_address import *


class TestValidateEmail(TestCase):

    def test_validate_email_address(self):
        user_input = [
            5,
            'clara@example.com',
            'john-doe23@example.com',
            'jane_35@example.com',
            'joe%bloggs@example.com',
            'zhou_37@example.com'
        ]
        expected_result = [
            'clara@example.com', 'jane_35@example.com', 'john-doe23@example.com', 'zhou_37@example.com'
        ]
        with patch('sys.stdin.readline', side_effect=user_input):
            result = validate_email_address()
            self.assertEqual(result, expected_result)
        self.assertCountEqual(result, expected_result)

