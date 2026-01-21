# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## Project Overview

一个专注于面试准备的数据结构与算法学习项目，通过系统的 Python 实现帮助开发者掌握核心算法思想。项目覆盖从基础数据结构到高级算法的全面知识体系，按算法思想分类组织，每个算法都标注时间/空间复杂度、关联 LeetCode 面试题和难度等级。

## Project Type

- Language: Python 3.10+
- Purpose: Learning/Practice (Data Structures & Algorithms for Interview)

## Global Rules

### LaTeX in Markdown Tables
- Use `\vert` instead of `|` in LaTeX formulas within tables
- Wrong: `|x|` or `|x - \mu|`
- Correct: `\vert x \vert` or `\vert x - \mu \vert`

## Commands

### LeetCode CLI 集成命令

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

### Python 测试命令

```bash
# 运行单个算法文件
python src/array/two_pointers.py

# 检查语法
python -m py_compile src/**/*.py
```

## 算法文件规范

每个算法文件必须包含：

1. **文档字符串**：算法名称、复杂度、关联题目
2. **类型提示**：使用 Python 3.10+ 语法
3. **示例测试**：在 `if __name__ == "__main__":` 中提供示例

## 项目结构

```
src/
├── array/              # 数组相关
├── linked_list/        # 链表操作
├── tree/               # 树相关
├── graph/              # 图算法
├── sorting/            # 排序算法
├── searching/          # 搜索算法
├── backtracking/       # 回溯算法
├── greedy/             # 贪心算法
├── dynamic_programming/ # 动态规划
├── string/             # 字符串算法
├── math/               # 数学算法
├── bit_manipulation/   # 位运算
└── design/             # 设计题
```
