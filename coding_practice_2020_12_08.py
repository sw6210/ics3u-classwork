# first_last_6

from typing import List


def first_last_6(nums: List[int]) -> bool:
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False


result = first_last_6([1, 2, 6])
print(result)
