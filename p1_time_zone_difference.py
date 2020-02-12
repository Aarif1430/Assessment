from sys import stdin
from datetime import datetime


def diff_in_seconds_tz():
    datetime_format = '%a %d %b %Y %H:%M:%S %z'
    num_test_cases = int(stdin.readline())
    timezone_diff_list = []
    for i in range(num_test_cases):
        t1 = datetime.strptime(stdin.readline().rstrip(), datetime_format)
        t2 = datetime.strptime(stdin.readline().rstrip(), datetime_format)
        timezone_diff_seconds = abs(int(((t1 - t2).total_seconds())))
        print('\n%d' % timezone_diff_seconds)
        timezone_diff_list.append(timezone_diff_seconds)
    return timezone_diff_list


if __name__ == '__main__':
    diff_in_seconds_tz()