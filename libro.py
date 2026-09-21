class Libro():
    def __init__(self,nombre,id_libro,autor,categoria,stock,stock_total):
        
        if stock < 0 or stock > stock_total or stock_total < 1:
            raise ValueError("Stock inválido")
            
        self.__nombre = nombre
        self.__id_libro= id_libro
        self.__autor = autor
        self.__categoria = categoria
        self.__stock = stock
        self.__stock_total = stock_total
    
    @property
    def id_libro(self):
        return self.__id_libro
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, nuevo_autor):
        self.__autor = nuevo_autor
    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, nueva_categoria):
        self.__categoria = nueva_categoria
    
    @property
    def stock(self):
        return self.__stock
    
    @property
    def stock_total(self):
        return self.__stock_total
    
    def prestar(self):
        if self.__stock >= 1:
            self.__stock -= 1
            print(f"Libro prestado.\nQuedan {self.__stock} libros")
        else:
            print(f"El libro {self.__nombre} no esta disponible")
        prestados = self.__stock_total - self.__stock
        print(f"Libros prestados: {prestados}")
        print("===========================")
    
    def devolucion(self):
        if self.__stock_total > self.__stock:
            self.__stock += 1
            print("Su libro ha sido devuelto, gracias")
        else:
            print("Lo siento tenemos el máximo stock de este catalogo")
        print("===========================")