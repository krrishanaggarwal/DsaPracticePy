# Count the number of islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ##Bfs
#         if not grid:
#             return
        
#         rows=len(grid)
#         cols=len(grid[0])
#         count=0
#         q=collections.deque()
#         visit=set()
#         def bfs(r,c):    
#             q.append((r,c))
#             visit.add((r,c))
            
#             while(q):
#                 row,col=q.popleft()
#                 directions=[[-1,0],[0,1],[1,0],[0,-1]]##top,right,down,bottom
#                 for dr,dc in directions:
#                     adjRow,adjCol=row+dr,col+dc
                    
#                     if (adjRow in range(rows) 
#                         and adjCol in range(cols) 
#                         and grid[adjRow][adjCol]=="1" 
#                         and (adjRow,adjCol) not in visit):
                        
#                         q.append((adjRow,adjCol))
#                         visit.add((adjRow,adjCol))

        
#         for r in range(rows):
#             for c in range(cols):
#                 if (r,c) not in visit and grid[r][c]=="1":
#                     bfs(r,c)
#                     count+=1
#         return count
    
    ##Dfs
    
        rows=len(grid)
        cols=len(grid[0])
        count=0
        visited=set()
    
        
        def dfs(r,c):
            visited.add((r,c))
            ##Adjacent nodes
            directions=[[-1,0],[0,1],[1,0],[0,-1]] ##top,right,down,bottom
            for dr,dc in directions:
                adjRow,adjCol=r+dr,c+dc
                
                if  (adjRow in range(rows) 
                        and adjCol in range(cols) 
                        and grid[adjRow][adjCol]=="1" 
                        and (adjRow,adjCol) not in visited):
                    
                    dfs(adjRow,adjCol)

        if not grid:
            return
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]=="1":
                    dfs(r,c)
                    count+=1
        return count

        