#miniproject
#chabumru and tthongch
from checkmate import checkmate

def main():
    # Example 1
    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1)   #Success

    # Example 2
    board2 = """\
..
.K\
"""
    checkmate(board2)   #Fail

    #For TEST
    board3 = """\
....B...
......K.
......B.
....Q.RP
"""
    checkmate(board3)   #For TEST

        #For TEST no king
    board4 = """\
........
........
........
........
"""
    checkmate(board4)   #For TEST

        #For TEST only king
    board5 = """\
........
........
........
.......K
"""
    checkmate(board5)   #For TEST

        #For TEST 2 king
    board6 = """\
....K...
........
........
.......K
"""
    checkmate(board6)   #For TEST

 #For TEST 2 king
    board6 = """\
....P...
..E.....
..X...B.
.......K
"""
    checkmate(board6)   #For TEST

 #For TEST Err1
    board7 = 1

    checkmate(board7) #For TEST

 #For TEST Err2
    board8 = """\
"""
    checkmate(board8)   #For TEST

if __name__ == "__main__":
    main()