class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowsArr = [False for i in range(ROWS)]
        colsArr = [False for j in range (COLS)]
        for i in range(ROWS):         
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rowsArr[i] = True
                    colsArr[j] = True
              
        for i in range(ROWS):         
            for j in range(COLS):  
                if rowsArr[i] or colsArr[j]:
                    matrix[i][j] = 0
