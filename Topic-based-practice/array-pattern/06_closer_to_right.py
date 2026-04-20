# Problem: Print elements closer to right neighbor than left neighbor

nums = [1, 5, 2, 10, 6, 3, 8]

for i in range(1, len(nums)-1):
    if abs(nums[i] - nums[i+1]) < abs(nums[i] - nums[i-1]):
        print(nums[i])
