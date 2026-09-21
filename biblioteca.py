class Biblioteca():
    def __init__(self):
        self.catalogo = {}
        self.ultimo_id = 0
    
    def generar_id(self):
        return self.ultimo_id + 1
    
    def registrar(self, libro):
        if libro.id_libro in self.catalogo:
            print("EL ID ya ha sido utilizado")
        else:
            self.catalogo[libro.id_libro] = libro
            self.ultimo_id = libro.id_libro
            print("Registro Exitoso")
        
    def mostrar_info(self, id_libro):
        libro = self.catalogo[id_libro]
        
        print(f"""===================Buscar Libro===================
    Nombre del libro: {libro.nombre}
    ID: {libro.id_libro}
    Autor: {libro.autor}
    Categoria: {libro.categoria}
    Stock: {libro.stock}
    Stock total: {libro.stock_total}
    """)
        print("===========================================")
        return libro
    
    def mostrar_catalogo(self):
        if self.catalogo == {}:
            print("No hay libros registrados")
        
        else:
            for consulta_libro in self.catalogo.values():
                print(f"Nombre del libro: {consulta_libro.nombre}")
                print(f"ID libro: {consulta_libro.id_libro}")
                print(f"Autor: {consulta_libro.autor}")
                print(f"Categoria: {consulta_libro.categoria}")
                print(f"Stock: {consulta_libro.stock}")
                print(f"Stock total: {consulta_libro.stock_total}")
                print("===========================================")
    
    
    def eliminar_libro(self, id_libro):
        if id_libro not in self.catalogo:
            print("No existe el ID del libro dado")
        
        else:
            while True:
                confirmacion = input("¿Seguro que desea eliminar este libro? (si/no): ")
                confirmacion = confirmacion.lower()
                
                if confirmacion == "si":
                    self.catalogo.pop(id_libro)
                    print(f"Libro {id_libro} eliminado")
                    break
                
                elif confirmacion == "no":
                    break
                    
                else:
                    print("Solo se aceptan si o no de respuestas.")
        print("========================")
    
    def editar_libro(self,id_libro):
        mostrar_libro = self.mostrar_info(id_libro)
        while True:
            print("""¿Qué desea modificar?\n
                1. Nombre
                2. Autor
                3. Categoría""")
            print("========================")
            while True:
                try:
                    opcion = int(input("Dato: "))
                except ValueError as error:
                    print(f"ERROR {error} Ingrese uno de los 3 números dados")
                else:
                    if opcion >= 1 and opcion <= 3:
                        break
                    else:
                        print("Ingrese únicamente 1, 2 o 3")
            
            if opcion == 1:
                nuevo_nombre = input("Actualice el nombre del libro: ")
                mostrar_libro.nombre = nuevo_nombre
            
            elif opcion == 2:
                nuevo_autor = input("Actualice el nombre del Autor: ")
                mostrar_libro.autor = nuevo_autor
            
            elif opcion == 3:
                nueva_categoria = input("Actualice la categoria del libro: ")
                mostrar_libro.categoria = nueva_categoria
            
            print("========================")
            
            opcion2 = input("Escribe si, si quieres editar otro dato, caso contrario escribe cualquier cosa: ").lower()
            if opcion2 != "si":
                break
                
        self.mostrar_info(id_libro)
    
    def prestar_libro(self, id_libro):
        self.catalogo[id_libro].prestar()
    
    def devolucion_libro(self,id_libro):
        self.catalogo[id_libro].devolucion()