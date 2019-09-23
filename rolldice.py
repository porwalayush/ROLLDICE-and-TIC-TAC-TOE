import random
min = 1
max = 6

d='y'
name1=input("\nEnter First Player Name : ")
name2=input("\nEnter Second Player Name : ")
score1=0
score2=0
i=0

while i<6:
    print( "Rolling the dices...")
    print("The values are....")
    c1=random.randint(min, max)
    c2=random.randint(min, max)
    score1=score1+c1
    score2=score2+c2
    print(c1)
    print(c2)
    i+=1

print(score1)
print(score2)



def text_random():
    min=65
    max=74
    ran=random.randint(min, max)
    print("you got a special character",chr(ran))
    



def tic_tac_toe(a1):
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p1()
        else:
            board[n] = "X"

    def p2():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p2()
        else:
            board[n] = "O"

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nThat's not on the board. Try again")
                        continue
                except ValueError:
                   print("\nThat's not a number. Try again")
                   continue

    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print(a1," Wins!\n")
                print("Congratulations!\n")
                text_random()
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Player 3  Wins!\n")
                print("Congratulations!\n")
                text_random()
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print(a1," choose where to place a cross")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 3 choose where to place a nought")
        p2()
        print()

    
if score1<score2:
    print(name2,"wins the match")
    tic_tac_toe(name2)
else:
    print(name1,"wins the match")
    tic_tac_toe(name1)
    
