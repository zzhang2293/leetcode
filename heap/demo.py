def find_val(lst: list[int], x: int):
    # lst sorted
    # x in lst?
    # log(n)
    # 2
    # [1, 2, 3, 4, 5]
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == x: return True
        elif lst[mid] < x:
            left = mid + 1
        elif lst[mid] > x:
            right = mid - 1
    return False


find_val([1, 2, 3, 4, 6], 5)
