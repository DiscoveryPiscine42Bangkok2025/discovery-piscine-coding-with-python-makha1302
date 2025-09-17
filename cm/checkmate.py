def checkmate(board_str):
    board = [list(row) for row in board_str.strip().split('\n')]
    n = len(board)
    m = len(board[0])

    king_pos = None
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail")
        return

    ki, kj = king_pos

    # Pawn (P)
    pawn_attacks = [(1, -1), (1, 1)]
    for di, dj in pawn_attacks:
        ni, nj = ki + di, kj + dj
        if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 'P':
            print("Success")
            return

    # Bishop (B)
    bishop_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for di, dj in bishop_dirs:
        ni, nj = ki, kj
        while True:
            ni += di
            nj += dj
            if not (0 <= ni < n and 0 <= nj < m):
                break
            if board[ni][nj] != '.':
                if board[ni][nj] == 'B':
                    print("Success")
                    return
                else:
                    break

    # Rook (R)
    rook_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in rook_dirs:
        ni, nj = ki, kj
        while True:
            ni += di
            nj += dj
            if not (0 <= ni < n and 0 <= nj < m):
                break
            if board[ni][nj] != '.':
                if board[ni][nj] == 'R':
                    print("Success")
                    return
                else:
                    break

    # Queen (Q)
    queen_dirs = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    for di, dj in queen_dirs:
        ni, nj = ki, kj
        while True:
            ni += di
            nj += dj
            if not (0 <= ni < n and 0 <= nj < m):
                break
            if board[ni][nj] != '.':
                if board[ni][nj] == 'Q':
                    print("Success")
                    return
                else:
                    break

    # Knight (N)
    knight_moves = [(-2, -1), (-2, 1), (2, -1), (2, 1),
                    (-1, -2), (-1, 2), (1, -2), (1, 2)]
    for di, dj in knight_moves:
        ni, nj = ki + di, kj + dj
        if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 'N':
            print("Success")
            return

    print("Fail")