# Chess Dictionary Program
print("Nikhil N,USN:1AY24AI075,SEC:O")
def validate_chessboard(chess_dict):
    valid_squares = [f"{file}{rank}" for file in "abcdefgh" for rank in "12345678"]
    valid_pieces = ["wp", "wR", "wN", "wB", "wQ", "wK",
                    "bp", "bR", "bN", "bB", "bQ", "bK"]
    
    # Check keys
    for square in chess_dict.keys():
        if square not in valid_squares:
            return False, f"Invalid square: {square}"
    
    # Check values
    for piece in chess_dict.values():
        if piece not in valid_pieces:
            return False, f"Invalid piece: {piece}"

    # Count pieces
    piece_counts = {p: 0 for p in valid_pieces}
    for piece in chess_dict.values():
        piece_counts[piece] += 1
    
    # Basic piece count validation:
    if piece_counts["wK"] != 1:
        return False, "There must be exactly one white king."
    if piece_counts["bK"] != 1:
        return False, "There must be exactly one black king."

    # Max pawns per side is 8
    if piece_counts["wp"] > 8:
        return False, "Too many white pawns."
    if piece_counts["bp"] > 8:
        return False, "Too many black pawns."
    
    # Max pieces per side limit (optional, basic)
    white_pieces = sum(piece_counts[p] for p in valid_pieces if p.startswith('w'))
    black_pieces = sum(piece_counts[p] for p in valid_pieces if p.startswith('b'))

    if white_pieces > 16:
        return False, "Too many white pieces."
    if black_pieces > 16:
        return False, "Too many black pieces."
    
    return True, "Chessboard is valid."
# Example usage:
chessboard = {
    "a1": "wR", "b1": "wN", "c1": "wB", "d1": "wQ", "e1": "wK", "f1": "wB", "g1": "wN", "h1": "wR",
    "a2": "wp", "b2": "wp", "c2": "wp", "d2": "wp", "e2": "wp", "f2": "wp", "g2": "wp", "h2": "wp",
    "a7": "bp", "b7": "bp", "c7": "bp", "d7": "bp", "e7": "bp", "f7": "bp", "g7": "bp", "h7": "bp",
    "a8": "bR", "b8": "bN", "c8": "bB", "d8": "bQ", "e8": "bK", "f8": "bB", "g8": "bN", "h8": "bR"
}

valid, message = validate_chessboard(chessboard)
print(message)



