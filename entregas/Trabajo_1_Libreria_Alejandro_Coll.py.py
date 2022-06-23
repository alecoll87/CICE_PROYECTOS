DB = [{
    "id": "cf_1",
    "title": "El hombre bicentenario",
    "author": "Isaac Asimov",
    "genre": "Ciencia ficción"
},
{
    "id": "ne_1",
    "title": "Lobo de mar",
    "author": "Jack London",
    "genre": "Narrativa extranjera"
},
{
    "id": "np_1",
    "title": "El legado de los huesos",
    "author": "Dolores Redondo",
    "genre": "Narrativa policíaca"
},
{
    "id": "dc_1",
    "title": "El error de Descartes",
    "author": "Antonio Damasio",
    "genre": "Divulgación científica"
},
{
    "id": "dc_2",
    "title": "El ingenio de los pájaros",
    "author": "Jennifer Ackerman",
    "genre": "Divulgación científica"
},
{
    "id": "ne_1",
    "title": "El corazón de las tinieblas",
    "author": "Joseph Conrad",
    "genre": "Narrativa extranjera"
},
{
    "id": "dc_5",
    "title": "Metro 2033",
    "author": "Dmitri Glujovski",
    "genre": "Divulgación científica"
},
{
    "id": "dc_5",
    "title": "Sidharta",
    "author": "Hermann Hesse",
    "genre": "Narrativa extranjera"
},
{
    "id": "el_1",
    "title": "Andres Trapiello",
    "author": "Las armas y las letras",
    "genre": "Narrativa extranjera"
},
{
    "id": "aa_1",
    "title": "El poder del ahora",
    "author": "Ekhart Tolle",
    "genre": "Narrativa extranjera"
},
]

genre = ["Narrativa extranjera", "Divulgación científica", "Narrativa policíaca", "Ciencia ficción", "Autoayuda"]

def menu():
    print("Bienvenido a bookshop")
    print("1. Buscar por ID")
    print("2. Buscar por Autor")
    print("3. Buscar por Título")
    print("4. Buscar por Materia")
    print("5. Eliminar libro por ID")
    print("6. Actualizar libro por ID")
    print("q. para salir")

def get_by_id (book_id):
    for book in DB:
        if book["id"].lower() == book_id:
            return book
    
            
def get_by_param(user_input, book_param):
    result = []
    user_input = user_input.lower()

    for book in DB:
        if book[book_param].lower().find(user_input) >= 0:
            result.append(book)
    
    return result

def pretty_book(book):
    for k,v in book.items():
        print(f"{k}: {v}")


user = None

while user != "q":
    menu()

    user = input("\n: ")

    if user == "1":
        book_id = input("\nid: ").lower()
        book = get_by_id(book_id)
        if book:
            pretty_book(book)
        else:
            print(f" No hemos encontrado el libro por el ID:  {book_id}")
        
        input("\nSiguiente\n")

    elif user == "2":
        book_author = input("\nAuthor: ").lower()
        books = get_by_param(book_author, "author")
        for book in books:
            pretty_book(book)

            input("\nSiguiente\n")
    
    elif user == "3":
        book_title = input("\nTitle: ").lower()
        books = get_by_param(book_title, "title")
        for book in books:
            pretty_book(book)

            input("\nSiguiente\n")
    
    elif user == "4":
    
        for i, genr in enumerate(genre):
            print(f"{i + 1}. {genr}")
        user = int(input(": " )) - 1
        
        books = get_by_param(genre[user], "genre")
        for book in books:
            pretty_book(book) 

            input("\nSiguiente\n")
    
    elif user == "5":
        book_id = input("\nid: ")
        delete_book = get_by_id(book_id)
        if delete_book:
            DB.remove(delete_book)

            print(f"El libro '{delete_book['title']}' se ha eliminado")

            input("\nSiguiente\n")


        else:
            print(f" No hemos encontrado el libro por el ID:  {book_id}")

            input("\nSiguiente\n")

    elif user == "6":
        book_id = input("\nid: ").lower()
        update_book = get_by_id(book_id)

        if update_book:
            print("\n")
            pretty_book(update_book)
            print("\n")
        
        else:
            print(f" No hemos encontrado el libro por el ID:  {book_id}")

        if update_book:
            for k,v in update_book.items():
                new_data = input(f"new {k}: ")
                if new_data:
                    update_book[k] = new_data
            
        
        print (update_book)
        input("\nSiguiente\n")






             

    

        
        