import add_books
import view_all_books
import book_update
import book_lent
import book_remove
import book_return

all_books = []

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Remove Books")
    print("4. Lend Someone a Book")
    print("5. Return Lent Book")
    print("6. Update Book")

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Library Management System ")
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
        all_books = book_return.return_book(all_books)
    elif menu == "6":
        all_books = book_update.book_update(all_books)
    else:
        print("Choose a valid number")
