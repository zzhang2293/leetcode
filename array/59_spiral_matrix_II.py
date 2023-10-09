class Solution(object):
    def generateMatrix(self, n:int) -> list[list[int]]:
        """
        :type n: int
        :rtype: List[List[int]]

        Given a positive integer n, generate an n x n matrix 
        filled with elements from 1 to n2 in spiral order.
        """


        count = 1
        matrix = [[0] * n for _ in range(n)]
        loop , mid = n // 2, n // 2
        x, y = 0, 0

        for offset in range(1, loop + 1):   
            for i in range(y, n - offset):
               matrix[x][i] = count       # from left to right
               count += 1
            
            for i in range(x, n - offset):
               matrix[i][n - offset] = count      # from up to down 
               count += 1
            
            for i in range(n - offset, y, -1):  # from left to right
                matrix[n - offset][i] = count
                count += 1

            for i in range(n - offset, x, -1):   # from down to up
                matrix[i][y] = count
                count += 1

            x += 1
            y += 1

        if n % 2 != 0:
            matrix[mid][mid] = count

        return matrix




obj = Solution()
res = obj.generateMatrix(1)
print(res)
