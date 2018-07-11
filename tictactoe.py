from IPython.display import clear_output
import random


def display_board(board):
	print(board[7] + '|' + board[8] + '|' + board[9])
	print(board[4] + '|' + board[5] + '|' + board[6])
	print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
	player1 = ''	
	while player1 != 'X' and player1 != 'O':
		player1 = input('Player 1, type in X or O to select your marker: \n')

	return player1
	

def place_marker(board, marker, position):
	board[position] = marker

def win_check(board, mark):
	for x in range(1,4):
		if board[x] == board[x + 3] == board[x + 6] == mark:
			return True
	for x in range(1,8,3):
		if board[x] == board[x + 1] == board[x + 2] == mark:
			return True
	if board[1] == board[5] == board[9] == mark:
		return True
	elif board[7] == board[5] == board[3] == mark: 
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
	if position < 10 and position > 0:
		if board[position] != ' ':
			return True
		else:
			return False
	else:
		return False
def full_board_check(board):
	if ' ' in board[1:]:
		return False
	return True

def player_choice(board):
	pos = -1
	while  pos < 1 or pos > 9 and not space_check(board,pos):
		if pos != -1:
			print('Position not available')		
		pos = int(input('Position of move?'))
		
	
	return pos

def replay():
	play = input('Play again? (Y or N)')
	play = play.lower()
	if play == 'y':
		return True
	elif play == 'n':
		return False

print('Tic Tac Toe Game')

while True:
	board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	player1 = ''
	player2 = ''
	player1 = player_input()
	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'
	print('THIS IS PLAYER 2' + player2)
	first = choose_first()
	print(first + ' will go first.')
	
	game = True
	while game:
		
		if first == 'Player 1':
			print('PLAYER 1 GO:' + first)
			display_board(board)
			posChoice = player_choice(board)
			print(posChoice)
			place_marker(board, player1, posChoice)
			display_board(board)
			if win_check(board, player1):
				print('Player 1 won.')
				break
			elif full_board_check(board):
				print('Tie')
				break
			print("Player 2's turn")
		else:
			print('PLAYER 2 GO')
			display_board(board)
			posChoice = player_choice(board)
			print(posChoice)
			place_marker(board, player2, posChoice)
			display_board(board)
			if win_check(board, player2):
				print('Player 2 won.')
				break
			elif full_board_check(board):
				print('Tie')
				break
			print("Player 1's turn")
		if first == 'Player 1':
			first = 'Player 2'
		else:
			first = 'Player 1'
	if not replay():
		break





