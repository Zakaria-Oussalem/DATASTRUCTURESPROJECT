# Binary search:


def BinaryS(myList: list[float], val: float) -> bool:
    """function searching for value in a list using dichotomy

    Args:
        myList (list): list to look into
        val (float): the value to look for

    Returns:
        bool: If the value exists or not
    """
    if len(myList) == 0:
        return False
    mini = 0
    maxi = len(myList) - 1
    mid = (maxi + mini) // 2

    if val in [myList[mini], myList[mid], myList[maxi]]:
        return True

    if val < myList[mini] or val > myList[maxi]:
        return False

    while maxi - mini > 1:
        if val == myList[mid]:
            return True
        elif myList[mid] < val:
            mini = mid
            mid = (mini + maxi) // 2

        elif myList[mid] > val:
            maxi = mid
            mid = (mini + maxi) // 2

    return False


# recursive version
def BinarySearchR(myList: list[float], val: float) -> bool:

    if len(myList) == 0:
        return False

    mini = 0
    maxi = len(myList) - 1
    mid = (maxi + mini) // 2

    if len(myList) == 0:
        return False

    if val in [myList[mini], myList[mid], myList[maxi]]:
        return True

    if val < myList[mini] or val > myList[maxi]:
        return False

    return BinarySearchR(myList[mini:mid], val) or BinarySearchR(myList[mid:maxi], val)


# Bubble sort:
def bubbleSort(myList: list[float]) -> list[float]:

    if len(myList) == 0:
        return myList
    for j in range(len(myList) - 1):
        swap = False
        for i in range(len(myList) - 1 - j):
            if myList[i] > myList[i + 1]:
                myList[i + 1], myList[i] = myList[i], myList[i + 1]
                swap = True
        if not swap:
            break
    return myList


# Bubble sort for dictionnaries
def bubbleSortDict(myList: list[dict[str, float]], key: str) -> list[dict[str, float]]:

    for j in range(len(myList) - 1):
        swap = False
        for i in range(len(myList) - 1 - j):
            if myList[i][key] > myList[i + 1][key]:
                myList[i + 1], myList[i] = myList[i], myList[i + 1]
                swap = True
        if not swap:
            break
    return myList


# Quick sort using Hoare partitioning
def quickSortH(myList: list[float]) -> list[float]:
    if len(myList) < 2:
        return myList

    pivot = myList[0]
    start = 1
    end = len(myList) - 1

    while start <= end:

        while start < len(myList) and myList[start] <= pivot:
            start += 1

        while myList[end] > pivot:
            end -= 1

        if start < end:
            myList[end], myList[start] = myList[start], myList[end]

    myList[end], myList[0] = pivot, myList[end]
    return (
        quickSortH(myList[:end]) + myList[end : end + 1] + quickSortH(myList[end + 1 :])
    )


# Quick sort using Lotome partitioning
def quickSortL(myList: list[float]) -> list[float]:
    if len(myList) < 2:
        return myList

    pivot = myList[-1]
    p_index = 0
    i = 0

    while p_index < len(myList) - 1 and i < len(myList) - 1:

        while p_index < len(myList) - 1 and myList[p_index] < pivot:
            p_index += 1
        i = p_index
        while i < len(myList) - 1 and myList[i] >= pivot:
            i += 1

        myList[p_index], myList[i] = myList[i], myList[p_index]

    return (
        quickSortL(myList[:p_index])
        + myList[p_index : p_index + 1]
        + quickSortL(myList[p_index + 1 :])
    )


# Insertion sort
def insertionSort(myList: list[float]) -> list[float]:

    if len(myList) < 2:
        return myList

    for pointer in range(len(myList)):
        print(myList)
        pointBack = pointer
        anchor = myList[pointer]
        while True:
            pointBack -= 1
            if pointBack < 0:
                break
            elif myList[pointBack] > anchor:
                myList[pointBack + 1] = myList[pointBack]
            else:
                break

        myList[pointBack + 1] = anchor

    return myList


def runningMedian(myList: list[float]):
    """Function that simulates computing median of a running series
    It simulates online data and uses insertion sort as it is more adapted
    Args:
        myList (list): list of values
    """

    def median(myList: list[float]) -> float:

        if len(myList) == 1:
            return myList[0]
        if len(myList) % 2 == 1:
            return myList[len(myList) // 2]
        else:
            return sum(myList[len(myList) // 2 - 1 : len(myList) // 2 + 1]) / 2

    for pointer in range(0, len(myList)):
        pointBack = pointer
        anchor = myList[pointer]
        while True:
            pointBack -= 1
            if pointBack < 0:
                break
            elif myList[pointBack] > anchor:
                myList[pointBack + 1] = myList[pointBack]
            else:
                break

        myList[pointBack + 1] = anchor
        print(myList[: pointer + 1])
        print(median(myList[: pointer + 1]))


def mergeSort(mylist: list[float]) -> list[float]:

    # basic case
    if len(mylist) < 2:
        return mylist

    # devide:
    len_right = len(mylist) // 2
    len_left = len(mylist) - len(mylist) // 2
    right = mergeSort(mylist[:len_right])
    left = mergeSort(mylist[len_right:])

    # concatenate:
    result = []
    r_i = 0
    l_i = 0

    while r_i < len_right and l_i < len_left:
        if left[l_i] < right[r_i]:
            result.append(left[l_i])
            l_i += 1
        else:
            result.append(right[r_i])
            r_i += 1

    result += left[l_i:] + right[r_i:]

    return result


# merge sort for dictionaries: sorting according to a key
def mergeSortDict(mydic: list[dict[str, float]], key) -> list[dict[str, float]]:

    # basic case
    if len(mydic) < 2:
        return mydic

    # devide:
    len_right = len(mydic) // 2
    len_left = len(mydic) - len(mydic) // 2
    right = mergeSortDict(mydic[:len_right], key)
    left = mergeSortDict(mydic[len_right:], key)

    # concatenate:
    result = []
    r_i = 0
    l_i = 0

    while r_i < len_right and l_i < len_left:
        if left[l_i][key] < right[r_i][key]:
            result.append(left[l_i])
            l_i += 1
        else:
            result.append(right[r_i])
            r_i += 1

    result += left[l_i:] + right[r_i:]

    return result


# selection sort
def selectionSort(mylist: list[float]) -> list[float]:

    for i in range(len(mylist)):
        mini_index = i
        for j in range(i, len(mylist)):
            if mylist[j] < mylist[mini_index]:
                mini_index = j
        if i != mini_index:
            mylist[mini_index], mylist[i] = mylist[i], mylist[mini_index]

    return mylist
