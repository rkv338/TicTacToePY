from IPython.display import clear_output
import random


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
def choose_first():
	c = random.randint(1,2)
	if c == 1:
		return 'Player 1'
	else:
		return 'Player 2'

def space_check(board, position):
	if board[position]:
		return True
	else:
		return False
def full_board_check(board):
	for x in range(0, len(board) - 1):
		if space_check(board, x) == False:
			return False
	return True

def player_choice(board):
	pos = 0
	while  not space_check(board,pos):
		pos = int(input('Position of move?'))
	
	return pos

def replay():
	play = input('Play again? (Y or N)')
	play = play.lower()
	if play == 'y':
		return True
	else if play == 'n':
		return False


