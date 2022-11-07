#!/usr/bin/python3

def safe_print_division(a, b):

    # new
    try:
        c = a/b
    except ZeroDivisionError:
        c = None
    finally:
        print("Inside result: {}".format(c))
    if c is None:
        return c

    return c  # this will return if c is not None

    # older code is better writing wise

    # try:
    #     result = a / b
    #     return result
    # except (ZeroDivisionError):
    #     result = None
    #     return result
    # finally:
    #     print("Inside result: {}".format(result))
