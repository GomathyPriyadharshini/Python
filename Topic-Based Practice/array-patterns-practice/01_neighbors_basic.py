# Topic: Neighbor traversal using i-1 and i+1
# Description: Print each element with its left and right neighbor

nums = [2, 4, 6, 8, 10]

for i in range(1, len(nums)-1):
    print(nums[i-1], nums[i], nums[i+1])
