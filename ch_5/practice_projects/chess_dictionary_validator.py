#!/usr/bin/env python3
# Determines if dictionary chess board is valid

def isValidChessBoard(board):
    pieces = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
    colors = ['w', 'b']
    # Board position can be defined by a-h followed by 1-8 or 
    # 1-8 followed by a-h pairs
    board_pos = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 
                'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 
                'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 
                'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 
                'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 
                'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8',
                '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', 
                '1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b', 
                '1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c', 
                '1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d', 
                '1e', '2e', '3e', '4e', '5e', '6e', '7e', '8e', 
                '1f', '2f', '3f', '4f', '5f', '6f', '7f', '8f', 
                '1g', '2g', '3g', '4g', '5g', '6g', '7g', '8g', 
                '1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h']

    # Checks if all key / positions are valid inputs
    for position in board.keys():
        if position not in board_pos:
            print(f'Invalid board position {position}.')
            return False

    valid_pieces = []
    for piece in pieces:
        for color in colors:
            valid_pieces.append(color+piece)

    # Checks if all pieces in board are valid.
    # Only one black king and one white king
    white_king = 0
    black_king = 0
    for piece in board.values():
        if piece not in valid_pieces:
            print(f'Invalid piece {piece}.')
            return False 

        if piece == 'wking':
            white_king += 1
        elif piece == 'bking':
            black_king += 1
    
    if white_king != 1 or black_king != 1:
        print('Invalid number of kings')
        return False

    return True
    # Valid board will have exactly one black and white king.

if __name__ == '__main__':
    board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
    if isValidChessBoard(board):
        print('True')
    
    invalid_board = {'a5': 'wking', 'a7': 'wqueen', 'c4': 'bqueen'}
    isValidChessBoard(invalid_board)

    invalid_board = {'a5': 'wking', 'a9': 'wqueen', 'c4': 'bqueen'}
    isValidChessBoard(invalid_board)