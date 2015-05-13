from print_instruction import print_instruction
from board import print_board
from input import get_input
from checkwin import check_win
from quitgame import quit_game

def main():
	
	print_instruction()
	
	#board = []
	#for i in range(9):
	#	board.append(-1)
	board=[-1 for i in range(9)] #this is quicker than a for loop+append, for future reference :)
	
	
	win = False
	move = 0
	while not win:

		print_board(board)
		print "Turn number" + str(move+1)
        	if move % 2 == 0:
            		#this is the user
            		turn = 'X'
            		user = get_input(turn)
            		while board[user] != -1:
                		print "Invalid move! Cell already taken. Please try again.\n"
                		user = get_input(turn)
            		board[user] = 1
        	else:
            		#this will be the computer
            		turn = 'O'
            		comp=generate_o(board)#computer behaviour define
            		board[comp]=0
		move += 1
		if move > 4:
			winner = check_win(board)
			if winner != -1:
				out = "The winner is"
				out += "X" if winner == 1 else "O"
				out += "=D"
				quit_game(board,out)
			elif move >= 9:
				quit_game(board, "No winner :(")
				
if __name__== "__main__": 
	main()
