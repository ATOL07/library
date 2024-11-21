from save_all_books import save_all_books

def book_remove(all_books):
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
        choice = int(input("Select the book to remove (number): "))
        book = found_books[choice - 1]

    all_books.remove(book)
    save_all_books(all_books)
    print(f"Book '{book['title']}' removed successfully.")

    return all_books
