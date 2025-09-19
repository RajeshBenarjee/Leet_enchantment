class Spreadsheet:
    def __init__(self, rows: int):
        """
        Initialize a spreadsheet with 26 columns (A–Z) and given number of rows.
        We'll store only explicitly set cells in a dictionary for efficiency.
        """
        self.rows = rows
        self.cells = {}  # key: cell string like "A1", value: int

    def setCell(self, cell: str, value: int) -> None:
        """
        Set the given cell (e.g. 'B10') to the specified integer value.
        """
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        """
        Reset the given cell to 0. We can simply remove it to treat as 0.
        """
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula: str) -> int:
        """
        Evaluate a formula of the form '=X+Y', where X and Y are either integers
        or valid cell references. Returns the computed sum.
        """
        # Remove the leading '=' and split by '+'
        parts = formula[1:].split('+')
        total = 0

        for p in parts:
            # If p is digits, treat as integer; else treat as cell reference
            if p.isdigit():
                total += int(p)
            else:
                # cell reference
                total += self.cells.get(p, 0)
        return total
