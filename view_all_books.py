import json
from tabulate import tabulate

def view_all_books(all_books):
    with open("all_books.json", "r") as fp:
        all_books = json.load(fp)

    if all_books:
        headers = ["Title", "Author", "ISBN", "Year", "Price", "Quantity", "Book Added Date", "Book Last Updated Date"]
        table = []
        for book in all_books:
            table.append([
                book['title'], book['author'], book['isbn'], book['year'], book['price'],
                book['quantity'], book['bookAddedDate'], book['bookLastUpdatedDate']
            ])

        print(tabulate(table, headers, tablefmt="fancy_grid"))
    else:
        print("No books found in the program")
