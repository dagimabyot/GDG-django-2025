def two_sum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        diff = target - v
        if diff in seen:
            return [seen[diff], i]
        seen[v] = i
print(two_sum([2, 7, 11, 15], 9))
