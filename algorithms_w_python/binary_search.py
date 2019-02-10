def binary_search(elements, term):
    low = 0
    high = len(elements) - 1
    while low <= high:
        mid = (low + high) // 2
        if elements[mid] == term:
            return mid
        elif elements[mid] <= term:
            low = mid + 1
        else:
            high = mid - 1
    return -1
