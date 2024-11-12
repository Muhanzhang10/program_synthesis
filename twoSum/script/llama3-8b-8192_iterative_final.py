def func(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        if num in num_dict:
            return [num_dict[num], i]
        else:
            num_dict[target - num] = i
    return []