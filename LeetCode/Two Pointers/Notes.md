🧠 TWO POINTERS CHEAT SHEET
🔥 1. Opposite Direction (i, j)
📌 When to use:
Pair problems
Sorted arrays
Sum / difference / matching
Palindrome checks
🧭 Setup:
i = 0
j = len(arr) - 1
⚡ Movement rule:

Ask: “too small or too big?”

Condition	Action
result < target	i += 1
result > target	j -= 1
🧠 Memory line:

“Need more → go right, Need less → go left”

🔥 2. Same Direction (Fast–Slow)
📌 When to use:
Remove duplicates
Filter / overwrite array
Partition problems
🧭 Setup:
slow = 0
for fast in range(n):
⚡ Rule:
fast scans everything
slow stores valid result
🧠 Memory line:

“Fast explores, slow writes”

🔥 3. Sliding Window (i, j forward)
📌 When to use:
Subarray problems
Sum / length constraints
Longest / shortest window
🧭 Setup:
i = 0
for j in range(n):
⚡ Rule:
expand j
shrink i when condition breaks
🧠 Memory line:

“Expand → then fix window”

⚠️ DECISION TREE (VERY IMPORTANT)

Ask this:

1. Is array sorted or pair-based?

👉 Opposite pointers

2. Am I modifying array in-place?

👉 Fast–slow

3. Am I dealing with subarray/substring?

👉 Sliding window

🧠 SUPER SHORT MEMORY TRICK
Pattern	Meaning
Opposite	shrink space
Fast–Slow	overwrite/filter
Sliding	maintain window
🔥 INTERVIEW ONE-LINER

“I choose two pointers based on whether I need to shrink a search space, filter elements in-place, or maintain a dynamic window.”
