# dsa-interview

一个专注于面试准备的数据结构与算法学习项目，通过系统的 Python 实现帮助开发者掌握核心算法思想。项目覆盖从基础数据结构到高级算法的全面知识体系，按算法思想分类组织，每个算法都标注时间/空间复杂度、关联 LeetCode 面试题和难度等级。适合求职 AI 算法工程师、数据工程师和应用开发工程师的系统复习与提升。

## 目录结构

```
dsa-interview/
├── src/                    # 算法实现源代码
│   ├── array/              # 数组相关（双指针、滑动窗口、哈希）
│   ├── linked_list/        # 链表操作
│   ├── tree/               # 树相关（二叉树遍历、BST）
│   ├── graph/              # 图算法（Dijkstra、拓扑排序）
│   ├── sorting/            # 排序算法（快速排序、归并排序）
│   ├── searching/          # 搜索算法（二分查找、DFS/BFS）
│   ├── backtracking/       # 回溯算法（排列组合、子集）
│   ├── greedy/             # 贪心算法（活动选择、区间调度）
│   ├── dynamic_programming/ # 动态规划（背包问题、LCS）
│   ├── string/             # 字符串算法（KMP、Boyer-Moore）
│   ├── math/               # 数学算法（素数、GCD/LCM）
│   ├── bit_manipulation/   # 位运算操作
│   └── design/             # 设计题（LRU Cache、Trie）
├── docs/                   # 文档
│   ├── README.md           # 学习路线
│   ├── complexity-reference.md  # 复杂度速查表
│   └── leetcode-mapping.md     # LeetCode 题目映射
├── scripts/                # 工具脚本
│   └── lc-wrapper.py      # leetcode-cli 包装脚本
├── leetcode-imports/       # leetcode-cli 生成的临时文件
└── README.md              # 本文件
```

## 快速开始

### 环境要求

- Python 3.10+
- Node.js 20+
- Git

### 安装依赖

```bash
npm install
```

### 配置 leetcode-cli

```bash
# 全局安装 leetcode-cli
npm install -g leetcode-cli

# 登录 LeetCode 账号
leetcode user -l

# 设置默认语言为 Python
leetcode config code:lang python3
```

### 使用方式

#### 方式 1：使用 leetcode-cli 管理

```bash
# 查看题目列表
npm run lc:list

# 生成题目代码（自动移动到 src/ 对应目录）
npm run lc:show 1

# 测试代码
npm run lc:test ./leetcode-imports/1.two-sum.py

# 提交代码
npm run lc:submit ./leetcode-imports/1.two-sum.py

# 同步到 src/（将临时文件移动到正确目录）
npm run lc:sync

# 拉取历史提交
npm run lc:pull
```

#### 方式 2：手动创建 + 提交

```bash
# 直接在 src/ 中编写代码
vim src/array/two_pointers.py

# 测试和提交
npm run lc:test src/array/two_pointers.py
npm run lc:submit src/array/two_pointers.py
```

## 学习路线

参见 [docs/README.md](./docs/README.md) 了解详细的学习计划和推荐顺序。

## 算法实现规范

每个算法文件应包含：

```python
"""
算法名称
时间复杂度：O(n)
空间复杂度：O(1)
关联题目：LeetCode 1 (Two Sum) - Easy
"""

def algorithm_function(params):
    # 实现
    pass

if __name__ == "__main__":
    # 示例测试
    result = algorithm_function(sample_input)
    print(result)
```

## 复杂度参考

参见 [docs/complexity-reference.md](./docs/complexity-reference.md) 查看常见算法的复杂度总结。

## LeetCode 题目映射

参见 [docs/leetcode-mapping.md](./docs/leetcode-mapping.md) 查看已实现的 LeetCode 题目列表。

## 参考资源

- [LeetCode](https://leetcode.com/)
- [leetcode-cli](https://github.com/skygragon/leetcode-cli)
- [Introduction to Algorithms](https://mitpress.mit.edu/books/introduction-algorithms-fourth-edition)

## License

MIT
