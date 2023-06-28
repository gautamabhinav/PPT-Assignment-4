def find_disjoint_nums(nums1, nums2):
    nums1_set = set(nums1)
    nums2_set = set(nums2)

    distinct_nums1 = [num for num in nums1_set if num not in nums2_set]
    distinct_nums2 = [num for num in nums2_set if num not in nums1_set]

    return [distinct_nums1, distinct_nums2]



nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

result = find_disjoint_nums(nums1, nums2)
print(result)
