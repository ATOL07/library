
from save_all_books import save_all_books
from datetime import datetime, timedelta
import json

def book_lent_to_someone(all_books):
    try:
        search_term = input("Enter search term (title, author, or ISBN): ").strip().lower()

        found_books = [
            book for book in all_books
            if not book.get('removed', False) and (
                search_term in book['title'].lower()
                or search_term in book['author'].lower()
                or search_term in str(book['isbn'])
            )
        ]

        if not found_books:
            print(f"No book found matching the term '{search_term}'.")
            return all_books

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

        if book['quantity'] == 0:
            print("Not enough books are available to lend.")
            return all_books

        borrower_name = input("Enter the name of the borrower: ")
        borrower_phone = input("Enter the phone number of the borrower: ")

        while True:
            try:
                quantity_to_lend = int(input(f"Enter quantity to lend for '{book['title']}': "))
                if quantity_to_lend <= 0:
                    print("Quantity must be a positive integer.")
                    continue
                if quantity_to_lend > book['quantity']:
                    print(f"Not enough books are available to lend. Available quantity: {book['quantity']}")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        return_due_date = datetime.now() + timedelta(days=14)  # Example: set due date to 14 days from now

        # Update book quantity
        book['quantity'] -= quantity_to_lend
        if 'borrowers' not in book:
            book['borrowers'] = []

        # Record borrower details
        book['borrowers'].append({
            "name": borrower_name,
            "phone": borrower_phone,
            "quantity": quantity_to_lend,
            "return_due_date": return_due_date.strftime('%Y-%m-%d %H:%M:%S'),
            "book_title": book['title']
        })

        # Save updated book details
        save_all_books(all_books)

        # Success message
        print(f"Book '{book['title']}' has been lent out successfully to {borrower_name}.")
        print(f"Phone Number: {borrower_phone}")
        print(f"Quantity lent: {quantity_to_lend}. Return due date: {return_due_date.strftime('%Y-%m-%d %H:%M:%S')}.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return all_books

