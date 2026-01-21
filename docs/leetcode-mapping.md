# LeetCode 题目映射表

本文档记录已实现的 LeetCode 题目及其对应的算法分类和文件路径。

## 已实现题目

### Array（数组）

| ID | 题目 | 难度 | 文件路径 |
|----|------|------|---------|
| 1 | Two Sum | Easy | src/array/two_sum.py |
| 15 | 3Sum | Medium | src/array/three_sum.py |
| 167 | Two Sum II | Medium | src/array/two_sum_ii.py |

### Linked List（链表）

| ID | 题目 | 难度 | 文件路径 |
|----|------|------|---------|
| 2 | Add Two Numbers | Medium | src/linked_list/add_two_numbers.py |
| 206 | Reverse Linked List | Easy | src/linked_list/reverse_linked_list.py |

### Tree（树）

| ID | 题目 | 难度 | 文件路径 |
|----|------|------|---------|
| 94 | Binary Tree Inorder Traversal | Easy | src/tree/inorder_traversal.py |
| 102 | Binary Tree Level Order Traversal | Medium | src/tree/level_order_traversal.py |

### Graph（图）

| ID | 题目 | 难度 | 文件路径 |
|----|------|------|---------|
| 200 | Number of Islands | Medium | src/graph/number_of_islands.py |
| 207 | Course Schedule | Medium | src/graph/course_schedule.py |

### Sorting（排序）

| ID | 题目 | 难度 | 文件路径 |
|----|------|------|---------|
| 912 | Sort an Array | Medium | src/sorting/sort_array.py |
| 215 | Kth Largest Element | Medium | src/sorting/kth_largest.py |

### Searching（搜索）

| ID | 题目 | 难度 | 文件路径 |
|----|------|------|---------|
| 704 | Binary Search | Easy | src/searching/binary_search.py |
| 34 | Find First and Last Position | Medium | src/searching/search_range.py |

### Backtracking（回溯）

| ID | 题目 | 难度 | 文件路径 |
|----|------|------|---------|
| 46 | Permutations | Medium | src/backtracking/permutations.py |
| 78 | Subsets | Medium | src/backtracking/subsets.py |

### Greedy（贪心）

| ID | 题目 | 难度 | 文件路径 |
|----|------|------|---------|
| 55 | Jump Game | Medium | src/greedy/jump_game.py |

### Dynamic Programming（动态规划）

| ID | 题目 | 难度 | 文件路径 |
|----|------|------|---------|
| 70 | Climbing Stairs | Easy | src/dynamic_programming/climbing_stairs.py |
| 300 | Longest Increasing Subsequence | Medium | src/dynamic_programming/lis.py |

### String（字符串）

| ID | 题目 | 难度 | 文件路径 |
|----|------|------|---------|
| 3 | Longest Substring Without Repeating | Medium | src/string/longest_substring.py |

### Math（数学）

| ID | 题目 | 难度 | 文件路径 |
|----|------|------|---------|
| 204 | Count Primes | Medium | src/math/count_primes.py |

### Bit Manipulation（位运算）

| ID | 题目 | 难度 | 文件路径 |
|----|------|------|---------|
| 191 | Number of 1 Bits | Easy | src/bit_manipulation/count_bits.py |

### Design（设计）

| ID | 题目 | 难度 | 文件路径 |
|----|------|------|---------|
| 146 | LRU Cache | Medium | src/design/lru_cache.py |

---

## 待实现题目

### 优先级 1：面试高频题

- [ ] LeetCode 11: Container With Most Water
- [ ] LeetCode 42: Trapping Rain Water
- [ ] LeetCode 23: Merge K Sorted Lists
- [ ] LeetCode 53: Maximum Subarray
- [ ] LeetCode 121: Best Time to Buy and Sell Stock

### 优先级 2：经典算法题

- [ ] LeetCode 139: Word Break
- [ ] LeetCode 198: House Robber
- [ ] LeetCode 322: Coin Change
- [ ] LeetCode 416: Partition Equal Subset Sum
- [ ] LeetCode 560: Subarray Sum Equals K

### 优先级 3：进阶挑战

- [ ] LeetCode 32: Longest Valid Parentheses
- [ ] LeetCode 72: Edit Distance
- [ ] LeetCode 76: Minimum Window Substring
- [ ] LeetCode 84: Largest Rectangle in Histogram
- [ ] LeetCode 85: Maximal Rectangle

---

## 使用方法

### 查找题目

1. 在本表中搜索题目 ID 或名称
2. 找到对应的文件路径
3. 使用 `npm run lc:show <ID>` 生成代码

### 添加新题目

1. 使用 `npm run lc:show <ID>` 生成代码
2. 实现算法后，更新本表
3. 提交到 LeetCode 后更新完成状态

### 同步进度

```bash
# 拉取所有历史提交
npm run lc:pull

# 同步到 src/ 目录
npm run lc:sync
```

---

## 统计信息

- 已实现题目：15 个
- 简单：2 个
- 中等：11 个
- 困难：2 个
- 完成率：0.02%（15/7000+）

---

## 参考资料

- [LeetCode 官方题单](https://leetcode.com/problemset/all/)
- [LeetCode Top 100 Liked](https://leetcode.com/problemset/top-100-liked-questions/)
- [LeetCode Interview Questions](https://leetcode.com/problemset/algorithms/?listId=xcibl0i)

---

**最后更新：** 2026-01-21
