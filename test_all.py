import numpy as np


def test_addition():
    assert 1 + 1 == 2


def test_partition():
    input_array = np.array([-10, 3, 1, 5, -7])
    partitioned_array = np.partition(input_array, 2)
    assert partitioned_array[2] == 1
