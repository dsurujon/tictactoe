from print_instruction import print_instruction
def get_input(turn):

	valid = False
	while not valid:
		try:
			user = raw_input("Where would like to place " + turn + " (1-9)? ")
			user = int(user)
			if user >= 1 and user <= 9:
				return user-1
			else:
				print "That is not a valid move! Please try again.\n"
				print_instruction()
		except Exception as e:
			print user, "is not a valid move! Please try again.\n"
			print_instruction()