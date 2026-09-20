import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        sqr = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            rows = set()
            for j in range(9):
                val = board[i][j]
                sqr_r = 2 - math.floor((8-i)/3)
                sqr_c = 2 - math.floor((8-j)/3)
                cur_sqr = sqr[sqr_r][sqr_c]
                if val != '.':
                    if val not in rows:
                        rows.add(val)
                    else: return False
                    if val not in cols[j]:
                        cols[j].add(val)
                    else: return False
                    if val not in cur_sqr:
                        cur_sqr.add(val)
                    else: return False

        return True

                
                
                
                    
