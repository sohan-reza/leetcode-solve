class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # this algorithm is easy to process then my previous solutio Spiral Matrix I
        #It's Time complexity is O(N*N) and Space is O(N*N)
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        rowBegin = 0
        rowEnd = len(matrix)

        colBegin = 0
        colEnd = len(matrix)
        s = 1
        while rowBegin < rowEnd and colBegin < colEnd:
            for i in range(colBegin, colEnd):
                matrix[rowBegin][i] = s
                s+=1
            rowBegin+=1
            
            for i in range(rowBegin, rowEnd):
                matrix[i][colEnd-1] = s
                s+=1
            colEnd-=1
            
            if colBegin<colEnd:
                
                for i in range(colEnd-1, colBegin-1, -1):
                    
                    matrix[rowEnd-1][i] =s
                    s+=1
            rowEnd -=1
            if rowBegin<rowEnd:
                for i in range(rowEnd-1, rowBegin-1,-1):
                    matrix[i][colBegin] = s
                    s+=1
            colBegin+=1
        return matrix

