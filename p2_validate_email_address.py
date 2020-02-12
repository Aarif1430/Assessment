from sys import stdin
import re


def validate_email_address():
    num_test_cases = int(stdin.readline())
    valid_emails = []
    for i in range(num_test_cases):
        email = stdin.readline().split('\n')[0]
        if re.search(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+.[a-zA-Z]{1,3}$', email):
            valid_emails.append(email)
    return sorted(valid_emails)


if __name__ == '__main__':
    print(validate_email_address())
