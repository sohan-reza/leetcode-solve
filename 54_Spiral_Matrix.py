class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Time Complexity O(n) and Space Complexity is O(n)

        row = len(matrix)
        col = len(matrix[0])



        n = row*col

        direction = True # row, False : column
        sign = True # for incressing , False : decressing

        c = 0
        r = 0
        ans = []

        visited = [[-1 for _ in range(col)] for _ in range(row)]

        for i in range(n):
            if direction:		
                ans.append(matrix[r][c])
                visited[r][c] = 1
                if sign:
                    c +=1
                else:
                    c -=1
                if c == col:
                    direction = False
                    c -=1
                    r +=1
                elif c<0 and r>0:
                    r -= 1
                    c = 0
                    direction = False
                    sign = False
                
                if i == n-1:
                    continue	
                
                if visited[r][c] != -1:
                    
                    if sign is True:
                        r +=1
                        c -=1
                        direction = False
                    else:
                        
                        #print(r, c)
                        r -=1
                        c +=1
                        #print(r, c)
                        direction = False
                        sign = False
                    
                
            else:
                ans.append(matrix[r][c])
                visited[r][c]=1
                
                if sign:
                    r+=1
                else:
                    r-=1
                    
                if r == row:
                    r-=1
                    c-=1
                    direction=True
                    sign=False
                
                if i == n-1:
                    continue
                    
                
                if  visited[r][c] != -1:
                    
                    if sign is True:
                        r-=1
                        c -=1
                        direction = True
                        sign = False
                    else:
                        
                        r +=1
                        c +=1
                        direction = True
                        sign = True

        return ans


