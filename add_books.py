from save_all_books import save_all_books
import random
from datetime import datetime

def add_books(all_books):
    # Validate title input
    while True:
        title = input("Enter Book Title: ").strip()
        if title:
            break
        else:
            print("Invalid input. Title cannot be empty.")
    
    # Validate author input
    while True:
        author = input("Enter Author Name: ").strip()
        if author:
            break
        else:
            print("Invalid input. Author name cannot be empty.")
    
    # Generate a random ISBN for the book
    isbn = random.randint(1000000000, 9999999999)
    bookAddedDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Validate year input
    while True:
        year_input = input("Enter Publishing Year: ").strip()
        if year_input.isdigit():
            year = int(year_input)
            if 1000 <= year <= datetime.now().year:
                break
            else:
                print(f"Invalid input. Enter a year between 1000 and {datetime.now().year}.")
        else:
            print("Invalid input. Please enter a valid year (e.g., 2021).")
    
    # Validate price input
    while True:
        price_input = input("Enter Book Price: ").strip()
        if price_input.isdigit():
            price = int(price_input)
            if price > 0:
                break
            else:
                print("Invalid input. Price must be greater than 0.")
        else:
            print("Invalid input. Please enter a positive number.")
    
    # Validate quantity input
    while True:
        quantity_input = input("Enter Book Quantity: ").strip()
        if quantity_input.isdigit():
            quantity = int(quantity_input)
            if quantity >= 0:
                break
            else:
                print("Invalid input. Quantity cannot be negative.")
        else:
            print("Invalid input. Please enter a whole number.")
    
    
    # Construct the book dictionary
    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
        "bookAddedDate": bookAddedDate,
        "bookLastUpdatedDate": "",
    }
    
    all_books.append(book)  
    save_all_books(all_books)  
    
    print("Book added successfully!")
    return all_books
