#!/usr/bin/python3

import sys

def is_attacked(board, row, col):
  for i in range(row):
    if board[i][col] == 1:
      return True
  for i in range(row - 1, -1, -1):
    if board[i][col] == 1 and col - row + i >= 0:
      return True
  for i in range(col):
    if board[row][i] == 1:
      return True
  for i in range(col - 1, -1, -1):
    if board[row][i] == 1 and col - row + i >= 0:
      return True
  return False

def solve(board, n):
  if n == 0:
    print(board)
    return
  for col in range(n):
    if not is_attacked(board, n - 1, col):
      board[n - 1][col] = 1
      solve(board, n - 1)
      board[n - 1][col] = 0

def main():
  if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
  try:
    n = int(sys.argv[1])
  except ValueError:
    print("N must be a number")
    sys.exit(1)
  if n < 4:
    print("N must be at least 4")
    sys.exit(1)
  board = [[0] * n for _ in range(n)]
  solve(board, n)

if __name__ == "__main__":
  main()
