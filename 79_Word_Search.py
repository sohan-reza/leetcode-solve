class Solution(object):

    def search(self, board, i, j, word, pos):
        if pos==len(word):
            return True
        
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
            return False
       
        

        
        if board[i][j] != word[pos]:
            return False
        
        board[i][j] = "-"+board[i][j]
       
        a = self.search(board, i, j+1, word, pos+1)
        b = self.search(board, i, j-1, word, pos+1)
        c = self.search(board, i+1, j, word, pos+1)
        d = self.search(board, i-1, j, word, pos+1)

        board[i][j] = board[i][j][1]

        return a or b or c or d
        
        

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(self.search(board, i, j, word, 0)):
                    return True
        return False
