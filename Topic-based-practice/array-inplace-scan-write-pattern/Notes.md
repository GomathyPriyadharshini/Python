📘 **Array In-Place Pattern – Interview Notes**

---

## 🧠 Core Pattern Name

**Scan → Decide → Write (In-place Array Pattern)**

---

## 🧠 Universal Thinking Steps

1. What am I scanning?
2. What should I keep?
3. Where do I write it?
4. When do I move the write position?

---

## 🔑 Roles

* `i` → scans everything
* `k` → writes only valid elements

👉 Rule:

* `i` always moves
* `k` moves only when you keep something

---

## 📌 Problem-wise Memory Shortcuts

---

### 🟢 1. Remove Element

**Goal:** remove a specific value

🧠 Think:
Keep everything **NOT equal to val**

⚡ Rule:
If element is valid → write it

---

### 🟢 2. Move Zeroes

**Goal:** push zeros to end

🧠 Think:
Keep non-zero values → push zeros later

⚡ Rule:
Step 1: write non-zero
Step 2: fill remaining with zero

---

### 🟢 3. Remove Duplicates (only 1 allowed)

**Goal:** keep unique elements

🧠 Think:
Sorted array → duplicates are adjacent

⚡ Rule:
Keep if different from previous

---

### 🔴 4. Remove Duplicates (max 2 allowed)

**Goal:** allow at most 2 duplicates

🧠 Think:
Check what is already written

⚡ Rule:
Compare with element at position `k-2`

---

## 🔥 MASTER RULE ⭐

To allow **K duplicates** → compare with element at `k-K`

---

## 🧠 Pattern Recognition (Interview Clues)

| Clue in Question  | Meaning                    |
| ----------------- | -------------------------- |
| "in-place"        | no extra array             |
| "remove" / "move" | overwrite                  |
| "sorted array"    | compare with previous      |
| "keep order"      | no swapping                |
| "duplicates"      | comparison logic           |
| "at most k times" | compare with k-th previous |

---

## ⚡ One-line Summary

Scan everything → keep only valid → write forward

---

## 🧠 Final Mental Model

Input → Filter → Compact → Done

---

## 💬 Key Advice

Don’t memorize code.
Remember:

* what to keep
* when to write
* how to compare

---
