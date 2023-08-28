#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        while (i < x):
            print("{}".format(my_list[i]), end="")
            i++;
    except Exeption as err:
        print("an err accured".format(err));
    finally:
        print("\n");
