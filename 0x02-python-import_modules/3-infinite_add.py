#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numbers = len(sys.argv) - 1
    result = 0
    for i in range(numbers):
        result += int(sys.argv[i + 1])
    print(f"{result}")
