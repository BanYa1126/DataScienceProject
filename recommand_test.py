import csv
import random

def random_books(category):
    with open("book_info.csv", 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        header = next(reader)

        books = list(reader)
        random.shuffle(books)

        ran_book_rec=[]
        for book in books:
            if book[2] == category:
                if len(ran_book_rec) < 5:
                    ran_book_rec.append(book[0])
                if len(ran_book_rec) == 5:
                    break

    return ran_book_rec