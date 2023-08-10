#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    operations = {"+": add, "-": sub, "*": mul, "/": div}

    if op not in list(operations.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    fop = int(sys.argv[1])
    sop = int(sys.argv[3])
    print("{} {} {} = {}".format(fop, op, sop, operations[op](fop, sop)))
