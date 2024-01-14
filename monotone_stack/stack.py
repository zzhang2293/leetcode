
def stack(arr: list):
    record = []
    ans = {}
    for ind, val in enumerate(arr):
        if not record or record[-1][1] < val:
            record.append([ind, val])
        elif record and record[-1][1] >= val:
            while record and record[-1][1] >= val:
                k, v = record.pop(-1)
                ans[k] = {"left": record[-1][0] if record else -1, "right": ind, "val": v}
            record.append([ind, val])

    while record:
        ind, val = record.pop(-1)
        ans[ind] = {"left": record[-1][0] if record else -1, "right": -1, "val": val}

    for key in ans:
        l, r, v = ans[key].values()
        while r != -1 and v == arr[r]:
            v = ans[r]["val"]
            r = ans[r]["right"]
        ans[key]["right"] = r
    res = []
    for i in range(len(arr)):
        res.append([ans[i]["left"], ans[i]["right"]])

    return res


print(stack([3, 3, 1, 5, 6, 2, 7]))





