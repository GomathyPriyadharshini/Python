# Topic: Exclude peaks and valleys
# Description: Print elements that are neither peak nor valley

nums = [5, 2, 6, 1, 7, 3]

for i in range(1, len(nums)-1):
    peak = nums[i] > nums[i-1] and nums[i] > nums[i+1]
    valley = nums[i] < nums[i-1] and nums[i] < nums[i+1]

    if not peak and not valley:
        print(nums[i])
