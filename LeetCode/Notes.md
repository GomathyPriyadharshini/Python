COMMON PYTHON RECURSION / DP PATTERNS

--------------------------------------------------
FIBONACCI / TWO VARIABLE UPDATE
--------------------------------------------------

a, b = 0, 1

for _ in range(n):
    a, b = b, a + b

print(a)

Pattern:
a = previous
b = current


--------------------------------------------------
CLIMBING STAIRS PATTERN
--------------------------------------------------

a, b = 1, 2

for _ in range(3, n + 1):
    a, b = b, a + b

return b


--------------------------------------------------
SWAP VARIABLES
--------------------------------------------------

a, b = b, a


--------------------------------------------------
REVERSE LOOP
--------------------------------------------------

for i in range(n-1, -1, -1):
    print(i)


--------------------------------------------------
DFS RECURSION TEMPLATE
--------------------------------------------------

def dfs(node):

    if not node:
        return

    dfs(node.left)
    dfs(node.right)


--------------------------------------------------
BASIC RECURSION TEMPLATE
--------------------------------------------------

def fn(n):

    if base_case:
        return answer

    return fn(smaller_problem)


--------------------------------------------------
FIBONACCI RECURSION
--------------------------------------------------

def fib(n):

    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)


--------------------------------------------------
BACKTRACKING TEMPLATE
--------------------------------------------------

def backtrack(path):

    if goal:
        result.append(path[:])
        return

    for choice in choices:

        path.append(choice)

        backtrack(path)

        path.pop()


--------------------------------------------------
COUNTING RECURSION
--------------------------------------------------

def count(n):

    if n == 0:
        return

    print(n)

    count(n-1)


--------------------------------------------------
BINARY SEARCH TEMPLATE
--------------------------------------------------

def binary_search(arr, target):

    left, right = 0, len(arr)-1

    while left <= right:

        mid = (left + right)//2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1


--------------------------------------------------
FAST POWER RECURSION
--------------------------------------------------

def power(x, n):

    if n == 0:
        return 1

    half = power(x, n//2)

    if n % 2 == 0:
        return half * half

    return x * half * half


--------------------------------------------------
MEMOIZATION TEMPLATE
--------------------------------------------------

memo = {}

def solve(n):

    if n in memo:
        return memo[n]

    if base_case:
        return answer

    memo[n] = solve(smaller_problem)

    return memo[n]


--------------------------------------------------
TREE LEVEL ORDER (BFS)
--------------------------------------------------

from collections import deque

q = deque([root])

while q:

    node = q.popleft()

    if node.left:
        q.append(node.left)

    if node.right:
        q.append(node.right)


--------------------------------------------------
SLIDING WINDOW TEMPLATE
--------------------------------------------------

left = 0

for right in range(len(arr)):

    while invalid_window:

        left += 1


--------------------------------------------------
TWO POINTER TEMPLATE
--------------------------------------------------

left, right = 0, len(arr)-1

while left < right:

    if condition:
        left += 1
    else:
        right -= 1


--------------------------------------------------
MOST IMPORTANT INTERVIEW PATTERNS
--------------------------------------------------

a, b = b, a+b        -> Fibonacci / DP
left, right          -> Two pointers
mid = (l+r)//2       -> Binary search
path.append/pop      -> Backtracking
dfs(node.left/right) -> Tree recursion
memo[n]              -> Dynamic programming
