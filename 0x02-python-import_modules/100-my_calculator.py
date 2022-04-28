#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv[1:]
    argv_count = len(argv)
    operators = ["+", "-", "*", "/"]
    if argv_count is not 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]
        if operator == "+":
            print(f"{a} {operator} {b} = {add(a,b)}")
        elif operator == "-":
            print(f"{a} {operator} {b} = {sub(a,b)}")
        elif operator == "*":
            print(f"{a} {operator} {b} = {mul(a,b)}")
        elif operator == "/":
            print(f"{a} {operator} {b} = {div(a,b)}")
