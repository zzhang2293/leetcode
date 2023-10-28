#https://leetcode.com/problems/valid-sudoku/
class Solution(object):
    def isValidSudoku(self, board:list[list[str]]):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

       
        # check row
        record = set()
        for val in board:
            for item in val:
                if item != "." and item in record:
                    return False
                record.add(item)
            record.clear()
        for index in range(len(board[0])):
            for inner_ind in range(len(board[0])):
                if board[inner_ind][index] != '.':
                    if board[inner_ind][index] in record:
                        return False
                    record.add(board[inner_ind][index])
            record.clear()
        
        elements = [[set() for i in range(3)] for i in range(3)]
        for row, ls in enumerate(board):
            for column, item in enumerate(ls):
                if item != '.':
                    if item in elements[row // 3][column // 3]:
                        return False
                    elements[row // 3][column // 3].add(item)    

        return True

obj = Solution()
print(obj.isValidSudoku([[".",".","4",".",".",".","6","3","."],
                         [".",".",".",".",".",".",".",".","."],
                         ["5",".",".",".",".",".",".","9","."],
                         [".",".",".","5","6",".",".",".","."],
                         ["4",".","3",".",".",".",".",".","1"],
                         [".",".",".","7",".",".",".",".","."],
                         [".",".",".","5",".",".",".",".","."],
                         [".",".",".",".",".",".",".",".","."],
                         [".",".",".",".",".",".",".",".","."]]))


        