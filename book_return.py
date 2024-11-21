from save_all_books import save_all_books

def return_book(library_book):
    try:
        search_term = input("Enter search term (title, author, or ISBN): ").strip().lower()
        if not search_term:
            print("Search term cannot be empty.")
            return library_book

        found_books = [
            book for book in library_book
            if not book.get('removed', False) and (
                search_term in book['title'].lower() or
                search_term in book['author'].lower() or
                search_term in str(book['isbn'])
            )
        ]

        if not found_books:
            print(f"No book found matching the term '{search_term}'.")
            return library_book

        if len(found_books) == 1:
            book = found_books[0]
        else:
            print("Multiple books found:")
            for i, book in enumerate(found_books, 1):
                print(f"{i}. Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
            while True:
                try:
                    choice = int(input("Select the book to return (number): "))
                    if 1 <= choice <= len(found_books):
                        book = found_books[choice - 1]
                        break
                    else:
                        print(f"Please enter a valid number between 1 and {len(found_books)}.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        print(f"Selected Book: {book['title']} by {book['author']} (ISBN: {book['isbn']})")
        
        if 'borrowers' not in book or not book['borrowers']:
            print(f"No borrowers found for the book '{book['title']}'.")
            return library_book

        print("Borrowers:")
        for i, borrower in enumerate(book['borrowers'], 1):
            print(f"{i}. {borrower['name']}")

        while True:
            try:
                borrower_choice = int(input("Select the borrower (number): "))
                if 1 <= borrower_choice <= len(book['borrowers']):
                    borrower_record = book['borrowers'][borrower_choice - 1]
                    break
                else:
                    print(f"Please enter a valid number between 1 and {len(book['borrowers'])}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            try:
                quantity_to_return = int(input(f"Enter quantity to return for '{book['title']}': "))
                borrowed_quantity = borrower_record.get('quantity', 1)
                if 0 < quantity_to_return <= borrowed_quantity:
                    break
                else:
                    print(f"Please enter a valid quantity between 1 and {borrowed_quantity}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        book['quantity'] += quantity_to_return

        if quantity_to_return == borrower_record.get('quantity', 1):
            book['borrowers'].remove(borrower_record)
            print(f"All books returned by '{borrower_record['name']}'. Borrower removed from the record.")
        else:
            borrower_record['quantity'] -= quantity_to_return
            print(f"Book '{book['title']}' returned successfully. Quantity returned: {quantity_to_return}.")

        save_all_books(library_book)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return library_book
