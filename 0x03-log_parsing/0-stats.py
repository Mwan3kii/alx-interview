#!/usr/bin/python3
import sys
import signal

# Initialize counters and accumulators
total_size = 0
status_codes_count = {
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
    """ Print the current statistics """
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def signal_handler(sig, frame):
    """ Handle keyboard interruption (CTRL + C) """
    print_stats()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # Split the line into components
        parts = line.split()

        # Validate format (must have 7 parts)
        if len(parts) < 7:
            continue
        
        # Extract values
        ip_address = parts[0]
        status_code = parts[-2]
        file_size = parts[-1]

        # Check if status_code is a valid integer and one of the expected status codes
        if status_code in status_codes_count:
            # Increment the count for this status code
            status_codes_count[status_code] += 1

        # Try to convert file_size to an integer and add to total size
        try:
            total_size += int(file_size)
        except ValueError:
            continue

        # Increment the line count
        line_count += 1

        # Every 10 lines, print the stats
        if line_count % 10 == 0:
            print_stats()


except KeyboardInterrupt:
    print_stats()
    sys.exit(0)