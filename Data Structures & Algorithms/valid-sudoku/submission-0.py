class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def box(m,row,col):
            s = set()
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    if m[row + i][col+j] not in s and m[row + i][col+j] != ".":
                        s.add(m[row + i][col+j])
                    elif m[row + i][col+j] in s:
                        return False
            return True
        def ver(m,col):
            s = set()
            for i in range(9):
                if m[i][col] not in s and m[i][col] != ".":
                        s.add(m[i][col])
                elif m[i][col] in s:
                        return False
            return True
        def hor(m,row):
            s = set()
            for i in range(9):
                if m[row][i] not in s and m[row][i] != ".":
                        s.add(m[row][i])
                elif m[row][i] in s:
                        return False
            return True
        
        
        for i in [1,4,7]:
            for j in [1,4,7]:
                if not box(board,i,j):
                    return False
        for i in range(9):
            if not ver(board,i) or not hor(board,i):
                return False 
        return True