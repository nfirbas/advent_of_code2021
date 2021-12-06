def mark_guess(boards, guess):
    for board in range(len(boards)):
        for row in range(5):
            for number in range(5):
                if  boards[board][row][number] == guess:
                    boards[board][row][number] = -1
    return boards

def check_win(boards):
    for board in range(len(boards)):
        for row in range(5):
            if sum(boards[board][row]) == -5 or vertical_sum(boards[board], row) == -5:
                return board
    return -1

def vertical_sum(board, row):
    sum = 0
    for i in range(5):
        sum += board[i][row]
    return sum

def get_whining_board_sum(board, boards):
    board_sum = 0 
    for i in range(5): 
        board_sum += sum([x if x != -1 else 0 for x in boards[board][i]])
    return board_sum

def solve_first(boards, guesses):
    for guess in guesses:
        mark_guess(boards, guess)
        
        whining_board = check_win(boards)
        if check_win(boards) != -1:            
            print(guess * get_whining_board_sum(whining_board, boards))
            break

def solve_second(boards, guesses):
    for guess in guesses:
        mark_guess(boards, guess)
        while check_win(boards) != -1:
            if len(boards) != 1:
                del boards[check_win(boards)]
            else: 
                print(guess * get_whining_board_sum(0, boards))
                print(boards)
                return

if __name__ == "__main__":
    f = open("./input.txt", "r")
    guesses = [int(x) for x in f.readline().split(',')]
    f.readline()

    boards =[]
    board = []
    for x in f:
        temp = [int(j) for j in x.split()]
        if len(temp) == 0:
            boards.append(board)
            board = []
        else:
            board.append(temp)
    boards.append(board)
    f.close()

    solve_first(boards, guesses)
    solve_second(boards, guesses)
        

    #print(guess)