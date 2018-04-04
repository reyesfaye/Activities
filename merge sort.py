def merge(left, right, a):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1

        else:
            a[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


def merge_sort(a):
    left = []
    right = []
    n = len(a)
    if n < 2 :
        return
    mid = n / 2
    for i in range(mid):
        left.append(a[i])
    for i in range(mid, n):
        right.append(a[i])

    merge_sort(left)
    merge_sort(right)
    merge(left, right, a)


a = [2, 4, 1, 3, 8, 9, 0, -2, -1]
merge_sort(a)
print a
