def two_sum_sorted(nums, target):
    i, j = 0, len(nums) - 1
    while i < j:
        current_sum = nums[i] + nums[j]
        if current_sum == target:
            return [i, j]
        elif current_sum < target:
            i += 1
        else:
            j -= 1
    return None


nums = [2, 7, 11, 15] 
target = 9
print(two_sum_sorted(nums, target))  
