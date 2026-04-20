# Topic: Local peak detection
# Description: Print elements greater than both neighbors

nums = [1, 3, 2, 5, 4, 6, 3]

for i in range(1, len(nums)-1):
    if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        print(nums[i])
