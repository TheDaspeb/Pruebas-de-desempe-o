from servicios1 import*


# -------------------------------------------------------
# Mail Menu
# -------------------------------------------------------

def menu():
    #Main manu of the program
    while True:
        print("""
======== SISTEMA DE LIBRERÍA ========
1. Ver productos
2. Registrar producto
3. Actualizar producto
4. Eliminar producto
5. Registrar venta
6. Top 3 productos
7. Ventas por autor
8. Reporte de ingresos
9. Salir
""")

        option = input("Elige una opción: ")

        if option == "1":
            see_book()
        elif option == "2":
            add_book()
        elif option == "3":
            update_book()
        elif option == "4":
            delete_book()
        elif option == "5":
            register_sale()
        elif option == "6":
            top_3()
        elif option == "7":
            sales_by_author()
        elif option == "8":
            income_report()
        elif option == "9":
            print("Adiós.")
            break
        else:
            print("Opción inválida.")


# Start menú
menu()



