# 🧠 Array Neighbor Logic (i-1, i+1) — Quick Notes

## 🔹 1. Safe Loop Range (IMPORTANT)

```python
for i in range(1, len(nums)-1):
```

* Prevents index errors
* Allows safe use of `i-1` and `i+1`

---

## 🔹 2. Neighbor Access Pattern

```python
left  = nums[i-1]
curr  = nums[i]
right = nums[i+1]
```

---

## 🔹 3. Peak (Local Maximum)

Element greater than both neighbors:

```python
nums[i] > nums[i-1] and nums[i] > nums[i+1]
```

---

## 🔹 4. Valley (Local Minimum)

Element smaller than both neighbors:

```python
nums[i] < nums[i-1] and nums[i] < nums[i+1]
```

---

## 🔹 5. OR Logic (At Least One Condition)

Greater than at least one neighbor:

```python
nums[i] > nums[i-1] or nums[i] > nums[i+1]
```

---

## 🔹 6. NOT Logic (Reverse Condition)

```python
not (condition)
```

Example:

```python
not (nums[i] < nums[i-1] and nums[i] < nums[i+1])
```

---

## 🔹 7. Neutral Elements (Not Peak & Not Valley)

```python
peak = nums[i] > nums[i-1] and nums[i] > nums[i+1]
valley = nums[i] < nums[i-1] and nums[i] < nums[i+1]

if not peak and not valley:
    print(nums[i])
```

---

## 🔹 8. AND vs OR vs NOT

| Operator | Meaning              | Use Case         |
| -------- | -------------------- | ---------------- |
| `and`    | both conditions true | peak / valley    |
| `or`     | at least one true    | loose comparison |
| `not`    | reverse condition    | exclude cases    |

---

## 🔹 9. Common Mistake ⚠️

```python
for i in range(len(nums)):
    nums[i+1]  # ❌ IndexError at last element
```

✅ Fix:

```python
for i in range(1, len(nums)-1):
```

---

## 🔹 10. Mental Model

```
[left]  [current]  [right]
```

Ask:

* Bigger than both → Peak
* Smaller than both → Valley
* Otherwise → Neutral

---

## 🔥 One-line Summary

Use `range(1, len(nums)-1)` and compare `nums[i]` with neighbors
to classify elements using `and`, `or`, and `not`.
