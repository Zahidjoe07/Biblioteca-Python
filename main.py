from libro import Libro
from biblioteca import Biblioteca

biblioteca1 = Biblioteca()

"======================================================="
libro1 = Libro("La Odisea",1,"Homero","Drama",3,10)
libro2 = Libro("Meditaciones",2,"Marco Aurelio", "Filosofía",2,10)
libro3 = Libro("Dinosaurios",3,"Marco Aurelio", "Filosofía",5,10)
# Libro(nombre,nombre_autor,categoria,stock,stock_total)
# Registrar libros dentro de biblioteca
biblioteca1.registrar(libro1)
biblioteca1.registrar(libro2)
biblioteca1.registrar(libro3)
"======================================================="

while True:
    print("========================== BIblioteca ==========================")
    print("""\n1. Registrar libro
2. Mostrar catálogo
3. Consultar libro
4. Editar libro
5. Eliminar libro
6. Prestar libro
7. Devolver libro
8. Salir\n\n
==========================""")
    while True:
        try:
            opcion= int(input("Seleccione una opción: "))
            if 0 < opcion < 9:
                break
            else:
                print("Escoja una opción valida")
        except ValueError as error:
            print(f"ERROR {error}")
    
    # Registrar libro
    if opcion == 1:
        nombre_libro = input("Ingrese el nombre del libro que desea registrar: ")
        nombre_autor = input("Ingrese el nombre del autor del libro: ")
        categoria = input("Ingrese el nombre de la categoria a la que pertenece: ")
        
        while True:
            try:
                stock = int(input("Ingrese el stock que posee el libro en la biblioteca: "))
            except ValueError as error:
                print(f"ERROR {error}\nIngrese el stock de manera valida")
                print("==========================")
            else:
                break
        
        while True:
            try:
                stock_total = int(input("Ingrese el stock total que posee el libro en la biblioteca: "))
            except ValueError as error:
                print(f"ERROR {error}\nIngrese el stock total de manera valida")
                print("==========================")
            else:
                break
        
        nuevo_id = biblioteca1.generar_id()
        while True:
            try:
                libro = Libro(nombre_libro,nuevo_id,nombre_autor,categoria,stock,stock_total)
            except ValueError as error:
                print("==========================")
                print(f"ERROR {error}\nIngrese bien nuevamente el stock y el stock total")
            
                while True:
                    try:
                        print("==========================")
                        stock = int(input("Ingrese el stock que posee el libro en la biblioteca: "))
                        stock_total = int(input("Ingrese el stock total que posee el libro en la biblioteca: "))
                    except ValueError as error:
                        print(f"ERROR {error}\nIngrese el stock y el stock total de manera valida")
                        print("==========================")
                    else:
                        break
            else:
                break
        
        biblioteca1.registrar(libro)
        
    # Mostrar catálogo
    elif opcion == 2:
        biblioteca1.mostrar_catalogo()
    
    # Consultar libro
    elif opcion == 3:
        while True:
            try:
                id_consulta = int(input("Escriba el ID del libro que desea consultar: "))
                biblioteca1.mostrar_info(id_consulta)
            except ValueError as error:
                print(f"ERROR {error}\nIngresa un ID valido")
            except KeyError:
                print("ID inexistente")
            else:
                break
    
    # Editar libro
    elif opcion == 4:
        while True:
            try:
                consulta_editar_libro = int(input("Escriba el ID del libro que desea editar: "))
                biblioteca1.editar_libro(consulta_editar_libro)
            except ValueError as error:
                print(f"ERROR {error}\nIngresa un ID valido")
            except KeyError:
                print("ID inexistente")
            else:
                break
    
    # Eliminar libro
    elif opcion == 5:
        while True:
            try:
                consulta_libro = int(input(f"Escriba el ID del libro que deseas eliminar: "))
                biblioteca1.eliminar_libro(consulta_libro)
            except ValueError as error:
                print(f"ERROR {error}\nIngresa un ID valido")
            except KeyError:
                print("ID inexistente")
            else:
                break
    
    # Prestar libro
    elif opcion == 6:
        while True:
            try:
                consulta_prestamo = int(input("Escriba el ID del libro que deseas prestar: "))
                biblioteca1.prestar_libro(consulta_prestamo)
            except ValueError as error:
                print(f"Error {error}\nIngresa un ID valido")
            except KeyError as error:
                print("ID inexistente")
            else:
                break
    
    # Devolver libro
    elif opcion == 7:
        while True:
            try:
                consulta_devolucion = int(input("Escriba el ID del libro que deseas devolver: "))
                biblioteca1.devolucion_libro(consulta_devolucion)
            except ValueError as error:
                print(f"ERROR {error}\nIngrese un ID valido")
            except KeyError:
                print("ID inexistente")
            else:
                break
    
    # Salir
    elif opcion == 8:
        break