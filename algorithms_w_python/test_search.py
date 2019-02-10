import pytest

from algorithms_w_python.binary_search import binary_search

SCENERIOS = [
    ([], 1, -1),
    ([1], 5, -1),
    ([1], 1, 0),
    ([1, 2], 1, 0),
    ([1, 2], 2, 1),
    ([1, 2, 3], 3, 2),
    ([1, 2, 4, 19, 2000, 5000, 100000], 100000000000, -1),
    ([1, 2, 4, 19, 2000, 5000, 100000], 1, 0),
    ([1, 2, 4, 19, 2000, 5000, 100000], 100000, 6),
]

FUNCS = [
    binary_search
]

@pytest.mark.parametrize("elements, term, expected", SCENERIOS)
@pytest.mark.parametrize("func", FUNCS)
def test_search(func, elements, term, expected):
    assert func(elements, term) == expected
