class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Time complexity O(n^2)
        if len(matrix)==1:
            return

        from math import ceil
        layer = int(ceil(len(matrix)/2))
        n = len(matrix)

        #print(layer)

        for i in range(layer+1):
            for j in range(i, n-(i+1)):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]
                tmp2 = matrix[j][n-(i+1)]
                matrix[j][n-(i+1)] = tmp
                tmp = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = tmp2
                matrix[n-j-1][i] = tmp




