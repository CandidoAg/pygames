from Piece import Piece
from SpriteSheet import SpriteSheet


class ChessSet:
    """Represents a set of chess pieces.
    Each piece is an object of the Piece class.
    """

    def __init__(self, chess_game):
        """Initialize attributes to represent the overall set of pieces."""

        self.chess_game = chess_game
        self.pieces = []
        self._load_pieces()

    def _load_pieces(self):
        """Builds the overall set:
        - Loads images from the sprite sheet.
        - Creates a Piece object, and sets appropriate attributes
          for that piece.
        - Adds each piece to the list self.pieces.
        """
        filename = 'chess_pieces.bmp'
        piece_ss = SpriteSheet(filename)

        # Create a black king.
        b_king_rect = (68, 70, 85, 85)
        b_king_image = piece_ss.image_at(b_king_rect)

        b_king = Piece(self.chess_game)
        b_king.image = b_king_image
        b_king.name = 'king'
        b_king.color = 'black'
        self.pieces.append(b_king)