def remove_dup(inputlist):
    list(set(inputlist))
    s = set()
    remove_dup = list(set(inputlist) - set(s))
    print(remove_dup)
    return remove_dup


def main():
    while True:
        try:
            l1 = input("enter list: ")
            if len(l1) < 1:
                print ("Please enter a list")
            else:
                remove_dup(l1)

        except KeyboardInterrupt:
            return False


if __name__ == '__main__':
    main()
