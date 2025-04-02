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

	def test_grid_length(self):
		grid = gridGenerator(8, 2, "0") #first argument is column number, second one is row number and third one is the character to fill the cases
		self.assertEqual(len(grid), len(self.test_data))
		for i in range(len(grid)):
			self.assertEqual(len(grid[i]), len(self.test_data[i]))
	
	def test_grid_length_false(self):
		grid = gridGenerator(2, 8, "0") 
		self.assertEqual(len(grid), len(self.test_data))
		for i in range(len(grid)):
			self.assertEqual(len(grid[i]), len(self.test_data[i]))

	def test_grid_content(self):
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

	def test_player_grid_content(self):
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
	

if __name__ == '__main__':
    unittest.main()