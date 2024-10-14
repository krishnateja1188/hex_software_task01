def print_board(board):
  """Prints the current state of the Tic-Tac-Toe board."""
  for row in board:
    print(" | ".join(row))
    print("-" * 9)

def check_winner(board):
  """Checks if there's a winner or if the game is a draw."""
  # Check rows and columns
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
      return board[i][0]
    if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
      return board[0][i]

  # Check diagonals
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
    return board[0][2]

  # Check if the board is full
  if all(all(cell != " " for cell in row) for row in board):
    return "Draw"

  return None

def play_game():
  """Main function to play the Tic-Tac-Toe game."""
  board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
  current_player = "X"

  while True:
    print_board(board)
    row = int(input(f"Player {current_player}, enter the row number (1-3): ")) - 1
    col = int(input(f"Player {current_player}, enter the column number (1-3): ")) - 1

    if row < 0 or row >= 3 or col < 0 or col >= 3 or board[row][col] != " ":
      print("Invalid move. Please try again.")
      continue

    board[row][col] = current_player
    winner = check_winner(board)

    if winner:
      print_board(board)
      print(f"Player {winner} wins!")
      break

    current_player = "O" if current_player == "X" else "X"

if _name_ == "_main_":
  play_game()
