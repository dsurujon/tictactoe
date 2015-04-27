def check_win(board):
	win_cond = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))
	for each in win_cond:
		try:
			if board[each[0]-1] == board[each[1]-1] and board[each[1]-1] == board[each[2]-1]:
				return board[each[0]-1]
		except:
			pass
	return -1