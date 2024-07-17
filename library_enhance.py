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
    while True:

    
        book_title = input("What is the book title? ")
        author = input("Who is the author? ")
        new_book = (book_title, author)
        print(new_book)

        if new_book in library:
            print("Duplicate. That book is already in the library.")
            break
            
        else:
            library.append(new_book)
            print(f'"{book_title}" by: {author} has been added to the library.')
            add_another_book = input("Would you like to add more books? (yes/no) ")
            if add_another_book == 'yes':
                continue
            elif add_another_book == 'no':
                print(f'Current selections in library: {library}')
                break
            else:
                print('Please answer with yes or no.')
        
        
           

add_book()


    




