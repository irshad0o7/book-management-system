import json

class Book:
    def __init__(self, id, title, author, publisher, year):
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

# Get the ID list from books details
def getAllIdList(filename):
    # List of IDs
    idList = list()

    with open(filename, 'r') as file:
        # Load existing data into a dictonary.
        books = json.load(file)

    # Iterate in books details to get book IDs and push them in idList.
    for book in books['books_details']:
        idList.append(book['id'])

    return idList

# Add a new book details.
def addNewBookDetails():
    id = input('Enter the id of the book: ')
    title = input('Enter the title of the book: ')
    author = input('Enter the name of the author: ')
    publisher = input('Enter the name of the publisher: ')
    try:
        year = int(input('Enter the year of publication: '))
    except:
        print()
        print('Failed to add book details')
        print('Year should be an integer value')
        print('Please try again')
        print()
        return

    # Object of class Book
    book = Book(id, title, author, publisher, year)

    with open('books.json','r+') as file:
        # Load existing data into a dictonary.
        books = json.load(file)
        # Add new book data to existing books data.
        books['books_details'].append(book.__dict__)
        # Clears the json file
        file.truncate(0)
        # Sets file's current position at the beginning of the file.
        file.seek(0)
        # Convert and write back to json.
        json.dump(books, file, indent = 4)
    
    print()
    print(f'Book with ID "{id}" is added successfully !')
    print()

# Listing title of all the books.
def listTitleOfAllBooks():
    with open('books.json', 'r') as file:
        # Load existing data into a dictonary.
        books = json.load(file)
    
    # Count of books to be displayed.
    noOfBooks = len(books['books_details'])

    # Page number for pagination.
    page = 1

    print("Number of book titles found: ", noOfBooks)
    print()
        
    while True:
        startIndex = (page - 1) * 10
        endIndex = startIndex + 10
        noOfBooks -= 10

        # Iterate in titles list to display title of books as per pagination.
        for book in books['books_details'][startIndex:endIndex]:
            print(book['title'])

        if noOfBooks >= 0:
            print()
            # If next page exists, trigger it once pressed 'n'
            nextPage = input("Press 'n' for next page or any key to quit: ")
            print()

            if nextPage == 'n': page += 1
            else: break
        else: break

# Update an existing book details
def updateExistingBookDetails():
    existingId = input("Enter the ID of book that you want to update: ")

    IdsList = getAllIdList('books.json')

    if existingId in IdsList:
        updatedTitle = input("Enter the title of the book to update: ")
        updatedAuthor = input("Enter the name of the author to update: ")
        updatedPublisher = input("Enter the name of the publisher to update: ")
        try:
            updatedYear = int(input("Enter the year of publication to update: "))
        except:
            print()
            print('Failed to update book details')
            print('Year should be an integer value')
            print('Please try again')
            print()
            return

        with open('books.json', 'r+') as file:
            # Load existing data into a dictonary.
            books = json.load(file)

            # Object of class Book
            updatedBook = Book(existingId, updatedTitle, updatedAuthor, updatedPublisher, updatedYear)

            # Iterate in books details to update a particular book details.
            for i in range(len(books['books_details'])):
                if books['books_details'][i]['id'] == existingId:
                    books['books_details'][i] = updatedBook.__dict__
                    break

            # Clears the json file
            file.truncate(0) 
            # Sets file's current position at the beginning of the file.
            file.seek(0)
            # Convert and write back to json.
            json.dump(books, file, indent = 4)

        print()
        print(f'Book details for ID "{existingId}" is updated successfully !')
        print()
    else:
        print()
        print(f'Entered ID "{existingId}" does not exists !')
        print()

# Delete an existing book details
def deleteExistingBookDetails():
    existingId = input("Enter the ID of book that you want to update: ")

    IdsList = getAllIdList('books.json')

    if existingId in IdsList:
        with open('books.json', 'r+') as file:
            # Load existing data into a dictonary.
            books = json.load(file)

            # Iterate in books details to delete a book.
            for book in books['books_details']:
                if book['id'] == existingId:
                    books['books_details'].remove(book)
                    break
            
            # Clears the json file
            file.truncate(0)
            # Sets file's current position at the beginning of the file.
            file.seek(0)
            # Convert and write back to json.
            json.dump(books, file, indent = 4)

        print()
        print(f'Book with ID "{existingId}" is deleted successfully !')
        print()
    else:
        print()
        print(f'Entered ID "{existingId}" does not exists !')
        print()

# Listing authors.
def listAllAuthors():
    # Set of authors to get unique author name.
    authors = set()

    with open('books.json', 'r') as file:
        # Load existing data into a dictonary.
        books = json.load(file)

    # Iterate in books details to get author names.
    for book in books['books_details']:
        authors.add(book['author'])

    print("Number of authors found: ", len(authors))
    print()

    # Iterate in set of authors to display author names.
    for author in authors:
        print(author)
    print()

# Map choice to it's functionality.
switcher = {
    1: addNewBookDetails,
    2: listTitleOfAllBooks,
    3: updateExistingBookDetails,
    4: deleteExistingBookDetails,
    5: listAllAuthors,
}

while True:
    # Displays Menu
    print("*************************MENU*************************")
    print()
    print("Choose any of the following operations:")
    print("1. Add a new book details")
    print("2. List title of all the books")
    print("3. Update an existing book details")
    print("4. Delete an existing book")
    print("5. List all the authors")
    print('6. Quit')
    print()
    print("******************************************************")
    print()

    # Gets choice based on menu
    choice = int(input('Enter your choice: '))

    # Quit the app
    if choice == 6: break

    # Get function definition based on choice.
    executeSelectedChoice = switcher.get(choice)

    print()
    print("******************************************************")
    print()

    # Executes the desired function based on choice.
    try:
        executeSelectedChoice()
    except:
        print('Invalid choice !')
        print('Please try again')
        print()
