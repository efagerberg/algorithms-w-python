from random import sample

import pytest

from algorithms_w_python.selection_sort import selection_sort
from algorithms_w_python.quick_sort import quick_sort

CASES = [
    [],
    [1],
    [1, 2, 3],
    [3, 1],
    [3, 2, 1],
    sample(range(100000), 1000)
]

FUNCS = [
    selection_sort,
    quick_sort
]


@pytest.mark.parametrize("elements", CASES)
@pytest.mark.parametrize("func", FUNCS)
def test_sort(func, elements):
    assert func(elements[:]) == sorted(elements)
