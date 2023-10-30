import unittest
import sys

# Add the directory containing booklover.py to the sys.path
sys.path.append('Documents/MSDS/DS5100/DS-5100-141654114/m08')

from booklover import BookLover

# Your test cases go here
# ...

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        lover = BookLover('Alice', 'alice@example.com', 'Mystery')
        lover.add_book('Book A', 4)
        self.assertTrue('Book A' in lover.book_list['book_name'].values)


    def test_2_add_book(self):
        lover = BookLover('Bob', 'bob@example.com', 'Fantasy')
        lover.add_book('Book B', 3)
        lover.add_book('Book B', 5)
        self.assertEqual(len(lover.book_list[lover.book_list['book_name'] == 'Book B']), 1)


    def test_3_has_read(self):
        lover = BookLover('Charlie', 'charlie@example.com', 'Science Fiction')
        lover.add_book('Book C', 4)
        self.assertTrue(lover.has_read('Book C'))

    def test_4_has_read(self):
        lover = BookLover('David', 'david@example.com', 'Romance')
        self.assertFalse(lover.has_read('Book D'))

    def test_5_num_books_read(self):
        lover = BookLover('Eve', 'eve@example.com', 'Thriller')
        lover.add_book('Book E1', 4)
        lover.add_book('Book E2', 3)
        lover.add_book('Book E3', 5)
        self.assertEqual(lover.num_books_read(), 3)

    def test_6_fav_books(self):
        lover = BookLover('Frank', 'frank@example.com', 'Non-Fiction')
        lover.add_book('Book F1', 2)
        lover.add_book('Book F2', 4)
        lover.add_book('Book F3', 5)
        lover.add_book('Book F4', 3)
        fav_books = lover.fav_books()
        self.assertTrue(all(book_rating > 3 for book_rating in lover.fav_books()['book_rating']))


if __name__ == '__main__':
    unittest.main(verbosity=3)

