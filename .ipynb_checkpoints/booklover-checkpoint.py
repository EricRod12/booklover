# Import the pandas library
import pandas as pd

# Define the BookLover class
class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        if book_list is None:
            # Initialize an empty DataFrame if book_list is not provided
            self.book_list = pd.DataFrame({'book_name': [], 'book_rating': []})
        else:
            # Use the provided book_list if available
            self.book_list = book_list

    def read_book(self, book_name, book_rating):
        # Add a book to the book_list DataFrame
        self.book_list = self.book_list.append({'book_name': book_name, 'book_rating': book_rating}, ignore_index=True)
        self.num_books += 1

    def add_book(self, book_name, rating):
    # Check if the book already exists in the book list
        if book_name in self.book_list['book_name'].values:
            print("The book '" + book_name + "' already exists in your book list.")
        else:
        # Add the book to the book list using the provided code snippet
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1


    def has_read(self, book_name):
        # Check if the person has read the book (matching on book_name)
        return book_name in self.book_list['book_name'].values

    def num_books_read(self):
        # Return the total number of books the person has read
        return self.num_books

    def fav_books(self):
        # Filter the DataFrame to select the person's favorite books (rating > 3)
        return self.book_list[self.book_list['book_rating'] > 3]

    def __str__(self):
        # Customize the string representation of the object
        return "Name: {}\nEmail: {}\nFavorite Genre: {}\nNumber of Books Read: {}".format(self.name, self.email, self.fav_genre, self.num_books)





