import unittest
from Grocery_Manager_App_Functions import *

class TestGroceryManagerAppFunctions(unittest.TestCase):
	def test_that_add_item_adds_and_stores_book(self):
		actual = add_item("Emmax")
		expected = "Item added successfully"
		self.assertEqual(actual,expected)
	def test_that_add_item_returns_type_error(self):
		actual = 1
		self.assertRaises(TypeError,add_item,actual)
	def test_that_add_item_ignore_case(self):
		
		self.assertEqual(actual,expected)
				