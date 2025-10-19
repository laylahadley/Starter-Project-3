class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

        # Normalize dictionary
        self.dictionary = set(word.upper() for word in dictionary)

        # Precompute prefixes for pruning
        self.prefixes = set()
        for word in self.dictionary:
            for i in range(1, len(word) + 1):
                self.prefixes.add(word[:i])

        self.solutions = set()

    def getSolution(self):
        self.solutions.clear()
        for r in range(self.rows):
            for c in range(self.cols):
                self._dfs(r, c, set(), "")
        # Always return uppercase sorted list
        return sorted(word.upper() for word in self.solutions)

    def _dfs(self, r, c, visited, current):
        # Out of bounds
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols:
            return
        if (r, c) in visited:
            return

        # Add this tile
        token = self.grid[r][c].upper()
        if token in ("QU", "ST"):
            current += token
        else:
            current += token

        # Prefix pruning
        if current not in self.prefixes:
            return

        # Valid word check
        if current in self.dictionary and len(current) >= 3:
            if not current.endswith("Q"):  # reject bare "Q"
                self.solutions.add(current.upper())

        # Explore neighbors with backtracking
        visited.add((r, c))
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                self._dfs(r + dr, c + dc, visited, current)
        visited.remove((r, c))
