import pytest
from Python_01 import Solution

solution = Solution()


def test_twoSum_case1():
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1], "Case 1 Failed"


def test_twoSum_case2():
    assert solution.twoSum([3, 2, 4], 6) == [1, 2], "Case 2 Failed"


def test_twoSum_case3():
    assert solution.twoSum([3, 3], 6) == [0, 1], "Case 3 Failed"


def test_twoSum_case4():
    assert solution.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4], "Case 4 Failed"
