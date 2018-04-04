print ('Sorted List')


def selection_sort(aList):
    for i in range(len(aList)):
        least = i
        for k in range(i + 1, len(aList)):
            if aList[k] < aList[least]:
                least = k

        swap(aList, least, i)


def swap(a, x, y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp


my_list = [13.15, 13.13, 2.05, 22.96, 26.91, 8.03, 27.03, 2.08, 11.13, 9.20, 1.09]
selection_sort(my_list)
print (my_list)

print ('Search')


def binary_search(number, target):
    low = 0
    mid = len(number) / 2
    upper = len(number)

    if len(number) == 1:
        if number[0] == target:
            print target
            return number[0]
        else:
            return False
    if target == number[mid]:
        print number[mid]
        return mid
    else:
        if mid > low:
            number1 = number[0:mid]
            binary_search(number1, target)

        if upper > mid:
            number2 = number[mid:len(number)]
            binary_search(number2, target)


if __name__ == "__main__":
    a = [2, 5, 7, 8, 9, 4, 3, 2, 5, 6, 1]
    binary_search(a, 9)
