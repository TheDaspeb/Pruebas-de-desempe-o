import datetime #This is for recording sales


#===================
#Initial inventory with 5 products (required)
#====================

# the list "library" load dictionary, each dictionary is a book
library = [    
    {"id": "001", "title": "Harry Potter y la piedra filosofal", "author": "J. K. Rowing", "category": "Fantasy", "price": 25.0, "stock": 20},
    {"id": "002", "title": "Angel de la guarda", "author": "Fleur Jaeggy", "category": "childish", "price": 12.0, "stock": 10},
    {"id": "003", "title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy", "price": 22.0, "stock": 15},
    {"id": "004", "title": "It", "author": "Stephen King", "category": "Horror", "price": 20.0, "stock": 8},
    {"id": "005", "title": "the fifty shades of gray", "author": "E. L James", "category": "erotic", "price": 26.0, "stock": 30}

] #This is where the books are stored

sales = [] #This is sales will be stored


#Rigth now, I going yo create the functions

""" Inventary Function """


#===================
#The functions Add 
#===================

def see_book(): #show the book
    if not library:
        print('No hay libros en la biblioteca')
        return
    
    for l in library:
        print(f"{l['id']} | {l['title']} | {l['author']} | {l['category']} | ${l['price']} | Stock: {l['stock']}")

def add_book(): #add the new book

    print('======== Agregar un libro ==========\n')

    lid = input("ID del producto: ").strip()

    #validate existing ID
    for p in library:
        if p["id"] == lid:
            print("El ID ya existe.")
            return

    title = input('\nIngrese el Nombre del libro para agregar: ')
    author = input('\nIngresa el nombre del autor del libro: ')
    category = input('\nIngresa la categoría del libro: ')
    try:
        price = float(input('\nIngresa el precio del libro: '))
        stock = int(input('\nIngrese el número de libros que hay: '))
        if price < 0 and stock < 0:
            print('\nEl precio y la cantidad deben ser positivos')
            return

    except ValueError:
        print('\nIngrese número numéricos.')
        return
    
        
    books = {
        'id': lid,
        'title': title,
        'author': author,
        'category': category,
        'price': price,
        'stock': stock
        }
    library.append(books)
    print(f'El libro {title} se agregó correctamente.')

def update_book(): # update existing books
    
    print('\n----- Actualizar datos de los  libros ------')
    lid = input("Ingresa el ID del producto: ")

    for p in library:
        if p['id'] == lid:
            print('\nSi dejas un espacio vacio no se modifca')

            new_title = input(f"Nuevo título ({p['title']}): ")
            new_author = input(f'Nuevo autor ({p['author']})')
            new_category = input(f'Nueva categoria ({p['category']})')
            new_price = float(input(f'Nuevo precio ({p['price']})'))
            new_stock = int(input(f'Nueva cantidad ({p['stock']})'))
            
            #update only if you write something
            if new_title: p["title"] = new_title
            if new_author: p["author"] = new_author
            if new_category: p["category"] = new_category
            if new_price: p["price"] = float(new_price)
            if new_stock: p["stock"] = int(new_stock)

            print('\nLibro actualizado.')
            return
    print('\nlibro no encontrado')

def delete_book():
        #delate of books
    print("\n--- ELIMINAR PRODUCTO ---")
    lid = input("ID del producto: ")

    for p in library:
        if p["id"] == lid:
            library.remove(p)
            print("\nProducto eliminado.")
            return

    print("\nProducto no encontrado.")


#=======================
#       Sales functions
#=======================

def register_sale():
    
    print("\n--- REGISTRAR VENTA ---")
    lid = input("ID del producto vendido: ")

    product = None
    for p in library:
        if p["id"] == lid:
            product = p
            break

    if product is None:
        print("\nProducto no encontrado.")
        return

    try:
        client = input("Nombre del cliente: ").strip()
        quantity = int(input("Cantidad vendida: "))#cantidad
        discount = float(input("Descuento (0 si no hay): "))

        if quantity <= 0 or discount < 0:
            print("Valores inválidos.")
            return

        if product["stock"] < quantity:
            print("Stock insuficiente.")
            return

    except:
        print("Error: valores numéricos inválidos.")
        return

    # Discount stock
    product["stock"] -= quantity

    # Regist the sale in "sales"
    sale = {
        "client": client,
        "product": product["title"],
        "author": product["author"],
        "quantity": quantity,
        "price": product["price"],
        "discount": discount,
        "date": datetime.date.today().isoformat()
    }

    sales.append(sale)
    print("Venta registrada correctamente.")

#=================
#     Repots
#=================

def top_3():
    print('\nTop 3 de los libros más vendidos. ')

    if not sales:
        print('Aún no haz registrado alguna venta')
        return
    
    counts = {} #dictionary for count sales for title

    for b in sales:
        book = b["product"]
        counts [book] = counts.get(book, 0) + b["quantity"]

    #Sort by quantity sold (highest to lowest)
    sorted_books = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    for title, qty in sorted_books[:3]:
        print(f"{title}: {qty} vendidos")


def sales_by_author():
    
    print("\n--- VENTAS AGRUPADAS POR AUTOR ---")

    if not sales:
        print("Aún no hay ventas.")
        return

    totals = {}

    for b in sales:
        author = b["author"]
        amount = b["quantity"] * b["price"]
        totals[author] = totals.get(author, 0) + amount

    for author, total in totals.items():
        print(f"{author}: ${total}")


def income_report():
    """Calcula ingreso bruto y neto."""
    print("\n--- REPORTE DE INGRESOS ---")

    gross = sum(s["quantity"] * s["price"] for s in sales)
    net = sum((s["quantity"] * s["price"]) - s["discount"] for s in sales)

    print(f"Ingreso bruto: ${gross}")
    print(f"Ingreso neto: ${net}")

