#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i <= x:
            print("{}".format(my_list[i]), end="")
            i += 1;
        print("\n");
    except Exception as err:
        print("an err accured : {}".format(err));
    return i
