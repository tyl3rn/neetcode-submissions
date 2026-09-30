class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return None
        ROWS, COLS = len(board), len(board[0])


        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):  
                num = board[r][c]
                if num == ".":
                    continue
                if num in row[r] or num in col[c] or num in box[(r // 3, c // 3)]:
                    return False
                else:
                    row[r].add(num)
                    col[c].add(num)
                    box[(r // 3, c // 3)].add(num)
        return True
        
