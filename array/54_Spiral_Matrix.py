class Solution(object):
    def spiralOrder(self, matrix:list[list[int]]):  # so fucking stupid question
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # loop = min(len(matrix), len(matrix[0])) // 2
        row_len = len(matrix[0])
        col_len = len(matrix)
        x_start = 0
        y_start = 0
        x_end = col_len - 1
        y_end = row_len - 1
        res = []


        while row_len > 0 and col_len > 0:

            self.iter_matrix(x_start, x_end, y_start, y_end, res, matrix)
            x_start += 1
            x_end -= 1
            y_start += 1
            y_end -= 1
            row_len -= 2
            col_len -= 2
    
        return res

    def iter_matrix(self, x_start:int,x_end:int, y_start:int, y_end:int, res:list[int], matrix:list[list[int]]):
        if x_start != x_end and y_start != y_end:
            for i in range(y_start, y_end):
                res.append(matrix[x_start][i])
            for i in range(x_start, x_end):
                res.append(matrix[i][y_end])
            for i in range(y_end, y_start, -1):
                res.append(matrix[x_end][i])
            for i in range(x_end, x_start, -1):
                res.append(matrix[i][y_start])
        elif x_start == x_end and y_start != y_end:
            for i in range(y_start, y_end + 1):
                res.append(matrix[x_start][i])
        elif x_start != x_end and y_start == y_end:
            for i in range(x_start, x_end + 1):
                res.append(matrix[i][y_start])
        elif x_start == x_end and y_start == y_end:
            res.append(matrix[x_start][y_start])


obj = Solution()
res = obj.spiralOrder([[6,9,7]])
print(res)