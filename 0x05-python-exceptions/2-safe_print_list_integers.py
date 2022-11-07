#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    # new
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count = count + 1
        except ValueError:
            pass
        except TypeError:
            pass
    print()
    return count

    # old
    # start = 0
    # for i in range(0, x):
    #     try:
    #         print("{:d}".format(my_list[i]), end="")
    #         start += 1
    #     except (TypeError, ValueError): 2 exceptions in one line
    #         continue

    # print()

    # return start
