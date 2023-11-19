from typing import Optional, List 

def pacific_atlantic(heights: List[List[int]]) -> List[int]: 

    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()

    res = []

    def dfs(r,c, visit, prevHeight):
        if ((r,c) in visit or r < 0 or c < 0 
            or r == ROWS or c == COLS or 
            heights[r][c] < prevHeight
            ):
            return 
        visit.add((r,c))
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])


    
    return res 

