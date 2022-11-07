#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    # start = 0
    # for i in range(0, x):
    #     try:
    #         print(my_list[i], end="")
    #         start += 1
    #     except IndexError:
    #         pass

    # print()

    # return start

    # not very good writing, but works
    try:
        count = 0
        for n in range(x):
            print(my_list[n], end="")
            count = count + 1
        print()
        return count
    except:
        print()
        return count
