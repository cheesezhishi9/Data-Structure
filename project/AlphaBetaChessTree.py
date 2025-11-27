from TreeNode import TreeNode
import chess
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns
import numpy as np

class AlphaBetaChessTree:
    def __init__(self, fen):
        """
        Initializes an AlphaBetaChessTree object with a board state.
        The board state is represented in FEN (Forsyth-Edwards Notation) format.
        :param fen: A string representing the chess board in FEN format.
        """
        self.root = TreeNode(chess.Board(fen), chess.WHITE if fen.split()[1] == 'w' else chess.BLACK)
        self.pruned_nodes = 0
        self.total_nodes_visited = 0
        self.max_depth_reached = 0
        self.candidate_moves = {}

    @staticmethod
    def get_supported_evaluations():
        """
        Static method that returns a list of supported evaluation methods.
        :return: A list of strings containing supported evaluation methods.
        """
        return ["Material Count", "Positional",'Mobility','King Safety']

    def _apply_move(self, move, node, notation="SAN"):
        """
        Applies a chess move to a given game state (node).
        :param move: The move to be applied.
        :param node: The game state to which the move is applied.
        :param notation: The notation system used for the move (default: "SAN" - Standard Algebraic Notation).
        """
        if notation == "SAN":
            move = node._board.parse_san(move)
        elif notation == "UCI":
            move = node._board.parse_uci(move)
        node._board.push(move)
    

    def _get_legal_moves(self, node, notation="SAN"):
        """
        Returns a list of all legal moves from the given game state (node).
        :param node: The game state from which to get legal moves.
        :param notation: The notation system used for the moves (default: "SAN").
        :return: A list of strings representing all legal moves for a given node.
        """
        moves = list(node._board.legal_moves)


        if notation == "SAN":
            return [node.san(move) for move in moves]
        else:
            return [node.uci(move) for move in moves]

    def get_best_next_move(self, node, depth, notation="SAN"):
        """
        Determines the best next move for the current player using the Alpha-Beta pruning algorithm.
        :param node: The current game state.
        :param depth: The depth of the search tree to explore.
        :param notation: The notation system for the move (default: "SAN").
        :return: The best next move in the format defined by the variable notation.
        """
        #self.transposition_table = {}
        self.transposition_table = {}
        self.candidate_moves = {}
        board = chess.Board(node)  # Assumes 'node' is a valid FEN string

    # Determine which color's turn it is from the FEN string
        turn = chess.WHITE if node.split()[1] == 'w' else chess.BLACK
    
    # Create a new TreeNode for the board and turn
        new_node = TreeNode(board, turn)
    
    # Proceed with finding the best move using alpha-beta pruning
        best_move = self._alpha_beta(new_node, depth, float('-inf'), float('inf'), turn == chess.WHITE)[1]
        if best_move:
            return new_node._board.san(best_move) if notation == "SAN" else new_node._board.uci(best_move)
        return None
    

        
    def _alpha_beta(self, node, depth, alpha, beta, maximizing_player):
        """
        The Alpha-Beta pruning algorithm implementation. This method is used to evaluate game positions.
        :param node: The current node (game state).
        :param depth: The depth of the tree to explore.
        :param alpha: The alpha value for the Alpha-Beta pruning.
        :param beta: The beta value for the Alpha-Beta pruning.
        :param maximizing_player: Boolean indicating if the current player is maximizing or minimizing the score.
        :return: The best score for the current player.
        """
        self.total_nodes_visited += 1  # Moved outside of the if condition
        self.max_depth_reached = max(self.max_depth_reached, depth)

    # Check if the position is already in the transposition table
        if node._board.fen() in self.transposition_table:
            return self.transposition_table[node._board.fen()]

        if depth == 0 or node._board.is_game_over():
            score = self._evaluate_position(node, depth)
            return score, None

        best_move = None
        if maximizing_player:
            max_eval = float('-inf')
            for move in node._board.legal_moves:
                node._board.push(move)
                child_node = TreeNode(node._board, not node._turn)
                node.add_child(child_node)
                eval, _ = self._alpha_beta(child_node, depth - 1, alpha, beta, False)
                node._board.pop()
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                    san_move = node._board.san(best_move)  # Convert move to SAN
                    self.candidate_moves[san_move] = max_eval  # Store move as SAN
                alpha = max(alpha, eval)
                if beta <= alpha:
                    self.pruned_nodes += 1
                    break
            self.transposition_table[node._board.fen()] = (max_eval, depth)
            return (max_eval, best_move)
        else:
            min_eval = float('inf')
            for move in node._board.legal_moves:
                node._board.push(move)
                child_node = TreeNode(node._board, not node._turn)
                node.add_child(child_node)
                eval, _ = self._alpha_beta(child_node, depth - 1, alpha, beta, True)
                node._board.pop()
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                    san_move = node._board.san(best_move)  # Convert move to SAN
                    self.candidate_moves[san_move] = min_eval  # Store move as SAN
                beta = min(beta, eval)
                if beta <= alpha:
                    self.pruned_nodes += 1
                    break
            self.transposition_table[node._board.fen()] = (min_eval, depth)
            return (min_eval, best_move)
        
    def _evaluate_position(self, node, depth):
        """
        Evaluates the position at a given node, taking into account the depth of the node in the decision tree.
        :param node: The game state to evaluate.
        :param depth: The depth of the node in the game tree.
        :return: An evaluation score for the position.
        """
        base_evaluation = self._evaluate_board(node._board)
        depth_factor = 1 / (depth + 1)
        adjusted_evaluation = base_evaluation * depth_factor
        return adjusted_evaluation
    
    def _evaluate_material(self, board):

        material_score = 0
        for piece_type, base_value in [(chess.PAWN, 1), (chess.KNIGHT, 3), (chess.BISHOP, 3), (chess.ROOK, 5), (chess.QUEEN, 9)]:
            for color in [True, False]:
                piece_count = len(board.pieces(piece_type, color))
                value = base_value + 0.1 * piece_count  # Slight increase per piece of the same type
                if board.turn == color:
                    material_score += piece_count * value
                else:
                    material_score -= piece_count * value
        return material_score
    
    def _evaluate_mobility(self, board):

        mobility_score = 0
        for move in board.legal_moves:
            mobility_score += 1
            if move.to_square in [chess.D4, chess.E4, chess.D5, chess.E5]:
                mobility_score += 0.5  # Central control bonus
        if board.turn == chess.WHITE:
            return mobility_score
        else:
            return -mobility_score
    
    def _evaluate_piece_activity(self, board):

        activity_score = 0
        for piece_type in [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN]:
            for color in [True, False]:
                for square in board.pieces(piece_type, color):
                    attacks = len(board.attackers(not color, square))
                    if board.turn == color:
                        activity_score += attacks
                    else:
                        activity_score -= attacks
        return activity_score
    
  


    def _evaluate_board(self, board):
        """
        Evaluates a provided board and assigns a score.
        :param board: The board to evaluate.
        :return: An evaluation score for the board.
        """
        score = 0
        
        # Evaluate material
        score += self._evaluate_material(board)
        
        # Evaluate mobility
        score += self._evaluate_mobility(board)
        
        # Evaluate piece activity
        score += self._evaluate_piece_activity(board)
        
        # Evaluate pawn structure
        score += self._evaluate_pawn_structure(board)
        
        # Evaluate king safety
        score += self._evaluate_king_safety(board)
        
        # Evaluate central control
        score += self._evaluate_central_control(board)
        
        # Ensure positive scores for the side to move
        return score if board.turn == chess.WHITE else -score
    # Ensure positive scores for the side to move
        #return total_score if board.turn == chess.WHITE else -total_score
    
    def _get_piece_square_score(self, board, piece, value):

        score = sum(len(board.pieces(piece, color)) * value
                for color in [True, False]
                for square in board.pieces(piece, color)
                for rank in range(8)  # Iterate over ranks using range(8)
                for file in range(8)  # Iterate over files using range(8)
                if square == chess.square(file, rank) and board.color_at(square) == color)
        return score
    
    def _evaluate_pawn_structure(self, board):
        pawn_structure_score = 0
    # Consider pawn structure related to potential pawn breaks
        if board.piece_at(chess.E4) and board.piece_at(chess.D2) is None:
            pawn_structure_score += 1
        if board.piece_at(chess.D4) and board.piece_at(chess.C2) is None:
            pawn_structure_score += 1
        if board.piece_at(chess.E5) and board.piece_at(chess.D7) is None:
            pawn_structure_score += 1
        if board.piece_at(chess.D5) and board.piece_at(chess.C7) is None:
            pawn_structure_score += 1
        return pawn_structure_score
    
    def _evaluate_king_safety(self, board):
        king_safety_score = 0
    
        white_king_square = board.king(chess.WHITE)
        black_king_square = board.king(chess.BLACK)
    
    # Debugging: Check if king positions are correctly fetched
        if white_king_square is None or black_king_square is None:
            raise ValueError("King position could not be determined. Check board setup.")
    
        if board.turn == chess.WHITE:
            king_safety_score += len(board.attackers(chess.BLACK, white_king_square))
            king_safety_score -= len(board.attackers(chess.WHITE, black_king_square))
        else:
            king_safety_score -= len(board.attackers(chess.BLACK, white_king_square))
            king_safety_score += len(board.attackers(chess.WHITE, black_king_square))

        return king_safety_score
    
    def _evaluate_central_control(self, board):
        central_control_score = 0
        
        central_squares = [chess.D4, chess.E4, chess.D5, chess.E5]
        for square in central_squares:
            if board.piece_at(square) and board.piece_at(square).color == board.turn:
                central_control_score += 1
            elif board.piece_at(square) and board.piece_at(square).color != board.turn:
                central_control_score -= 1
        return central_control_score
    
    def get_board_visualization(self, board):
        """
        Generates a visual representation of the board.
        :param board: The board to visualize.
        :return: A visual representation of the board.
        """
        return str(board)

    def visualize_decision_process(self, depth, move, notation="SAN"):
        """
        Visualizes the decision-making process for a particular move up to a certain depth.
        :param depth: The depth of the analysis.
        :param move: The move being analyzed.
        :param notation: The notation system for the move (default: "SAN").
        """
        print(f"Visualizing the decision process for move {move} at depth {depth}.")
        G = nx.DiGraph()
        labels = {}
        positions = {}
        pos_x, pos_y = 0, 0
        stack = [(self.root, pos_x, pos_y, 0)]  # Include current depth in stack

        while stack:
            node, x, y, current_depth = stack.pop(0)
            if current_depth > depth:  # Stop if the current depth exceeds the maximum depth
                continue

            label = f"{node._board.fen().split()[0]} ({current_depth})"
            G.add_node(label)
            labels[label] = label
            positions[label] = (x, -y)  # Negative y to display top-down

            for child in node._children:
                child_label = f"{child._board.fen().split()[0]} ({current_depth + 1})"
                G.add_edge(label, child_label)
                stack.append((child, x + 1, y + len(node._children), current_depth + 1))

        nx.draw(G, pos=positions, labels=labels, with_labels=True, node_size=2000, node_color='lightblue', edge_color='gray', arrowstyle='-|>')
        plt.show()
    
    def visualize_game_tree(self):
        G = nx.DiGraph()
        labels = {}
        positions = {}
        pos_x, pos_y = 0, 0
        node_queue = [(self.root, pos_x, pos_y)]

        while node_queue:
            node, x, y = node_queue.pop(0)
            label = node._board.fen().split(' ')[0]
            G.add_node(label, color='lightblue' if node._score is not None else 'lightcoral')
            labels[label] = f"{label}\nScore: {node._score if node._score is not None else 'Pruned'}"
            positions[label] = (x, -y)

            for child in node._children:
                child_label = child._board.fen().split(' ')[0]
                G.add_edge(label, child_label)
                node_queue.append((child, x + 1, y - 1))

        colors = [node[1]['color'] for node in G.nodes(data=True)]
        nx.draw(G, pos=positions, labels=labels, with_labels=True, node_color=colors, node_size=2500)
        plt.show()
    
    def generate_heatmap(self):
        board_heat = np.zeros((8, 8))
        for move, score in self.candidate_moves.items():
            start_square = chess.SQUARE_NAMES.index(move[:2])
            board_heat[start_square // 8][start_square % 8] += score

        plt.figure(figsize=(10, 10))
        sns.heatmap(board_heat, annot=True, fmt=".0f", cmap='coolwarm', xticklabels=chess.SQUARE_NAMES[0:8], yticklabels=list(reversed(chess.SQUARE_NAMES[0:8])))
        plt.title("Heatmap of Move Scores")
        plt.show()
    
    def plot_evaluation_scores(self):
        scores = list(self.candidate_moves.values())

        plt.figure(figsize=(12, 6))
        plt.plot(scores, 'o', label="Evaluation Scores")

        plt.xlabel("Move Index")
        plt.ylabel("Evaluation Score")
        plt.title("Evaluation Scores by Move")
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def report_analytics(self):
        print("Descriptive Analytics Report:")
        print(f"Total Nodes Visited: {self.total_nodes_visited}")
        print(f"Pruned Nodes: {self.pruned_nodes}")
        print(f"Max Depth Reached: {self.max_depth_reached}")
        print("Evaluation Scores of Top Candidate Moves:")
        for move, score in self.candidate_moves.items():
            print(f"Move: {move}, Score: {score}")
        print(f"Search Efficiency: {100 * (1 - self.pruned_nodes / self.total_nodes_visited):.2f}% (higher is better)")