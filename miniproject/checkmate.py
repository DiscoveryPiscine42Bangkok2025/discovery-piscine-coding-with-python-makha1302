def checkmate(board_str):
    try:
        # ตรวจว่าข้อมูลที่ส่งเข้ามาต้องเป็น string
        if not isinstance(board_str, str):
            raise ValueError("Input must be a string")

        # แปลง string -> board (list ของ list)
        rows = board_str.strip().split('\n')
        if not rows or all(r.strip() == "" for r in rows):
            raise ValueError("Board is empty")

        # ตรวจว่าทุกแถวต้องมีความยาวเท่ากัน
        row_len = len(rows[0])
        if any(len(r) != row_len for r in rows):
            raise ValueError("Board rows must have the same length")

        board = [list(row) for row in rows]
        n = len(board)
        m = len(board[0])

        # เช็คตัวอื่นที่ไม่ใช้
        allowed = {'K', 'P', 'B', 'R', 'Q', '.'}
        for i in range(n):
            for j in range(m):
                if board[i][j] not in allowed:
                    raise ValueError(f"Invalid character '{board[i][j]}' at ({i},{j})")

        king_pos = None
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'K':
                    king_pos = (i, j)
                    break
            if king_pos:
                break

        if not king_pos:
            print("Fail (No King found)")
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

        print("Fail")

    except Exception as e:
        print(f"Error: {e}")