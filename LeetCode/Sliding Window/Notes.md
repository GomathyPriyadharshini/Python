```md
# 🚀 Sliding Window (Two Pointers) Cheat Sheet

A simple and powerful technique to solve **subarray / substring problems efficiently** in O(n) time.

---

# 📌 What is Sliding Window?

Sliding Window is a technique where we maintain a **contiguous range (window)** using two pointers:

```

[left ............. right]

```

- 👉 `right` expands the window
- 👈 `left` shrinks the window when needed

Instead of recalculating everything, we **reuse previous results**.

---

# 🧠 When to Use It?

Use Sliding Window when you see:

- 📍 Subarray / substring problems  
- 📍 Longest / shortest / maximum / minimum  
- 📍 “At most K”, “At least K”, “No duplicates”  
- 📍 Contiguous elements only  

---

# ⚙️ Core Idea

We maintain a condition (invariant) inside the window:

```

✔ window must always remain valid

```

If it becomes invalid:
```

👉 shrink from the left until valid again

```

---

# 🪟 Sliding Window Movement

## Expansion
```

[left -----> right]

```

Add new element → extend window

---

## Shrinking
```

[left X ----> right]

````

Remove elements from left until valid again

---

# 🧩 General Template (Dynamic Window)

```python
left = 0
window = some_data_structure()

for right in range(len(arr)):

    # ➕ Expand window
    add(arr[right])

    # ❌ Fix invalid window
    while window_is_invalid:
        remove(arr[left])
        left += 1

    # 📊 Update answer
    update_result(left, right)
````

---

# 📏 Fixed Size Window (k size)

Used when window size is constant.

```
[ window of size k ]
```

```python
left = 0
window_sum = 0

for right in range(len(arr)):

    window_sum += arr[right]

    # when window size hits k
    if right - left + 1 == k:
        update_answer(window_sum)

        window_sum -= arr[left]
        left += 1
```

---

# 🔥 Example: Longest Substring Without Repeating Characters

## Problem

Find the longest substring with all unique characters.

---

## Idea

Keep expanding until duplicate appears, then shrink.

---

## Visualization

```
a b c a b c b b
        ↑
     duplicate
```

Shrink until valid again.

---

## Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s):

        left = 0
        window = set()
        max_len = 0

        for right in range(len(s)):

            # ❌ shrink until valid
            while s[right] in window:
                window.remove(s[left])
                left += 1

            # ➕ expand window
            window.add(s[right])

            # 📊 update answer
            max_len = max(max_len, right - left + 1)

        return max_len
```

---

# ⚡ Why It Works (Important Insight)

Each element:

* enters the window once ➕
* leaves the window once ➖

So total work is:

```
O(n) time 🚀
```

---

# ❌ Common Mistakes

* using `if` instead of `while` when shrinking
* forgetting to remove from window
* moving pointers incorrectly
* not defining window condition clearly

---

# 🧠 Mental Model

Think of it like a rubber band:

```
👉 stretch right pointer
👈 shrink left pointer when invalid
```

Always maintain a valid window.

---

# 📚 Common Problems

* Longest Substring Without Repeating Characters
* Minimum Window Substring
* Maximum Sum Subarray of Size K
* At Most K Distinct Characters
* Permutation in String

---

# 🏁 Summary

Sliding Window =

```
Expand greedily ➜ Shrink when invalid ➜ Keep window valid
```

🚀 Turns O(n²) problems into O(n)

```

