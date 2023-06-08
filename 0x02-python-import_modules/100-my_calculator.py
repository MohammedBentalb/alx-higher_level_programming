#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul

    ln = len(sys.argv) - 1

    if ln != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if op == "+":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))
    elif op == "-":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))
    elif op == "*":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, mul(a, b)))
    elif op == "/":
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
