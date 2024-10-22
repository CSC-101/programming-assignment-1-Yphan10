import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_with_vowels(self):
        #Test the vowel_count function with a string containing vowels.
        result = hw1.vowel_count("Hello World")
        self.assertEqual(result, 3)

    def test_vowel_count_no_vowels(self):
        #the vowel_count function with a string containing no vowels.
        result = hw1.vowel_count("bcdfg")
        self.assertEqual(result, 0)

    # Part 2
    def test_short_lists(self):
        #the short_lists function with a list of sublists.
        result = hw1.short_lists([[1, 2], [1], [2, 3, 4], [4, 5]])
        self.assertEqual(result, [[1, 2], [4, 5]])

    # Part 3
    def test_ascending_pairs(self):
        #checks if the function correctly sorts pairs of integers in sublists.
        result = hw1.ascending_pairs([[3,1], [4, 5], [1, 2, 3]])
        self.assertEqual(result, [[1, 3], [4, 5], [1, 2, 3]])

    # Part 4
    def test_add_prices(self):
        #checks if the function correctly adds two prices and handles cents properly.
        p1 = hw1.Price(2, 75)
        p2 = hw1.Price(1, 50)
        result = hw1.add_prices (p1, p2)
        self.assertEqual(result, hw1.Price(4, 25))

    def test_add_prices_no_carry(self):
        p1 = hw1.Price(2, 30)
        p2 = hw1.Price(1, 40)
        result = hw1.add_prices(p1, p2)
        self.assertEqual(result, hw1.Price(3, 70))

    # Part 5
    def test_rectangle_area(self):
        #checks if the function correctly calculates the area of the rectangle.
        rect = hw1.Rectangle(hw1.Point(0, 0), hw1.Point(4, 3))
        result = hw1.rectangle_area(rect)
        self.assertEqual(result, 12)

    # Part 6
    def test_books_by_author(self):
        #Test the books_by_author function with a list of Book objects.
        books = [hw1.Book("Author1", "Title1"), hw1.Book("Author2", "Title2")]
        result = hw1.books_by_author("Author1", books)
        self.assertEqual(result, [hw1.Book("Author1", "Title1")])
    def test_books_by_author_no_match(self):
        books = [hw1.Book("Author", "Title1"), hw1.Book("Author2", "Title2")]
        result = hw1.books_by_author("Author3", books)
        self.assertEqual(result, [])
    # Part 7
    def test_circle_bound(self):
        #  It checks if the function correctly calculates the radius of the bounding circle for the rectangle.
        rect = hw1.Rectangle(hw1.Point(0, 0), hw1.Point(4, 3))
        result = hw1.circle_bound(rect)
        self.assertAlmostEqual(result.radius, 2.5)

    # Part 8
    def test_below_pay_average(self):
        #Test the below_pay_average function with a list of Employee objects.
        employees = [hw1.Employee("Alice", 5000), hw1.Employee("Bob", 60000)]
        result = hw1.below_pay_average(employees)
        self.assertEqual(result, ["Alice"])

if __name__ == '__main__':
    unittest.main()
#4 and 6 dont work!