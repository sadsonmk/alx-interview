#!/usr/bin/python3
"""This is a module for a python Interview question for a log parsing"""


import re
import signal
import sys


total_size = 0
line_count = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def print_stats(signal=None, frame=None):
    """Function to print the statistics of file size and status codes"""

    print(f'File size: {total_size}')
    for value in sorted(status_codes.keys()):
        if status_codes[value] > 0:
            print(f'{value}: {status_codes[value]}')
    if signal is not None:
        sys.exit()


signal.signal(signal.SIGINT, print_stats)

for line in sys.stdin:
    try:
        section = re.search(' - \\[.+\\] "GET \
                /projects/260 HTTP/1.1" (\\d+) (\\d+)', line)
        status_code = int(section.group(1))
        file_size = int(section.group(2))

        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats()
    except Exception:
        continue

print_stats()
