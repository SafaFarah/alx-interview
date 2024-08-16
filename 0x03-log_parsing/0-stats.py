#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics"""
import sys
import signal

total_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Print the total file size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_count):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")


def handle_interrupt(signal, frame):
    """Handle keyboard interrupt (CTRL+C)."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)
try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) > 6:
            try:
                status_code = int(parts[5])
                file_size = int(parts[6])
                if status_code in status_count:
                    status_count[status_code] += 1
                total_size += file_size
                line_count += 1
                if line_count % 10 == 0:
                    print_stats()
            except ValueError:
                continue
except KeyboardInterrupt:
    print_stats()
