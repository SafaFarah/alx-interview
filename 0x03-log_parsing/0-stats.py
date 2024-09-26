#!/usr/bin/python3
"""
A script that reads log entries from stdin and computes metrics.
"""


import sys


def main():
    """
    The main function that executes the log parsing and metrics calculation.
    """
    total_file_size = 0
    status_codes = {}
    line_count = 0
    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                total_file_size += file_size
                if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
                    status_codes[status_code] = status_codes.get(
                            status_code, 0) + 1
                if line_count % 10 == 0:
                    print_statistics(total_file_size, status_codes)
            except (ValueError, IndexError):
                continue
        print_statistics(total_file_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_codes)


def print_statistics(total_file_size, status_codes):
    """
    Prints the total file size and counts of status codes.
    Args:
        total_file_size (int): The total size of files processed.
        status_codes (dict): A dictionary with status codes and their counts.
    """
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")


if __name__ == "__main__":
    main()
