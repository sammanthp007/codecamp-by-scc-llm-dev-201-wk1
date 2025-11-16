# Week 1 — Assignment 1: **Leet-Ladder 1 (8 DS&A Problems)**

> **Due:** **Sunday 23:59 (NPT)**
> **Goal:** Build problem-solving habits with clean, tested Python and a tiny **problem runner** you’ll reuse all camp. No LLMs—just you, the REPL, and clear thinking.

---

## Why this assignment exists (in one paragraph)

LLM apps fail for boring reasons: off-by-one bugs, edge-cases, and code that’s hard to trust. This week you’ll practice writing **small, predictable functions** and a **JSON-driven runner** that tells you the truth (pass/fail) without drama. These skills become your safety net when we add models later.

---

## What you’ll deliver

* `week1_leet_ladder/solutions.py` — **8 functions**, each with a short docstring and a **“Big-O: time …, space …”** line.
* `week1_leet_ladder/problems.json` — public tests (incl. edge cases).
* `week1_leet_ladder/runner.py` — loads JSON tests, prints a neat pass/fail table + totals.
* `README.md` — ≤200 words: what stumped you, what clicked, one tip for future-you.
* **60-sec demo video**: run → show a failing test → fix → re-run (screen recording; link in README).

---

## Learning outcomes

1. Implement 8 classic problems using **two-pointers, sliding window, hash maps, stacks, recursion/memo**, and **binary search**.
2. State **time & space complexity** clearly for each solution.
3. Write minimal yet effective **JSON-driven tests** and a simple runner.
4. Practice **edge-case** thinking and calm debugging.

---

## Tasks (conversational prompts included)

### A) Implement these 8 functions in `solutions.py`

**Easy (6)**

1. `reverse_vowels(s: str) -> str`
   Reverse only vowels using **two-pointers**.
   *Thinking prompt:* What invariant do the two pointers maintain? When do both move?

2. `two_sum(nums: list[int], target: int) -> list[int]`
   Return **indices** of two numbers that add to `target` (any valid pair). Use a **hash map**.
   *Thinking prompt:* What key/value do you store so you can answer in O(1) when you see the “partner”?

3. `valid_parentheses(s: str) -> bool`
   True if `()[]{}` are balanced using a **stack**.
   *Thinking prompt:* What exactly must match on pop? What happens on an unexpected close?

4. `first_unique_char(s: str) -> int`
   Return the **index** of the first non-repeating character, or **−1** if none (frequency map).
   *Thinking prompt:* Why two passes (count → find) is simpler than one clever pass.

5. `merge_two_sorted_lists(a: list[int], b: list[int]) -> list[int]`
   Merge two **ascending** lists via **two-pointers** (stable).
   *Thinking prompt:* When do you append from `a` vs `b`? What happens when one list runs out?

6. `binary_search(nums: list[int], target: int) -> int`
   Iterative **binary search** on an ascending list. Return index or **−1**.
   *Thinking prompt:* Where do you update `lo`/`hi`? How do you avoid infinite loops?

**Medium (2)**

7. `length_of_longest_substring(s: str) -> int`
   Length of the longest substring without repeating chars (**sliding window**).
   *Thinking prompt:* What does your window guarantee at every step? How do you move the left pointer?

8. `climbing_stairs_no_three_ones(n: int) -> int`
   Ways to reach step `n` using steps of **1 or 2**, but **never three consecutive 1-steps**. Use **recursion + memo** or bottom-up DP.
   *Thinking prompt:* What state do you need to remember to forbid “1,1,1”? (Hint: track how many 1s in a row.)
   *Sanity table (for your comments/tests):*
   `n: 1 2 3 4 5 6  →  ways: 1 2 2 4 5 8`

> **Docstring requirement (every function):** 1–2 lines of intent + **“Big-O: time …, space …”** on its own line.

---

### B) Provide public tests in `problems.json`

Start with **at least one** test per function, then add **one edge case** per function. You can mirror this structure:

```json
[
  { "func": "reverse_vowels", "args": ["leetcode"], "expected": "leotcede" },
  { "func": "reverse_vowels", "args": ["aA"], "expected": "Aa" },

  { "func": "two_sum", "args": [[2,7,11,15], 9], "expected": [0,1] },
  { "func": "two_sum", "args": [[3,3], 6], "expected": [0,1] },

  { "func": "valid_parentheses", "args": ["([]{})"], "expected": true },
  { "func": "valid_parentheses", "args": ["(]"], "expected": false },

  { "func": "first_unique_char", "args": ["leetcode"], "expected": 0 },
  { "func": "first_unique_char", "args": ["aabb"], "expected": -1 },

  { "func": "merge_two_sorted_lists", "args": [[1,2,4],[1,3,4]], "expected": [1,1,2,3,4,4] },
  { "func": "merge_two_sorted_lists", "args": [[],[0]], "expected": [0] },

  { "func": "binary_search", "args": [[-1,0,3,5,9,12], 9], "expected": 4 },
  { "func": "binary_search", "args": [[-1,0,3,5,9,12], 2], "expected": -1 },

  { "func": "length_of_longest_substring", "args": ["abcabcbb"], "expected": 3 },
  { "func": "length_of_longest_substring", "args": ["bbbbb"], "expected": 1 },

  { "func": "climbing_stairs_no_three_ones", "args": [4], "expected": 4 },
  { "func": "climbing_stairs_no_three_ones", "args": [5], "expected": 5 }
]
```

**Edge-case hints:** empty strings, all vowels/no vowels, duplicates (`[3,3]`), negative numbers, already-sorted vs one empty list, targets not found.

---

### C) Make the runner tell the truth (and stay calm)

Your `runner.py` should:

* Load `problems.json`.
* For each case: call `solutions.<func>(*args)`; compare to `expected`.
* Print a tidy table: **Problem / Result / Expected / Pass?** and a final **X/Y passed**.
* On exceptions: show a short error but **continue**.
* Exit with code **0** only if all tests pass (so CI can use it later).

> Small, honest output beats flashy output. Aim for clarity.

---

## Acceptance criteria (all required)

* ✅ All **8 functions** exist, include docstrings + **Big-O**, and pass the public tests.
* ✅ **≥1 edge case** per function in `problems.json`.
* ✅ Runner prints a clear table + totals; handles exceptions without crashing; returns a meaningful exit code.
* ✅ `README.md` reflection (≤200 words): what stumped you, what clicked, one lesson for future-you.
* ✅ **60-sec demo video** link in `README.md`.
* ✅ Git hygiene: small, meaningful commits; run instructions included.

---

## Grading

* **Functionality & Tests** — 40%
* **Code Quality (clarity, idioms, naming)** — 20%
* **Complexity Understanding (Big-O lines)** — 15%
* **Runner UX (readable output, error handling)** — 10%
* **Reflection & Git Hygiene** — 15%
  **Pass bar:** ≥ **70%** and all acceptance items met.

---

## Constraints & tips

* Standard Python only this week (no third-party packages needed).
* Prefer **clear** over **clever**; add comments where intent might be misread.
* For `climbing_stairs_no_three_ones`, forbid any path containing `1,1,1`. Use memoization to avoid recomputation.
* Include at least **one empty-input** test where it makes sense.

---

## Submission

1. Push your code to GitHub.
2. Add your 60-sec demo link to `README.md`.
3. Submit the repo link on the LMS **before Sunday 23:59 (NPT)**.

---

## Integrity

Discuss ideas, not code. If you consulted a resource, cite it in `README.md` (link + one line). Your code must be your own.

---

### Quick troubleshooting

* **ImportError:** check `solutions.py` name and import path.
* **TypeError (args mismatch):** ensure `args` shapes match your function signatures.
* **List vs tuple:** JSON uses lists; compare like with like.
* **Two-pointers stuck:** make sure both pointers eventually move, even when skipping characters.
* **Binary search loop:** confirm `lo <= hi` and correct mid update.
