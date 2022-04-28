#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if (len(argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
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
