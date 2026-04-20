# Topic: OR logic with neighbors
# Description: Print elements greater than at least one neighbor

nums = [1, 3, 2, 5, 4]

for i in range(1, len(nums)-1):
    if nums[i] > nums[i-1] or nums[i] > nums[i+1]:
        print(nums[i])
