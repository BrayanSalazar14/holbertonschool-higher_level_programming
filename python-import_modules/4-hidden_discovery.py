#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    name = dir(hidden_4)
    if name[2:] != "__":
        for i in name:
            print("{}".format(name[i]))
