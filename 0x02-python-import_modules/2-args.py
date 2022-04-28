#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print(f"0 arguments.")
    elif len(argv) == 2:
        print(f"{len(argv) - 1} argument: ")
        print(f"{len(argv) - 1}: {argv[1]}")
    elif len(argv) > 2:
        print(f"{len(argv) - 1} arguments: ")
        for i in range(0, len(argv) - 1):
            print(f"{i}: {argv[i]}")
