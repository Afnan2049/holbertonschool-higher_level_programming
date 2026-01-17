#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Get all names defined in the module
    names = dir(hidden_4)

    # Sort the names alphabetically
    names.sort()

    # Print names that do not start with "__"
    for name in names:
        if name[:2] != "__":
            print("{}".format(name))
