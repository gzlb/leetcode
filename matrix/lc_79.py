from collections import defaultdict, Counter

def exist(board, word) -> bool: 
    board_dic = defaultdict(int)

    # count number of letters in the board 
    for i in range(len(board)):
        for j in range(len(board[0])):
            board_dic[board[i][j]] += 1 

    wordDic = Counter(word)

    for c in wordDic: 
        if c not in board_dic or board_dic[c] < wordDic[c]:
            return False 
        
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]: 
                if dfs(i,j, 0, board,word):
                    return True 
                
    return False 
    
    
def dfs(i,j, k, board, word): 
    if ( i < 0 or
         j < 0 or
         i >= len(board) or 
         j >= len(board[0]) or 
         k >= len(word) or 
         word[k] != board[i][j] 
         ): 
        return False 
    
    if k == len(word) - 1:
        return True 
    

    directions = [(1,0), (-1,0), (0,-1), (0,1)]

    for x,y in directions:
        tmp = board[i][j]

        board[i][j] -= 1 

        if dfs(i + x, j + y, k +1, board, word):
            return True
        
        board[i][j] = tmp 
    return False 



        