import random

def quick_sort(elements):
    if len(elements) <= 1:
        return elements
    pivot_index = random.randint(0, len(elements) - 1)
    pivot = elements[pivot_index]
    remaining = elements[:pivot_index] + elements[pivot_index + 1:]
    tail = [e for e in remaining if e <= pivot]
    head = [e for e in remaining if e > pivot]
    return quick_sort(tail) + [pivot] + quick_sort(head)
