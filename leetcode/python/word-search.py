# -*- coding: utf-8 -*-
"""
https://oj.leetcode.com/problems/word-search/

Word Search 

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighbouring. 
The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
    
:copyright: (c) 2014 by Gully Chen.
:license: BSD, see LICENSE for more details.  
"""
   

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if not board or not word:
            return False
            
        word_size = len(word)
        x, y = len(board[0]), len(board)
        
        placeholder = "$"
                        
        def dfs(i, j, word_idx):
            if word_idx >= word_size:
                return True
                
            if i < 0 or j < 0 or i >= y or j >= x or board[i][j] == placeholder:
                return False 
                                                
            saved_char = board[i][j]
            
            if board[i][j] == word[word_idx]:
                board[i][j] = placeholder
                
                if (dfs(i-1, j, word_idx+1) or  # up
                    dfs(i, j-1, word_idx+1) or  # left
                    dfs(i+1, j, word_idx+1) or  # down
                    dfs(i, j+1, word_idx+1)):   # right     
                   return True
                
            board[i][j] = saved_char
            return False
                
        # start search
        for i in xrange(y):
            for j in xrange(x):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
                    
        return False
        
                
def test_main():   
    sol = Solution()
    
    board =[
        list("ABCE"),
        list("SFCS"),
        list("ADEE"),
    ]
    
    board = [["a"] * 30 for i in xrange(30)]
    board[29][29] = "b"
    
    words= ["ABCCED", "SEE", "ABCB", "b"+"a"*899]
       
    for word in words:
        print("%s exist = %s" % (word, sol.exist(board, word)))
       
        
if __name__ == "__main__":
    test_main()
    
