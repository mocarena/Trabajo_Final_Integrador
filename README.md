# Trabajo_Final_Integrador 
## Proyecto de Inventario en Python

Este es un programa de gestión de inventarios desarrollado en Python utilizando SQLite como base de datos. Permite a los usuarios registrar, actualizar, eliminar y consultar productos de un inventario de manera sencilla y eficiente.

## Funcionalidades

El sistema proporciona un conjunto de funcionalidades principales:

- **Registrar un producto**: Permite agregar un nuevo producto al inventario con información como nombre, descripción, cantidad, precio y categoría.
- **Mostrar todos los productos**: Muestra una lista completa de los productos en el inventario.
- **Actualizar un producto**: Permite actualizar la cantidad de un producto específico.
- **Eliminar un producto**: Elimina un producto del inventario mediante su ID.
- **Buscar un producto**: Permite buscar productos por nombre o categoría.
- **Generar reporte de bajo stock**: Muestra productos cuyo stock es menor o igual al límite especificado.

## Requisitos

Para poder ejecutar este proyecto, necesitarás tener instalados los siguientes componentes:

- **Python 3.x**: El lenguaje de programación utilizado para desarrollar este proyecto.
- **SQLite3**: La base de datos utilizada para almacenar la información de los productos.
- **colorama**: Una librería para agregar colores a la terminal.

Puedes instalar la librería `colorama` ejecutando el siguiente comando:
```bash
pip install colorama
```
## Instalación

- Clona este repositorio a tu máquina local:
git clone https://github.com/tu_usuario/Trabajo_Final_Integrador.git
- Entra en el directorio del proyecto:
cd Trabajo_Final_Integrador

## Instala las dependencias necesarias:

- Instalar colorama
- Debes tener un archivo de base de datos SQLite con el nombre inventario.db en la ruta especificada en el código, o modifica el código para ajustar la ruta de la base de datos.

## Uso

Ejecutar el programa: simplemente ejecuta el archivo inventario.py:
```bash
python inventario.py
```

## Menú principal
Cuando ejecutes el programa, se mostrará un menú con las siguientes opciones:
- Registrar producto: Permite agregar un nuevo producto al inventario.
- Mostrar productos: Muestra todos los productos almacenados en la base de datos.
- Actualizar producto: Permite actualizar la cantidad de un producto específico.
- Eliminar producto: Permite eliminar un producto de la base de datos.
- Buscar producto: Permite buscar productos por nombre o categoría.
- Generar reporte de bajo stock: Muestra los productos con stock bajo según un límite especificado.
- Salir: Cierra el programa.

## Ejemplo de interacción:

Menú Principal

1. Registrar producto
2. Mostrar productos
3. Actualizar producto
4. Eliminar producto
5. Buscar producto
6. Generar reporte de bajo stock
7. Salir
- Seleccione una opción: 1
- Nombre del producto: Teclado
- Descripción: Teclado mecánico
- Cantidad: 50
- Precio: 100.0
- Categoría: Periféricos
- Producto registrado con éxito.

## Estructura del Proyecto
La estructura básica del proyecto es la siguiente:
```
Trabajo_Final_Integrador/
│
├── inventario.py    # Archivo principal con el código del sistema de inventario
├── inventario.db    # Base de datos SQLite que almacena los productos
├── README.md        # Documento con la documentación del proyecto
```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. 

