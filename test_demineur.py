import unittest
from demineur import *

class TestGridGenerator(unittest.TestCase):
	def setUp(self):
		# Code to set up test conditions
		self.test_data = [
			["0", "0", "0", "0", "0", "0", "0", "0"],
			["0", "0", "0", "0", "0", "0", "0", "0"]
		]
    
	def tearDown(self):
		# Code to clean up after each test
		self.test_data = None

	def test_grid_length(self): #test if the grid structure is correctly generated
		grid = gridGenerator(8, 2, "0") #first argument is column number, second one is row number and third one is the character to fill the cases
		self.assertEqual(len(grid), len(self.test_data))
		for i in range(len(grid)):
			self.assertEqual(len(grid[i]), len(self.test_data[i]))
	
	def test_grid_length_false(self):
		grid = gridGenerator(2, 8, "0") 
		self.assertEqual(len(grid), len(self.test_data))
		for i in range(len(grid)):
			self.assertEqual(len(grid[i]), len(self.test_data[i]))

	def test_grid_content(self): #test if the grid content is correctly generated
		char_fill = "0"
		grid = gridGenerator(8, 2, char_fill)
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				self.assertEqual(grid[i][j], char_fill)

	def test_grid_content_false(self):
		grid = gridGenerator(8, 2, "-1")
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				self.assertEqual(grid[i][j], "0")

	def test_player_grid_content(self): #test if the player grid content is correctly generated
		char_fill = "-"
		player_grid = gridGenerator(8, 2, char_fill)
		for i in range(len(player_grid)):
			for j in range(len(player_grid[i])):
				self.assertEqual(player_grid[i][j], char_fill)

	def test_player_grid_content_false(self):
		player_grid = gridGenerator(8, 2, "-1")
		for i in range(len(player_grid)):
			for j in range(len(player_grid[i])):
				self.assertEqual(player_grid[i][j], '-')
	


class TestbombPlacement(unittest.TestCase):
	def test_nb_bomb(self): #test if there is the right number of bomb in the grid
		char_fill = "0"
		col = 5
		row = 5
		nb_bomb_to_add = 1
		grid = gridGenerator(col, row, char_fill)
		grid = placeRandomBomb(nb_bomb_to_add, col, row, grid)
		nb_bomb_in_grid = 0
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if (grid[i][j] == "X"):
					nb_bomb_in_grid += 1
		self.assertEqual(nb_bomb_in_grid, nb_bomb_to_add)

	def test_nb_bomb_false(self):
		char_fill = "0"
		col = 5
		row = 5
		nb_bomb_to_add = 1
		grid = gridGenerator(col, row, char_fill)
		grid = placeRandomBomb(nb_bomb_to_add, col, row, grid)
		nb_bomb_in_grid = 0
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if (grid[i][j] == "Z"):
					nb_bomb_in_grid += 1
		self.assertEqual(nb_bomb_in_grid, nb_bomb_to_add)

	def test_player_grid_bomb(self): #checks if there is the right number of bombs in the player grid
		char_fill = "-"
		col = 5
		row = 5
		nb_bomb_to_add = 1
		player_grid = gridGenerator(col, row, char_fill)
		grid = gridGenerator(col, row, "0")
		grid = placeRandomBomb(nb_bomb_to_add, col, row, grid)
		for i in range(len(player_grid)):
			for j in range(len(player_grid[i])):
				player_grid = case(i, j, player_grid, grid)
		nb_bomb_in_grid = 0
		for i in range(len(player_grid)):
			for j in range(len(player_grid[i])):
				if (player_grid[i][j] == "X"):
					nb_bomb_in_grid += 1
		self.assertEqual(nb_bomb_in_grid, nb_bomb_to_add)

	def test_player_grid_bomb_false(self):
		char_fill = "-"
		col = 5
		row = 5
		nb_bomb_to_add = 1
		player_grid = gridGenerator(col, row, char_fill)
		grid = gridGenerator(col, row, "0")
		grid = placeRandomBomb(nb_bomb_to_add, col, row, grid)
		for i in range(len(player_grid)):
			for j in range(len(player_grid[i])):
				player_grid = case(i, j, player_grid, grid)
		nb_bomb_in_grid = 0
		for i in range(len(player_grid)):
			for j in range(len(player_grid[i])):
				if (player_grid[i][j] == "Y"):
					nb_bomb_in_grid += 1
		self.assertEqual(nb_bomb_in_grid, nb_bomb_to_add)

	def test_bomb_right_place(self): #test if the cases in the player grid are the same than in the grid
		char_fill = "-"
		col = 5
		row = 5
		nb_bomb_to_add = 1
		player_grid = gridGenerator(col, row, char_fill)
		grid = gridGenerator(col, row, "0")
		grid = placeRandomBomb(nb_bomb_to_add, col, row, grid)
		for i in range(len(player_grid)):
			for j in range(len(player_grid[i])):
				player_grid = case(i, j, player_grid, grid)
		for i in range(len(player_grid)):
			for j in range(len(player_grid[i])):
				self.assertEqual(player_grid[i][j], grid[i][j])

if __name__ == '__main__':
    unittest.main()