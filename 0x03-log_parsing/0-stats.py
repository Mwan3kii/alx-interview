#!/usr/bin/python3
"""Log parsing"""
import sys
import signal

# Initialize counters and accumulators
if __name__ == '__main__':
    total_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
        }
    line_count = 0

    def print_stats():
        """Print current statistics"""
        print(f"File size: {total_size}")
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print(f"{code}: {status_codes[code]}")

    def signal_handler(sig, frame):
        """Handle keyboard interruption"""
        print_stats()
        sys.exit(0)

    # Register the signal handler for keyboard interruption
    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 7:
                continue
            ip_address = parts[0]
            status_code = parts[-2]
            file_size = parts[-1]

            if status_code in status_codes:
                status_codes[status_code] += 1

            try:
                total_size += int(file_size)
            except ValueError:
                continue
            line_count += 1
            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
