# from copy import deepcopy
# import pygame

# RED = (255,0,0)
# WHITE = (255, 255, 255)

# def minimax(position, depth, max_player, game,alpha,beta):
#     if depth == 0 or position.winner() != None:
#         return position.evaluate(), position
    
#     if max_player:
#         maxEval = float('-inf')
#         best_move = None
#         for move in get_all_moves(position, WHITE, game):
#             evaluation = minimax(move, depth-1, False, game,alpha,beta)[0]
#             maxEval = max(maxEval, evaluation)
#             alpha = max(alpha,maxEval)
#             if maxEval == evaluation:
#                 best_move = move
#             if beta <=alpha:    
#                 break
#         return maxEval, best_move
#     else:
#         minEval = float('inf')
#         best_move = None
#         for move in get_all_moves(position, RED, game):
#             evaluation = minimax(move, depth-1, True, game,alpha,beta)[0]
#             minEval = min(minEval, evaluation)
#             beta = min(beta,minEval)
#             if  minEval == evaluation:
#                 best_move = move
#             if beta <=alpha:
#                 break
#         return minEval, best_move


# def simulate_move(piece, move, board, game, skip):
#     board.move(piece, move[0], move[1])
#     if skip:
#         board.remove(skip)

#     return board


# def get_all_moves(board, color, game):
#     moves = []
#     for piece in board.get_all_pieces(color):
#         valid_moves = board.get_valid_moves(piece)
#         for move, skip in valid_moves.items():
#             draw_moves(game, board, piece)
#             temp_board = deepcopy(board)
#             temp_piece = temp_board.get_piece(piece.row, piece.col)
#             new_board = simulate_move(temp_piece, move, temp_board, game, skip)
#             moves.append(new_board)
#     return moves



# def draw_moves(game, board, piece):
#     valid_moves = board.get_valid_moves(piece)
#     board.draw(game.win)
#     pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
#     game.draw_valid_moves(valid_moves.keys())
#     pygame.display.update()
#     pygame.time.delay(100)

# --------------------------------------------------------------------------------------

from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game, alpha, beta):
    # Base case: depth reached or game over
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    best_move = None  # Initialize best move for this depth

    if max_player:
        max_eval = float('-inf')  # Start with the worst case for max player
        for move in get_all_moves(position, WHITE, game):
            evaluation, _ = minimax(move, depth - 1, False, game, alpha, beta)
            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move
            alpha = max(alpha, max_eval)
            if beta <= alpha:  # Prune branches
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')  # Start with the worst case for min player
        for move in get_all_moves(position, RED, game):
            evaluation, _ = minimax(move, depth - 1, True, game, alpha, beta)
            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move
            beta = min(beta, min_eval)
            if beta <= alpha:  # Prune branches
                break
        return min_eval, best_move


def simulate_move(piece, move, board, game, skip):
    """
    Apply a move to the board, including capturing any skipped pieces.
    """
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board


def get_all_moves(board, color, game):
    """
    Generate all possible moves for a given color.
    """
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    return moves


def draw_moves(game, board, piece):
    """
    Visualize valid moves for a piece on the game window.
    """
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(100)

