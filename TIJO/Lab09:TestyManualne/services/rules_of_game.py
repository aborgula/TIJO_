class RulesOfGame:

    """
        Metoda zwraca true, tylko gdy przejscie z polozenia source na destination w jednym ruchu jest zgodne
        z zasadami gry w szachy.
    """
    def is_correct_move(self, source, destination):
        raise NotImplementedError("Subclasses must implement this method")

class Bishop(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        return abs(source_col - dest_col) == abs(source_row - dest_row) and source != destination

class Knight(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        if source == destination:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        ruch1 = abs(source_col - dest_col) == 1 and abs(source_row - dest_row) == 2
        ruch2 = abs(source_col - dest_col) == 2 and abs(source_row - dest_row) == 1

        return ruch1 or ruch2

class Pawn(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        if source == destination:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination
        ruch = abs(source_col - dest_col) == 0 and abs(source_row - dest_row) == 1

        return ruch

class King(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        if source == destination:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        ruch1 = abs(source_col - dest_col) == 1 and abs(source_row - dest_row) == 1
        ruch2 = abs(source_col - dest_col) == 0 and abs(source_row - dest_row) == 1
        ruch3 = abs(source_col - dest_col) == 1 and abs(source_row - dest_row) == 0

        return ruch1 or ruch2 or ruch3

class Rook(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        if source == destination:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        ruch1 = source_col == dest_col and source_row != dest_row
        ruch2 = source_col != dest_col and source_row == dest_row

        return ruch1 or ruch2

class Queen(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        if source == destination:
            return False
        source_col, source_row = source
        dest_col, dest_row = destination

        ruch1 = source_col == dest_col and source_row != dest_row
        ruch2 = source_col != dest_col and source_row == dest_row

        return ruch1 or ruch2 or (abs(source_col - dest_col) == abs(source_row - dest_row))
