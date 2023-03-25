# Book Manager
This Python script manages book details by providing functionality to add, update, delete, and list book titles. Book details are stored in a JSON file named books.json. The script uses a Book class with an __`__init__`__ method to create a new book object. The book object contains __`id`, `title`, `author`, `publisher`,__ and __`year`__ details.

## Requirements
This script requires `Python 3.x` and the `json` module, which is included with Python.

## How to use
1. Clone or download the script to your local system.
2. Open the command prompt and navigate to the directory containing the script.
3. Run the script using the following command:
```python book_manager.py```
4. Follow the on-screen instructions to perform the desired operation:
### Add a new book
This operation allows you to add a new book to the book manager. You will be prompted to enter the book's __`id`, `title`, `author`, `publisher`,__ and __`year`__ details.

### List all book titles
This operation allows you to list all the book titles available in the book manager. The titles are listed in pages of 10 books per page.

### Update an existing book
This operation allows you to update the details of an existing book in the book manager. You will be prompted to enter the __`id`__ of the book to be updated, and then the new __`title`, `author`, `publisher`,__ and __`year`__ details.

### Delete an existing book
This operation allows you to delete an existing book from the book manager. You will be prompted to enter the __`id`__ of the book to be deleted.

### Data storage
The book details are stored in a JSON file named __`books.json`__ in the following format:
```
{
    "books_details": [
        {
            "id": "1",
            "title": "Book Title",
            "author": "Author Name",
            "publisher": "Publisher Name",
            "year": 2022
        },
        {
            "id": "2",
            "title": "Another Book Title",
            "author": "Another Author Name",
            "publisher": "Another Publisher Name",
            "year": 2021
        }
    ]
}
```
Each book detail is represented by a dictionary with keys __`id`, `title`, `author`, `publisher`,__ and __`year`__. The __`books_details`__ key contains a list of all the books in the book manager.
