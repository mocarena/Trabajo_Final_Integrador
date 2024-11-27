import sqlite3
import sys
from colorama import Fore, Style

# Función para conectar a la base de datos
def conectar_base_datos():
    try:
        # Establecer la conexión con la base de datos SQLite
        conexion = sqlite3.connect(r'C:\Users\monic\Documents\PYTHON FS\CURSO PYTHON INICIAL\Trabajo_Final_Integrador\inventario.db')
        print(Fore.GREEN + "Conexión exitosa a la base de datos." + Style.RESET_ALL)
        return conexion
    except sqlite3.Error as err:
        # Manejo de error si la conexión falla
        print(Fore.RED + f"Error al conectar a la base de datos: {err}" + Style.RESET_ALL)
        return None

# Función para registrar un producto en la base de datos
def registrar_producto(conexion):
    # Solicitar información del producto
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    categoria = input("Categoría: ")

    cursor = conexion.cursor()
    # Preparar la consulta SQL para insertar el nuevo producto
    query = "INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)"
    valores = (nombre, descripcion, cantidad, precio, categoria)
    # Ejecutar la consulta
    cursor.execute(query, valores)
    conexion.commit()
    print(Fore.GREEN + "Producto registrado con éxito." + Style.RESET_ALL)

# Función para mostrar todos los productos en el inventario
def mostrar_productos(conexion):
    cursor = conexion.cursor()
    # Ejecutar la consulta SQL para obtener todos los productos
    cursor.execute("SELECT * FROM productos")
    resultados = cursor.fetchall()

    print(Fore.CYAN + "\nProductos en el inventario:" + Style.RESET_ALL)
    # Mostrar los resultados obtenidos
    for producto in resultados:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")

# Función para actualizar la cantidad de un producto
def actualizar_producto(conexion):
    # Solicitar ID del producto y nueva cantidad
    producto_id = int(input("ID del producto a actualizar: "))
    nueva_cantidad = int(input("Nueva cantidad: "))

    cursor = conexion.cursor()
    # Preparar la consulta SQL para actualizar la cantidad
    query = "UPDATE productos SET cantidad = ? WHERE id = ?"
    valores = (nueva_cantidad, producto_id)
    # Ejecutar la consulta
    cursor.execute(query, valores)
    conexion.commit()
    if cursor.rowcount > 0:
        print(Fore.GREEN + "Producto actualizado con éxito." + Style.RESET_ALL)
    else:
        print(Fore.RED + "No se encontró un producto con ese ID." + Style.RESET_ALL)

# Función para eliminar un producto
def eliminar_producto(conexion):
    # Solicitar ID del producto a eliminar
    producto_id = int(input("ID del producto a eliminar: "))

    cursor = conexion.cursor()
    # Preparar la consulta SQL para eliminar el producto
    query = "DELETE FROM productos WHERE id = ?"
    cursor.execute(query, (producto_id,))
    conexion.commit()
    if cursor.rowcount > 0:
        print(Fore.GREEN + "Producto eliminado con éxito." + Style.RESET_ALL)
    else:
        print(Fore.RED + "No se encontró un producto con ese ID." + Style.RESET_ALL)

# Función para buscar un producto por nombre o categoría
def buscar_producto(conexion):
    # Solicitar criterio de búsqueda y valor correspondiente
    criterio = input("Buscar por (nombre/categoria): ").lower()
    valor = input(f"Ingrese el {criterio}: ")

    cursor = conexion.cursor()
    # Preparar la consulta SQL para buscar productos que coincidan con el criterio
    query = f"SELECT * FROM productos WHERE {criterio} LIKE ?"
    cursor.execute(query, (f"%{valor}%",))
    resultados = cursor.fetchall()

    print(Fore.CYAN + "\nResultados de la búsqueda:" + Style.RESET_ALL)
    # Mostrar los resultados obtenidos
    for producto in resultados:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")

# Función para generar un reporte de productos con bajo stock
def reporte_bajo_stock(conexion):
    # Solicitar el límite de stock para filtrar productos
    limite = int(input("Ingrese el límite de stock: "))

    cursor = conexion.cursor()
    # Ejecutar la consulta SQL para obtener productos con cantidad menor o igual al límite
    query = "SELECT * FROM productos WHERE cantidad <= ?"
    cursor.execute(query, (limite,))
    resultados = cursor.fetchall()

    print(Fore.YELLOW + "\nProductos con bajo stock:" + Style.RESET_ALL)
    # Mostrar los productos con bajo stock
    for producto in resultados:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[3]}")

# Función para mostrar el menú principal y gestionar las opciones seleccionadas por el usuario
def menu_principal():
    # Conectar a la base de datos
    conexion = conectar_base_datos()

    # Si no se puede conectar a la base de datos, se cierra el programa
    if not conexion:
        print(Fore.RED + "No se pudo conectar a la base de datos. Cerrando el programa." + Style.RESET_ALL)
        sys.exit()

    # Bucle infinito para mostrar el menú y gestionar las opciones
    while True:
        # Título del menú
        titulo = "Menú Principal"
        ancho = 30
        
        # Mostrar menú con líneas azules
        print("\n\033[94m" + "-" * ancho + "\033[0m")  
        print('\033[1;97;104m' + titulo.center(ancho) + "\033[0m")  
        print("\033[94m" + "-" * ancho + "\033[0m\n")
        # Opciones del menú
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Generar reporte de bajo stock")
        print("7. Salir\n")
        # Solicitar al usuario que seleccione una opción
        opcion = input("Seleccione una opción: ")
      
        # Gestionar la opción seleccionada
        if opcion == "1":
            registrar_producto(conexion)
        elif opcion == "2":
            mostrar_productos(conexion)
        elif opcion == "3":
            actualizar_producto(conexion)
        elif opcion == "4":
            eliminar_producto(conexion)
        elif opcion == "5":
            buscar_producto(conexion)
        elif opcion == "6":
            reporte_bajo_stock(conexion)
        elif opcion == "7":
            print("\n\033[35m¡Gracias por usar la aplicación!\n\033[0m")
            print("Saliendo del programa...")
            conexion.close()
            print("\n") 
            break
        else:
            # Mensaje de error para opciones no válidas
            print(Fore.YELLOW + "Opción no válida. Intente nuevamente." + Style.RESET_ALL)

# Inicializar el menú
if __name__ == "__main__":
    menu_principal()
