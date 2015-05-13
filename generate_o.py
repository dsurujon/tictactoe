#define how the computer plays, I just went with random placement of the O
#but you can change this function if you want a more intelligent strategy
def generate_o(board):
    #see how many spots are available
    available=board.count(-1)
    #generate a random number for the choice
    n=int(random.random()*available)
    #find the nth available spot on the board
    bsub=board
    for i in range(n):
        bsub=bsub[bsub.index(-1)+1:]
    return len(board)-len(bsub)-1
