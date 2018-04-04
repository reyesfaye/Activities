mylist = [26, 11, 13, 8, 9, 96]


def bubble(badList):
    length = len(badList) - 1
    unsorted = True

    while unsorted:
        for element in range(0,length):
            unsorted = False
            if badList[element] > badList[element + 1]:
                hold = badList[element + 1]
                badList[element + 1] = badList[element]
                badList[element] = hold
                print badList
            else:
                unsorted = True

print bubble(mylist)