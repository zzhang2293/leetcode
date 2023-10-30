# https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix:list, target:int):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        left, right = 0, len(matrix) - 1
        mid_row = (left + right) // 2
        target_row = None
        while left <= right:
            if matrix[mid_row][0] > target:
                right = mid_row - 1
            elif matrix[mid_row][-1] < target:
                left = mid_row + 1
            elif matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                target_row = mid_row
                break
            mid_row = (right + left) // 2
        if target_row == None:
            return False
        row = matrix[target_row]
        left, right = 0, len(row) - 1
        mid = (left + right) // 2
        
        while left <= right:
            if row[mid] > target:
                right = mid - 1
            elif row[mid] < target:
                left = mid + 1
            elif row[mid] == target:
                return True
            mid = (right + left) // 2
        return False
            