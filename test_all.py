import numpy as np


def test_addition():
    assert 1 + 1 == 2


def test_division():
    assert 3./2 == 1.5


def partition_wrapper(arr, kth):
    try:
        return np.partition(arr, kth)
    except AttributeError:
        return np.sort(arr)


def test_partition():
    input_array = np.array([-10, 3, 1, 5, -7])
    partitioned_array = partition_wrapper(input_array, 2)
    assert partitioned_array[2] == 1
