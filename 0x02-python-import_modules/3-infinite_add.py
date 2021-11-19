#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    index = len(sys.argv)
    if index == 1:
        print("0")
    else:
        totalSum = 0
        for i in range(1, index):
            totalSum = totalSum + int(sys.argv[i])
            print("{}".format(totalSum))
