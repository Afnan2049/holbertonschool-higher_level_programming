#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Start the sum at 0
    total_sum = 0

    # Iterate through arguments, skipping the script name (index 0)
    for arg in sys.argv[1:]:
        total_sum += int(arg)

    print("{}".format(total_sum))
