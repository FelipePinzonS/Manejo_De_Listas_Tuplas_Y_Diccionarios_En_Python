# Manejo de Listas, Tuplas y Diccionarios en Python

## Nombre: Felipe Pinzon Segura
## Marticula: 2530495
## Grupo: IM 1-2

# Resumen Ejecutivo
"""
En Python, las listas, tuplas y diccionarios son estructuras de datos fundamentales:
- Listas: Colecciones ordenadas y mutables, ideales para almacenar secuencias de elementos que pueden cambiar.
- Tuplas: Colecciones ordenadas e inmutables, útiles para datos que no deben modificarse.
- Diccionarios: Colecciones de pares clave-valor, permiten búsquedas rápidas por clave.

Este documento cubre 6 problemas prácticos que demuestran el uso de estas estructuras en contextos como 
listas de compras, cálculos geométricos, catálogos de productos, sistemas de calificaciones, contadores 
de frecuencia y agendas de contactos, incluyendo validaciones y casos de prueba.
"""

# Principles & Good Practices (short list)
"""
- Usar listas cuando necesites agregar o eliminar elementos con frecuencia.
- Usar tuplas para datos que no deben cambiar (coordenadas, configuraciones fijas).
- Usar diccionarios cuando necesites buscar información por una clave.
- Evitar modificar una lista mientras la recorres con un for.
- Usar nombres de claves descriptivos en diccionarios.
- Escribir código legible y mensajes claros para el usuario.
"""


# Problem 1: Shopping list basics (list operations)
"""
Description: Work with a list of products (strings) and their quantities (integers).

Inputs:
- initial_items_text (string; e.g., "apple,banana,orange")
- new_item (string; product to add)
- search_item (string; product to search for)

Outputs:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false

Validations:
- initial_items_text not empty after strip()
- Split string by commas and remove extra spaces
- new_item and search_item not empty

Test cases:
1) Normal: initial_items_text="apple, banana, orange", new_item="milk", search_item="banana"
2) Border: initial_items_text="apple", new_item="", search_item="apple" (empty new_item)
3) Error: initial_items_text="", new_item="milk", search_item="banana" (empty initial)
"""

# Obtener entradas
initial_items_text = input("Enter initial items (comma-separated): ").strip()
new_item = input("Enter new item to add: ").strip()
search_item = input("Enter item to search for: ").strip()
    
# Validaciones
if not initial_items_text:
    print("Error: initial items cannot be empty")
    
# Procesar elementos iniciales
items_list = [item.strip() for item in initial_items_text.split(',')]
items_list = [item for item in items_list if item]  # Eliminar cadenas vacías
    
# Agregar nuevo elemento si no está vacío
if new_item:
    items_list.append(new_item)
    
# Buscar elemento
found = search_item in items_list if search_item else False
    
# Salidas
print("Items list:", items_list)
print("Total items:", len(items_list))
print("Found item:", str(found).lower())


# Problem 2: Points and distances with tuples
"""
Description: Use tuples to represent two points in 2D plane and calculate distance and midpoint.

Inputs:
- x1, y1, x2, y2 (float; coordinates of points)

Outputs:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)

Validations:
- Verify all 4 inputs can be converted to float

Test cases:
1) Normal: x1=0, y1=0, x2=3, y2=4 (distance=5, midpoint=(1.5, 2.0))
2) Border: x1=1.5, y1=2.5, x2=1.5, y2=2.5 (distance=0, midpoint=(1.5, 2.5))
3) Error: x1="a", y1=0, x2=3, y2=4 (invalid input)
"""

try:
    # Obtener entradas
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
        
    # Crear tuplas
    point_a = (x1, y1)
    point_b = (x2, y2)
        
    # Calcular distancia
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        
     # Calcular punto medio
    midpoint = ((x1 + x2)/2, (y1 + y2)/2)
        
     # Salidas
    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 2))
    print("Midpoint:", midpoint)
        
except ValueError:
    print("Error: invalid input - all coordinates must be numbers")


# Problem 3: Product catalog with dictionary
"""
Description: Manage a product catalog using dictionary with product names as keys and prices as values.

Inputs:
- product_name (string)
- quantity (int; quantity to purchase)

Outputs:
- If product exists: "Unit price:", "Quantity:", "Total:"
- If not exists: "Error: product not found"

Validations:
- quantity > 0
- product_name not empty after strip()
- Verify product_name exists in dictionary

Test cases:
1) Normal: product_name="apple", quantity=3 (exists)
2) Border: product_name="banana", quantity=1 (exists)
3) Error: product_name="grape", quantity=2 (not exists)
"""

# Catálogo inicial de productos
product_prices = {
    "apple": 10.0,
    "banana": 5.0,
    "orange": 8.0
}
    
# Obtener entradas
product_name = input("Enter product name: ").strip()
try:
    quantity = int(input("Enter quantity: "))
except ValueError:
    print("Error: quantity must be an integer")

    
# Validaciones
if not product_name:
    print("Error: product name cannot be empty")
    
if quantity <= 0:
    print("Error: quantity must be positive")
    
# Verificar si el producto existe
if product_name in product_prices:
    unit_price = product_prices[product_name]
    total_price = unit_price * quantity
        
    print("Unit price:", unit_price)
    print("Quantity:", quantity)
    print("Total:", total_price)
else:
    print("Error: product not found")


# Problem 4: Student grades with dict and list
"""
Description: Manage student grades using dictionary with student names as keys and grade lists as values.

Inputs:
- student_name (string)

Outputs:
- If student exists: "Grades:", "Average:", "Passed:" true|false
- If not exists: "Error: student not found"

Validations:
- student_name not empty after strip()
- Verify student_name exists in dictionary
- Verify grade list is not empty before calculating average

Test cases:
1) Normal: student_name="alice" (exists, average=87.5, passed=true)
2) Border: student_name="bob" (exists, average=70.0, passed=false)
3) Error: student_name="david" (not exists)
""" 
    
# Calificaciones iniciales de estudiantes
student_grades_dict = {
    "alice": [90.0, 85.0, 88.0, 87.0],
    "bob": [70.0, 70.0, 70.0, 70.0],
    "charlie": [65.0, 70.0, 72.0, 69.0]
}
    
# Obtener entrada
student_name = input("Enter student name: ").strip().lower()
    
# Validaciones
if not student_name:
    print("Error: student name cannot be empty")
    
# Verificar si el estudiante existe
if student_name in student_grades_dict:
    grades = student_grades_dict[student_name]
        
    if not grades:
        print("Error: no grades available for this student")
        
    # Calcular promedio
    average = sum(grades) / len(grades)
    passed = average >= 70.0
        
    print("Grades:", grades)
    print("Average:", round(average, 2))
    print("Passed:", str(passed).lower())
else:
    print("Error: student not found")


# Problem 5: Word frequency counter (list + dict)
"""
Description: Count frequency of each word in a sentence using list and dictionary.

Inputs:
- sentence (string)

Outputs:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word>

Validations:
- sentence not empty after strip()
- Verify words list is not empty

Test cases:
1) Normal: sentence="hello world hello python" (freq: hello:2, world:1, python:1)
2) Border: sentence="test test test" (freq: test:3)
3) Error: sentence="" (empty input)
"""

# Leer la oración
sentence = input("Enter a sentence: ").strip()

# Validar que la oración no esté vacía
if not sentence:
    print("Error: The sentence cannot be empty.")
else:
    # Convertir a minúsculas y manejar signos de puntuación básicos
    sentence_clean = sentence.lower()
    # Remover signos de puntuación comunes
    for char in ".,!?;:\"'":
        sentence_clean = sentence_clean.replace(char, ' ')
    
    # Separar en lista de palabras
    words_list = sentence_clean.split()
    
    # Validar que la lista de palabras no esté vacía
    if not words_list:
        print("Error: No words found in the sentence.")
    else:
        # Construir diccionario de frecuencias
        freq_dict = {}
        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
        
        # Encontrar la palabra más frecuente
        most_common_word = None
        max_frequency = 0
        
        for word, frequency in freq_dict.items():
            if frequency > max_frequency:
                max_frequency = frequency
                most_common_word = word
        
        # Mostrar resultados
        print(f"Words list: {words_list}")
        print(f"Frequencies: {freq_dict}")
        print(f"Most common word: {most_common_word}")


# Problem 6: Simple contact book (dictionary CRUD)
"""
Description: Implement a contact book using dictionary with CRUD operations.

Inputs:
- action_text (string; "ADD", "SEARCH", or "DELETE")
- name (string; contact name)
- phone (string; only for "ADD")

Outputs:
- For "ADD": "Contact saved:" name, phone
- For "SEARCH": "Phone:" <phone> or "Error: contact not found"
- For "DELETE": "Contact deleted:" name or "Error: contact not found"

Validations:
- Normalize action_text to uppercase
- Verify action_text is one of valid options
- name not empty after strip()
- For "ADD": phone not empty after strip()

Test cases:
1) Normal: action="ADD", name="john", phone="1231231231"
2) Border: action="SEARCH", name="bob" (exists)
3) Error: action="DELETE", name="Unknown" (not exists)
"""

# Contactos iniciales
contacts = {
    "alice": "1234567890",
    "bob": "9876543210"
}
    
# Obtener acción
action_text = input("Enter action (ADD/SEARCH/DELETE): ").strip().upper()
    
# Validaciones
valid_actions = ["ADD", "SEARCH", "DELETE"]
if action_text not in valid_actions:
    print("Error: invalid action")
    
# Obtener nombre
name = input("Enter contact name: ").strip().lower()
if not name:
    print("Error: name cannot be empty")
    
# Procesar acciones
if action_text == "ADD":
    phone = int(input("Enter phone number: ").strip())
    if not phone:
        print("Error: phone cannot be empty")
        
    contacts[name] = phone
    print("Contact saved:", name, phone)
        
elif action_text == "SEARCH":
    if name in contacts:
        print("Phone:", contacts[name])
    else:
        print("Error: contact not found")
            
elif action_text == "DELETE":
    if name in contacts:
        del contacts[name]
        print("Contact deleted:", name)
    else:
        print("Error: contact not found")


# CONCLUSIONES
"""
- Las listas son ideales cuando necesitamos colecciones ordenadas y modificables, permitiendo 
  operaciones flexibles de agregado y eliminación.
- Las tuplas son útiles para datos inmutables que no deben cambiar durante la ejecución del programa,
  como coordenadas o configuraciones fijas.
- Los diccionarios facilitan búsquedas rápidas por clave, siendo óptimos para catálogos, 
  configuraciones y datos estructurados.
- Los patrones comunes incluyen diccionarios de listas (como en calificaciones de estudiantes) y
  listas de tuplas (para datos estructurados inmutables).
- La combinación de estas estructuras permite modelar problemas complejos de manera eficiente y legible.
"""

# REFERENCIAS
"""
    1) Python - Built-in Types
       URL: https://docs.python.org/3.11/library/stdtypes.html
    2) Python - Data Structures
       URL: https://docs.python.org/3.11/tutorial/datastructures.html
    3) W3schools - Python Lists
       URL: https://www.w3schools.com/python/python_lists.asp
    4) Real Python - Dictionaries in Python
       URL: https://realpython.com/python-dicts/
    5) Youtube - Lists & Tuples in Python
       URL: https://www.youtube.com/watch?v=hANUgg72TDc&list=PL98qAXLA6afuh50qD2MdAj3ofYjZR_Phn
"""
# REPOSITORIO DE GITHUB
"""
    URL: https://github.com/FelipePinzonS/Manejo_De_Listas_Tuplas_Y_Diccionarios_En_Python.git
"""