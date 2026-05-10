RECURSION TEMPLATE / CHEAT SHEET

--------------------------------------------------
UNIVERSAL RECURSION TEMPLATE
--------------------------------------------------

def solve(problem):

    # 1. BASE CASE
    if smallest_possible_problem:
        return answer

    # 2. MAKE PROBLEM SMALLER
    smaller_problem = reduce(problem)

    # 3. RECURSIVE CALL
    smaller_answer = solve(smaller_problem)

    # 4. COMBINE RESULT
    return combine(smaller_answer)


--------------------------------------------------
MASTER RECURSION CHECKLIST
--------------------------------------------------

1. What is the smallest possible input?
   -> BASE CASE

2. How can I reduce the problem size?
   -> SMALLER PROBLEM

3. What recursive call solves it?
   -> RECURSIVE CALL

4. How do I use the smaller answer?
   -> COMBINE RESULT


--------------------------------------------------
TEMPLATE 1 — SIMPLE RETURN RECURSION
--------------------------------------------------

Used for:
- factorial
- sum of numbers
- power
- fibonacci

def fn(n):

    # base case
    if n == 0:
        return something

    # recursive case
    return current_work + fn(n-1)


Example:

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)


--------------------------------------------------
TEMPLATE 2 — MULTIPLE CHOICES RECURSION
--------------------------------------------------

Used for:
- fibonacci
- climbing stairs

def solve(n):

    if base_case:
        return answer

    choice1 = solve(n-1)
    choice2 = solve(n-2)

    return combine(choice1, choice2)


Example:

def climbStairs(n):

    if n <= 2:
        return n

    return climbStairs(n-1) + climbStairs(n-2)


--------------------------------------------------
TEMPLATE 3 — TREE / DFS RECURSION
--------------------------------------------------

Used for:
- binary trees
- graph DFS

def dfs(node):

    if not node:
        return

    # process current node

    dfs(node.left)
    dfs(node.right)


--------------------------------------------------
TEMPLATE 4 — BACKTRACKING
--------------------------------------------------

Used for:
- subsets
- permutations
- sudoku
- N queens

def backtrack(path):

    if goal_reached:
        result.append(path[:])
        return

    for choice in choices:

        make_choice

        backtrack(updated_path)

        undo_choice


Example:

def backtrack(start, path):

    result.append(path[:])

    for i in range(start, len(nums)):

        path.append(nums[i])

        backtrack(i+1, path)

        path.pop()


--------------------------------------------------
GOLDEN RULES
--------------------------------------------------

1. ALWAYS WRITE BASE CASE FIRST

2. EACH RECURSIVE CALL MUST MAKE
   THE PROBLEM SMALLER

3. TRUST THE RECURSIVE FUNCTION

4. THINK:
   "If smaller problem is solved,
    how do I use that answer?"


--------------------------------------------------
COMMON PATTERN
--------------------------------------------------

Current Answer =
something with
smaller problem answer


Example:

factorial(n)
= n * factorial(n-1)

fib(n)
= fib(n-1) + fib(n-2)


--------------------------------------------------
HOW TO TRACE RECURSION
--------------------------------------------------

Example:

fib(4)

= fib(3) + fib(2)

= (fib(2) + fib(1)) + fib(2)

= ...


Always:
1. go DOWN recursive calls
2. hit BASE CASE
3. return BACK UP


--------------------------------------------------
MOST IMPORTANT RECURSION IDEA
--------------------------------------------------

RECURSION =
1. BASE CASE
2. SMALLER PROBLEM
3. RECURSIVE CALL
4. COMBINE RESULT
