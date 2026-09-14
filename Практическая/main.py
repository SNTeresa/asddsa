from storage import load_books, save_books, add_book, remove_book

def main():
    books = load_books()
    books = add_book(books, "Капитанская дочка", "Пушкин")
    books = add_book(books, "Евгений Онегин", "Пушкин")
    books = add_book(books, "Анна Каренина", "Толстой")
    books = remove_book(books, "Война и мир")
    print("Текущий список в памяти:", books)

if __name__ == "__main__":
    main()
