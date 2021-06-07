def search(arr, k):
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2
    while low <= high:
        if k > arr[mid]:
            low = mid + 1
        elif k < arr[mid]:
            high = mid - 1
        else:
            break
        mid = (low + high) // 2
    if k != arr[mid]:
        mid += 1
    return mid


def search_arr(arr1, arr2, l):
    low = 0
    high = len(arr1) - 1
    mid = (low + high) // 2
    while low <= high:
        place = search(arr2, arr1[mid]) + mid
        if place == l:
            return arr1[mid]
        if place > l:
            high = mid - 1
        else:
            low = mid + 1
        mid = (low + high) // 2
    return None


def median(a, b):
    na = len(a)
    nb = len(b)
    needed = [(na + nb) // 2]
    found = [None]
    if (na + nb) % 2 == 0:
        needed.append(needed[0] - 1)
        found.append(None)
    for i in range(len(needed)):
        f = (search_arr(a, b, needed[i]))
        if f is not None:
            found[i] = f
    for i in range(len(needed)):
        if found[i] is not None:
            continue
        f = (search_arr(b, a, needed[i]))
        if f is not None:
            found[i] = f
    print(found)


median([1, 2, 3], [4, 5, 6])
