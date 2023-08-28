#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        while (i < x):
            print("{}"my_list[i], end="")
            i++;
    except Exeption as err:
        print("x is bigger then the length given");
    finally:
        print("\n");
