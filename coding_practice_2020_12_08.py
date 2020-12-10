from typing import List

# CODINGBAT LIST-1 QUESTIONS
----------------------------

# first_last_6
def first_last_6(nums: List[int]) -> bool:
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False

result = first_last_6([1, 2, 6])
print(result)


# same_first_last
def same_first_last(nums: List[int]) -> bool:
    if len(nums) >= 1 and nums[0] == nums[-1]:
        return True
    else:
        return False

result = same_first_last([1, 2, 3])
print(result)


# make_pi
def make_pi() -> List[int]:
    return [3, 1, 4]

result = make_pi()
print(result)


# common_end
def common_end(a: List[int], b: List[int]) -> bool:
    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    else:
        return False

result = common_end([1, 2, 3], [7, 3])
print(result)


# sum_3
def sum_3(nums: List[int]) -> int:
    return nums[0] + nums[1] + nums[2]

result = sum_3([1, 2, 3])
print(result)


# rotate_left_3
def rotate_left_3(nums: List[int]) -> List[int]:
    return [nums[1], nums[2], nums[0]]

result = rotate_left_3([1, 2, 3])
print(result)

# reverse_3
def reverse_3(nums: List[int]) -> List[int]:
    return [nums[2], nums[1], nums[0]]

result = reverse_3([1, 2, 3])
print(result)

# sum_2
def sum_2(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    elif len(nums) < 2:
        return nums[0] 
    else:
        return nums[0] + nums [1]

result = sum_2([1, 2, 3])
print(result)


# middle_way
def middle_way(a: List[int], b: List[int]) -> List[int]:
    return [a[1], b[1]]

result = middle_way([1, 2, 3], [4, 5, 6])
print(result)

# make_ends
def make_ends(nums: List[int]) -> List[int]:
    return [nums[0], nums[-1]]

result = make_ends([1, 2, 3])
print(result)


# CODINGBAT LIST-2 QUESTIONS
----------------------------

# count_evens
def count_evens(nums: List[int]) -> int:
    count = 0
    for number in nums:
        if number % 2 == 0:
            count += 1
    return count

result = count_evens([2, 1, 2, 3, 4])
print(result)


# big_diff
def big_diff(nums: List[int]) -> int:
    return max(nums) - min(nums)

result = big_diff([10, 3, 5, 6])
print(result)


# centered_average
def centered_average(nums: List[int]) -> int:
    return round((sum(nums) - max(nums) - min(nums)) / (len(nums)-2), 0)

result = centered_average([1, 2, 3, 4, 100])
print(result)


# sum_67
def sum_67(nums: List[int]) -> int:
    total = 0
    in_section = False
    for num in nums:
        if num == 6:
            in_section = True
        if not in_section:
            total += num
        elif num == 7:
                in_section = False
    return total

result = sum_67([1, 2, 2])
print(result)


# 

