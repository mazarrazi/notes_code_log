def twoSum(nums, target):
    complement_dict = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_dict:
            return [complement_dict[complement], i]
        else:
            complement_dict[num] = i

    return []

# e.g.
nums1 = [2, 7, 11, 15]
target1 = 9
result1 = twoSum(nums1, target1)
print(result1)  
