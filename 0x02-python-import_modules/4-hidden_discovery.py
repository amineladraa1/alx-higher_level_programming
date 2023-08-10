#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    directory = dir(hidden_4)
    for d in directory:
        if d[:2] != "__":
            print(d)
