class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Initialize sets with existing numbers
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(i=0) -> bool:
            if i == len(empty_cells):  # all filled
                return True

            r, c = empty_cells[i]
            box_idx = (r // 3) * 3 + (c // 3)

            for ch in map(str, range(1, 10)):
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[box_idx]:
                    # Place digit
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box_idx].add(ch)

                    if backtrack(i + 1):
                        return True

                    # Undo choice
                    board[r][c] = "."
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box_idx].remove(ch)

            return False

        backtrack()