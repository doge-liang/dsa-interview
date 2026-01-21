"""
快速排序
时间复杂度：O(n log n) 平均, O(n²) 最坏
空间复杂度：O(log n) 递归栈
关联题目：LeetCode 912 (Sort an Array) - Medium
"""


def quick_sort(arr: list[int]) -> list[int]:
    """
    快速排序实现

    使用分治策略，选择一个基准元素（pivot），
    将数组分为两部分：小于 pivot 和大于 pivot，
    然后递归排序。

    Args:
        arr: 待排序的整数数组

    Returns:
        排序后的数组
    """
    if len(arr) <= 1:
        return arr

    # 选择基准元素（这里选择中间元素）
    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr: list[int], low: int = 0, high: int | None = None) -> None:
    """
    原地快速排序实现

    相比普通快速排序，原地版本不需要额外的数组空间，
    只使用 O(log n) 的递归栈空间。

    Args:
        arr: 待排序的数组（就地修改）
        low: 起始索引
        high: 结束索引（不包括）
    """
    if high is None:
        high = len(arr)

    if low < high - 1:
        # 分区操作
        pivot = partition(arr, low, high - 1)

        # 递归排序左半部分
        quick_sort_inplace(arr, low, pivot)

        # 递归排序右半部分
        quick_sort_inplace(arr, pivot + 1, high)


def partition(arr: list[int], low: int, high: int) -> int:
    """
    分区操作

    选择最后一个元素作为基准，将数组分为两部分，
    小于等于基准的在左边，大于的在右边。

    Args:
        arr: 数组
        low: 起始索引
        high: 结束索引

    Returns:
        基准元素最终的索引
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    # 示例 1
    arr1 = [3, 6, 8, 10, 1, 2, 1]
    print(f"输入: {arr1}")
    print(f"快速排序（非原地）: {quick_sort(arr1)}")
    print()

    # 示例 2：原地排序
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    print(f"输入: {arr2}")
    quick_sort_inplace(arr2)
    print(f"快速排序（原地）: {arr2}")
    print()

    # 示例 3：随机数组
    import random

    arr3 = [random.randint(1, 100) for _ in range(10)]
    print(f"输入: {arr3}")
    quick_sort_inplace(arr3)
    print(f"排序后: {arr3}")
