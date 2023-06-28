def shuffle_array(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result


nums = [2, 5, 1, 3, 4, 7]
n = 3
shuffled = shuffle_array(nums, n)
print(shuffled)
