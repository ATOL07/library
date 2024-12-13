
from save_all_books import save_all_books
from datetime import datetime

def book_update(all_books):
    search_term = input("Enter search term (title, author, or ISBN): ").strip().lower()
    
    found_books = [
        book for book in all_books
        if search_term in book['title'].lower() or
        search_term in book['author'].lower() or
        search_term in str(book['isbn'])
    ]

    if not found_books:
        print(f"No book found matching the term '{search_term}'.")
        return all_books

    if len(found_books) == 1:
        book = found_books[0]
    else:
        print("Multiple books found:")
        for i, book in enumerate(found_books, 1):
            print(f"{i}. Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
        while True:
            try:
                choice = int(input("Select the book to update (number): "))
                if 1 <= choice <= len(found_books):
                    book = found_books[choice - 1]
                    break
                else:
                    print(f"Please enter a valid number between 1 and {len(found_books)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    print(f"Selected Book: {book['title']} by {book['author']} (ISBN: {book['isbn']})")

    # Update book details
    book['title'] = input(f"Enter new title (current: {book['title']}): ") or book['title']
    book['author'] = input(f"Enter new author(s) (current: {book['author']}): ") or book['author']
    book['isbn'] = int(input(f"Enter new ISBN (current: {book['isbn']}): ") or book['isbn'])
    book['year'] = int(input(f"Enter new publishing year (current: {book['year']}): ") or book['year'])
    book['price'] = int(input(f"Enter new price (current: {book['price']}): ") or book['price'])
    book['quantity'] = int(input(f"Enter new quantity (current: {book['quantity']}): ") or book['quantity'])
    book['bookLastUpdatedDate'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    save_all_books(all_books)
    print("Book details updated successfully.")

    return all_books
