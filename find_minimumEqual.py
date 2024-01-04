
#
# Complete the 'findMinimumEqualSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY rowA
#  2. INTEGER_ARRAY rowB
#

def findMinimumEqualSum(rowA: list, rowB: list):
    val1 = sum(rowA)
    num_1 = rowA.count(0)
    num_2 = rowB.count(0)
    val2 = sum(rowB)
    if (val1 > val2 and num_2 == 0) or (val1 < val2 and num_1 == 0):
        return -1
    if (num_1 == 0 and num_2 > val1) or (num_2 == 0 and num_1 > val2):
        return -1
    val1 += num_1
    val2 += num_2
    if val1 < val2:
        return val2
    if val1 > val2:
        return val1

    return val1

def isSpecial(tree_nodes, tree_from: list, tree_to: list):
    edges = []
    for i in range(len(tree_from)):
        edges.append([tree_from[i], tree_to[i]])
    children_nodes = set(edge[1] for edge in edges)
    node = None
    for edge in edges:
        if edge[0] not in children_nodes:
            node = edge[0]
    queue = [node]
    res = [0] * tree_nodes
    while queue:
        n = queue.pop(0)
        if n not in tree_from:
            res[n - 1] = 1

        for edge in edges:
            if edge[0] == n:
                queue.append(edge[1])
    return res


# print(isSpecial(4, [2, 2, 3], [1, 3, 4]))


x = 2
print(2 != x)







