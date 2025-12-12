Input: sum = [0,1,0,3,12]
def moveZeroes(nums):
    index = 0 
    for n in nums:
        if n != 0:
            nums[index] = n
            index += 1

        while index < len(nums):
            nums[index] = 0
            index += 1