def selection_sort(elements):
    sorted_elements = []
    for i in range(len(elements)):
        lowest_index = find_lowest_index(elements)
        lowest = elements.pop(lowest_index)
        sorted_elements.append(lowest)

    return sorted_elements

def find_lowest_index(elements):
    lowest_index = 0
    lowest = elements[0]
    for index, element in enumerate(elements):
        if element < lowest:
            lowest_index = index
            lowest = element
    return lowest_index
            