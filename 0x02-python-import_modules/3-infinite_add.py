#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    index = len(argv)
    if index == 1:
        print("0")
    else:
        Sum = 0
        for i in range(1, index):
            Sum += int(argv[i])
            print("{}".format(Sum))
