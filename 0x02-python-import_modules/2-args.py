#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argstr = ""
    lenth = len(argv) - 1
    if lenth == 1:
        argstr = "argument"
    else:
        argstr = "arguments"
    if lenth == 0:
        print("{:d} {}.".format(lenth, argstr))
    else:
        print("{:d} {}:".format(lenth, argstr))
        for i in range(lenth):
            print("{:d}: {}".format(i + 1, argv[i + 1]))

