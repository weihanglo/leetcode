// Question: https://leetcode.com/problems/valid-sudoku/
//
// Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
// http://sudoku.com.au/TheRules.aspx
//
// The Sudoku board could be partially filled,
// where empty cells are filled with the character '.'.
//
// Note:
// A valid Sudoku board (partially filled) is not necessarily solvable. 
// Only the filled cells need to be validated. 

/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
  for (let i = 0; i < 9; i++) {
    const rowCheck = new Set()
    const colCheck = new Set()
    const cubeCheck = new Set()
    for (let j = 0; j < 9; j++) {
      const rowEl = board[i][j]
      if (rowEl !== '.') {
        if (rowCheck.has(rowEl)) {
          return false
        }
        rowCheck.add(rowEl)
      }
      const colEl = board[j][i]
      if (colEl !== '.') { 
        if (colCheck.has(colEl)) {
          return false
        }
        colCheck.add(colEl)
      }
      const cubeRow = 3 * Math.floor(i / 3) + Math.floor(j / 3)
      const cubeCol = 3 * (i % 3) + j % 3
      const cubeEl = board[cubeRow][cubeCol]
      if (cubeEl !== '.') {
        if (cubeCheck.has(cubeEl)) {
          return false
        }
        cubeCheck.add(cubeEl)
      }
    }
  }
  return true
};
