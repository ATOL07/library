import add_books
import view_all_books
import book_update
import book_lent
import book_remove
import book_return
import restore_all_books
import view_all_who_borrowed_books

all_books = []

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Remove Books")
    print("4. Lend Someone a Book")
    print("5. View All Who Borrowed Books")
    print("6. Return Lent Book")
    print("7. Update Book")

    # Restore the books before displaying the menu again
    all_books = restore_all_books.restore_all_books(all_books)

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Library Management System")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        all_books = book_remove.book_remove(all_books)
    elif menu == "4":
        all_books = book_lent.book_lent_to_someone(all_books)
    elif menu == "5":
        # Assuming you want to view all books who borrowed them
        all_books = view_all_who_borrowed_books.view_all_who_borrowed_books(all_books)
    elif menu == "6":
        all_books = book_return.return_book(all_books)  # This should handle the actual return of a lent book
    elif menu == "7":
        all_books = book_update.book_update(all_books)
    else:
        print("Choose a valid number")
