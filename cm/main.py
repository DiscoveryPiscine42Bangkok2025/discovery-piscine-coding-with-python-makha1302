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
........
........
...K....
........
"""
    checkmate(board3)   #For TEST

if __name__ == "__main__":
    main()