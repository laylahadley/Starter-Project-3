import unittest
from boggle_solver import Boggle


class TestBoggle_BlackBox(unittest.TestCase):

    def test_empty_grid(self):
        grid = [[]]
        dictionary = ["HELLO", "WORLD"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])

    def test_empty_dictionary(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = []
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])

    def test_1x1_no_word(self):
        grid = [["A"]]
        dictionary = ["A"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])

    def test_1x1_too_long(self):
        grid = [["A"]]
        dictionary = ["APPLE"]
        game = Boggle(grid, dictionary)
        self.assertEqual(game.getSolution(), [])

    def test_qu_tile(self):
        grid = [["Qu", "A"], ["B", "C"]]
        dictionary = ["qua", "queen"]
        game = Boggle(grid, dictionary)
        sol = [w.lower() for w in game.getSolution()]
        self.assertIn("qua", sol)

    def test_diagonal_word(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["acd"]  # diagonal
        game = Boggle(grid, dictionary)
        sol = [w.lower() for w in game.getSolution()]
        self.assertIn(sol, [["acd"], []])

    def test_repeated_tile_invalid(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["aa"]
        game = Boggle(grid, dictionary)
        self.assertNotIn("AA", game.getSolution())

    def test_word_longer_than_path(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = ["abcdx"]
        game = Boggle(grid, dictionary)
        self.assertNotIn("ABCDX", game.getSolution())

    def test_large_grid_scalability(self):
        grid = [["A"] * 6 for _ in range(6)]
        dictionary = ["AAAAAA"]
        game = Boggle(grid, dictionary)
        self.assertIn("AAAAAA", game.getSolution())

    def test_normal_case(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "cfi", "abdhi", "xyz"]
        game = Boggle(grid, dictionary)
        sol = [w.lower() for w in game.getSolution()]
        self.assertIn("abc", sol)
        self.assertNotIn("xyz", sol)


if __name__ == "__main__":
    unittest.main()
