class BinarySearch(object):
    def search(self, num: list[int], target:int) -> int:
        mid = len(num) // 2
        lower = 0
        upper = len(num) - 1

        while lower <= upper:
            if num[mid] > target: # move to left
                upper = mid - 1
            elif num[mid] < target: # move to right
                lower = mid + 1
            elif num[mid] == target:
                return mid
            mid = (upper + lower) // 2 
            
        return -1
    



b = BinarySearch()
res = b.search([1,2,3,4,7], 6)
print(res)