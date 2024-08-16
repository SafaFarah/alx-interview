#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""
import sys
import re
import signal


log_pattern = re.compile(
    r'\d+\.\d+\.\d+\.\d+ - \[.*?\] "GET /projects/260 HTTP/1.1" '
    r'(\d{3}) (\d+)'
)
total_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def print_stats():
    """Print the total file size and status code counts."""
    print(f"File size: {total_size}")
    for status_code in sorted(status_codes.keys()):
        count = status_codes[status_code]
        if count > 0:
            print(f"{status_code}: {count}")


def signal_handler(signal, frame):
    """Handle keyboard interrupt (CTRL+C)."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            try:
                status_code = int(match.group(1))
                file_size = int(match.group(2))
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size
                line_count += 1
                if line_count % 10 == 0:
                    print_stats()
            except ValueError:
                continue
except KeyboardInterrupt:
    print_stats()
except BrokenPipeError:
    sys.exit(0)
