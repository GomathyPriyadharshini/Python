# Topic: Print element with left and right neighbors

nums = [2, 4, 6, 8, 10]

for i in range(1, len(nums)-1):
    print(nums[i-1], nums[i], nums[i+1])
