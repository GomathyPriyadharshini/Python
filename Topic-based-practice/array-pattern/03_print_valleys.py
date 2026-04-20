# Topic: Local valley detection
# Description: Print elements smaller than both neighbors

nums = [5, 2, 6, 1, 7, 3]

for i in range(1, len(nums)-1):
    if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
        print(nums[i])
