#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    # new
    lst = []
    for i in range(0, list_length):
        try:
            c = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
            print("division by zero")
            c = 0
        except TypeError:
            print("wrong type")
            c = 0
        except IndexError:
            print("out of range")
            c = 0
        finally:
            lst.append(c)
    return lst

    # old
    # newlist = []
    # result = 0

    # for i in range(0, list_length):
    #     try:
    #         result = my_list_1[i] / my_list_2[i]
    #     except ZeroDivisionError:
    #         print("division by 0")
    #         result = 0
    #     except TypeError:
    #         print("wrong type")
    #         result = 0
    #     except IndexError:
    #         print("out of range")
    #         result = 0
    #     finally:
    #         newlist.append(result)

    # return newlist
