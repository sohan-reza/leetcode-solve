class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Time complexity O(n^3) and Space O(1)

        make_change = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.makeZero(matrix, i, -1)
                    make_change= True
                    break
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    self.makeZero(matrix, -1, j)
                    make_change = True
                    

        
        if make_change:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 'c':
                        matrix[i][j] = 0
    
    def makeZero(self, matrix, r, c):
        if c==-1:
            for i in range(len(matrix[0])):
                if matrix[r][i] == 0:
                    continue
                matrix[r][i] = 'c'
        if r==-1:
            for i in range(len(matrix)):
                if matrix[i][c] == 0:
                    continue
                matrix[i][c] = 'c'

