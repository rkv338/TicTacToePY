from IPython.display import clear_output


def display_board(board):
	print(board[7] + '|' + board[8] + '|' + board[9])
	print(board[4] + '|' + board[5] + '|' + board[6])
	print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
	player1 = ''
	player2 = ''
	while player1 != 'X' and player1 != 'O':
		player1 = input('Player 1, type in X or O to select your marker: \n')

	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'

def place_marker(board, marker, position):
	board[position] = marker

def win_check(board, mark):
	for x in range(1,4):
		if board[x] == board[x + 3] == board[x + 6] == mark:
			return True
	for x in range(1,8,3):
		if board[x] == board[x + 1] == board[x + 2] == mark:
			return True
	if board[1] == board[5] == board[9]:
		return True
	elif board[7] == board[5] == board[3]: 
		return True
	else:
		return False