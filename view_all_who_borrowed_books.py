import json
from tabulate import tabulate

def view_all_who_borrowed_books(all_books):
    # Read books data from the JSON file
    try:
        with open("all_books.json", "r") as fp:
            library_book = json.load(fp)
    except FileNotFoundError:
        print("Error: The 'all_books.json' file does not exist.")
        return library_book

    borrowed_books = []

    # Collect borrowed book details
    if all_books:
        for book in all_books:
            if 'borrowers' in book and book['borrowers']:  # Only consider books with borrowers
                for borrower in book['borrowers']:
                    # Use .get() to safely access borrower details
                    phone_number = borrower.get('phone', 'N/A')  # Default to 'N/A' if phone is missing
                    borrowed_books.append([
                        book['title'],
                        borrower.get('name', 'Unknown'),  # Default to 'Unknown' if name is missing
                        phone_number,
                        borrower.get('quantity', 0),  # Default to 0 if quantity is missing
                        borrower.get('return_due_date', 'N/A')  # Default to 'N/A' if due date is missing
                    ])
    
    if borrowed_books:
        headers = ["Book Title", "Borrower's Name", "Phone Number", "Quantity Lent", "Return Due Date"]
        print(tabulate(borrowed_books, headers, tablefmt="fancy_grid"))
    else:
        print("No books have been borrowed yet.")
    
    return library_book
