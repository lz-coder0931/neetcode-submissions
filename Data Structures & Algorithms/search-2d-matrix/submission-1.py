class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0,len(matrix)-1
        l, r  = 0, len(matrix[0])-1
        row = -1

        while u<=d:
            mid = u+(d-u)//2
            if matrix[mid][0] > target:
                if mid == 0:
                    return False
                elif matrix[mid-1][0]<target:
                    row = mid-1
                    break
                d = mid-1
            elif matrix[mid][0] < target:
                if mid == len(matrix)-1:
                    row = mid
                    break
                elif matrix[mid+1][0]>target:
                    row = mid
                    break
                u = mid+1
            else:
                return True

        while l<=r:
            mid = l+(r-l)//2
            if matrix[row][mid]>target:
                r = mid-1

            elif matrix[row][mid]<target:
                l = mid+1
            else:
                return True

        return False