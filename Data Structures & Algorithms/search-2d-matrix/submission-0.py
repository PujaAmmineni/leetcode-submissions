class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if target > value:
                left = mid + 1
            elif target < value:
                right = mid - 1
            else:
                return True

        return False
