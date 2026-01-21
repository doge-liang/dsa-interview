"""
两数之和
时间复杂度：O(n)
空间复杂度：O(n)
关联题目：LeetCode 1 (Two Sum) - Easy
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    在数组中找到两个数，使它们的和等于目标值

    使用哈希表存储已遍历的数字及其索引，
    遍历时检查 target - nums[i] 是否在哈希表中。

    Args:
        nums: 整数数组
        target: 目标和

    Returns:
        两个数的索引列表
    """
    hash_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in hash_map:
            return [hash_map[complement], i]

        hash_map[num] = i

    return []


if __name__ == "__main__":
    # 示例 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"输入: nums = {nums1}, target = {target1}")
    print(f"输出: {two_sum(nums1, target1)}")
    print()

    # 示例 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"输入: nums = {nums2}, target = {target2}")
    print(f"输出: {two_sum(nums2, target2)}")
    print()

    # 示例 3
    nums3 = [3, 3]
    target3 = 6
    print(f"输入: nums = {nums3}, target = {target3}")
    print(f"输出: {two_sum(nums3, target3)}")
