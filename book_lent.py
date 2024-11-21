from save_all_books import save_all_books

def book_lent_to_someone(library_book):
    try:
        search_term = input("Enter search term (title, author, or ISBN): ").strip().lower()
        
        found_books = [
            book for book in library_book 
            if not book.get('removed', False) and (
                search_term in book['title'].lower() 
                or search_term in book['author'].lower() 
                or search_term in str(book['isbn'])
            )
        ]
        
        if not found_books:
            print(f"No book found matching the term '{search_term}'.")
            return library_book
        
        if len(found_books) == 1:
            book = found_books[0]
            print(f"Found book:\nTitle: {book['title']}\nAuthor: {book['author']}\nISBN: {book['isbn']}\nAvailable quantity: {book['quantity']}")
        else:
            print("Multiple books found:")
            for i, book in enumerate(found_books, 1):
                print(f"{i}. Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
            while True:
                try:
                    choice = int(input("Select the book to lend (number): "))
                    if 1 <= choice <= len(found_books):
                        book = found_books[choice - 1]
                        break
                    else:
                        print(f"Please enter a valid number between 1 and {len(found_books)}.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        borrower_name = input("Enter the name of the borrower: ")
        
        try:
            quantity_to_lend = int(input(f"Enter quantity to lend for '{book['title']}': "))
            if quantity_to_lend <= 0:
                print("Quantity must be a positive integer.")
                return library_book
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            return library_book
        
        book['quantity'] = int(book.get('quantity', 0))
        
        if book['quantity'] >= quantity_to_lend:
            book['quantity'] -= quantity_to_lend
            if 'borrowers' not in book:
                book['borrowers'] = []
            book['borrowers'].append({"name": borrower_name, "quantity": quantity_to_lend})
            save_all_books(library_book)
            print(f"Book '{book['title']}' has been lent out successfully to {borrower_name}. Quantity lent: {quantity_to_lend}.")
        else:
            print(f"Not enough stock for '{book['title']}'. Available quantity: {book['quantity']}.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return library_book
