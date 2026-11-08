"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

from math import sqrt

import data
import hw1


class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        self.assertEqual(hw1.vowel_count("HEllo WOrld"), 3)

    def test_vowel_count_empty_string(self):
        self.assertEqual(hw1.vowel_count(""), 0)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        self.assertEqual(hw1.short_lists([[1, 2], [3, 4], [5, 6, 7]]), [[1, 2], [3, 4]])

    def test_short_lists_no_matching_lengths(self):
        self.assertEqual(hw1.short_lists([[1], [2, 3, 4], [5, 6, 7, 8]]), [])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        self.assertEqual(hw1.ascending_pairs([[2, 1], [4, 3]]), [[1, 2], [3, 4]])

    def test_ascending_pairs_other_lengths_unchanged(self):
        self.assertEqual(hw1.ascending_pairs([[1, 2, 3], [5, 4, 6]]), [[1, 2, 3], [5, 4, 6]])

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        self.assertEqual(hw1.add_prices(data.Price(1, 50), data.Price(2, 25)), data.Price(3, 75))

    def test_add_prices_with_cents_carry(self):
        self.assertEqual(hw1.add_prices(data.Price(1, 75), data.Price(2, 50)), data.Price(4, 25))

    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(0, 0), data.Point(2, 3))), 6)

    def test_rectangle_area_negative_coordinates(self):
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(-1, -1), data.Point(1, 1))), 4)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        book1 = data.Book(["John"], "a book")
        book2 = data.Book(["John"], "another book")
        self.assertEqual(hw1.books_by_author("John", [book1, book2]), [book1, book2])

    def test_books_by_author_no_matches(self):
        book1 = data.Book(["John", "Jane"], "a book")
        book2 = data.Book(["Doe"], "another book")
        self.assertEqual(hw1.books_by_author("Gary", [book1, book2]), [])

    # Part 7: circle_bound
    def test_circle_bound_square(self):
        square = data.Rectangle(data.Point(0, 0), data.Point(2, 2))
        circle = data.Circle(data.Point(1, 1), sqrt(8) / 2)
        self.assertEqual(hw1.circle_bound(square), circle)

    def test_circle_bound_non_square_rectangle(self):
        rectangle = data.Rectangle(data.Point(0, 0), data.Point(2, 4))
        circle = data.Circle(data.Point(1, 2), sqrt(20) / 2)
        self.assertEqual(hw1.circle_bound(rectangle), circle)

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        employees = [
            data.Employee("John", 10),
            data.Employee("Jane", 20),
            data.Employee("Doe", 45)
        ]

        self.assertEqual(hw1.below_pay_average(employees), ["John", "Jane"])

    def test_below_pay_average_empty_list(self):
        employees = []
        self.assertEqual(hw1.below_pay_average(employees), [])


if __name__ == '__main__':
    unittest.main()
