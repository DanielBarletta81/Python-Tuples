#2. Python Data Structure Challenges in Real-World Scenarios

#Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.


#Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. 
# Your task is to update this system by adding new books and ensuring no duplicates.

#Existing Library Data:

#library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
#- Add functionality to insert new books into `library`. 
# Ensure that adding a duplicate book is handled appropriately.


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book():
    book_title = input("What is the book title? ")
    author = input("Who is the author? ")
    for i in enumerate(library):

        if book_title in library[i]:
            print("Duplicate. That book is already in the library.")
        else:
            library.append((book_title, author))
            print(f'"{book_title}" by: {author} has been added to the library.')
            print(library)

add_book()

    




