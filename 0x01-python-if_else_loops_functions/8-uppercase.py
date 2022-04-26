#!/usr/bin/python3
def uppercase(str):
    str2 = ""
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            str2 += chr(ord(str[i]) - 32)
            continue
        str2 += str[i]

    print("{}".format(str2))
