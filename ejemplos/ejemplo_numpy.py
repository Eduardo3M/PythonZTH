"""
Ejemplo básico de la librería numpy
Para computación numérica y trabajo con arrays
"""

import numpy as np

def ejemplo_numpy():
    """Ejemplos básicos de uso de la librería numpy"""
    
    print("🔢 Ejemplos con la librería numpy")
    print("=" * 40)
    
    # Ejemplo 1: Creación de arrays
    print("\n1. Creación de arrays:")
    
    # Array unidimensional
    arr1d = np.array([1, 2, 3, 4, 5])
    print(f"   Array 1D: {arr1d}")
    print(f"   Tipo: {type(arr1d)}")
    print(f"   Forma: {arr1d.shape}")
    
    # Array bidimensional
    arr2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"   Array 2D:\n{arr2d}")
    print(f"   Forma: {arr2d.shape}")
    
    # Ejemplo 2: Arrays especiales
    print("\n2. Creación de arrays especiales:")
    
    zeros = np.zeros((3, 3))
    print(f"   Array de ceros (3x3):\n{zeros}")
    
    ones = np.ones((2, 4))
    print(f"   Array de unos (2x4):\n{ones}")
    
    rango = np.arange(0, 10, 2)
    print(f"   Array con rango (0-10, paso 2): {rango}")
    
    linspace = np.linspace(0, 1, 5)
    print(f"   Array con espaciado lineal (0-1, 5 puntos): {linspace}")
    
    # Ejemplo 3: Operaciones matemáticas
    print("\n3. Operaciones matemáticas:")
    
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    
    print(f"   Array a: {a}")
    print(f"   Array b: {b}")
    print(f"   Suma: {a + b}")
    print(f"   Resta: {a - b}")
    print(f"   Multiplicación: {a * b}")
    print(f"   División: {a / b}")
    print(f"   Potencia: {a ** 2}")
    
    # Ejemplo 4: Funciones matemáticas
    print("\n4. Funciones matemáticas:")
    
    angulos = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
    print(f"   Ángulos: {angulos}")
    print(f"   Seno: {np.sin(angulos).round(3)}")
    print(f"   Coseno: {np.cos(angulos).round(3)}")
    print(f"   Raíz cuadrada de [1,4,9,16]: {np.sqrt([1, 4, 9, 16])}")
    
    # Ejemplo 5: Estadísticas
    print("\n5. Estadísticas básicas:")
    
    datos = np.random.normal(50, 10, 1000)  # 1000 valores normales, media=50, std=10
    print(f"   Datos generados: {len(datos)} valores")
    print(f"   Media: {np.mean(datos):.2f}")
    print(f"   Mediana: {np.median(datos):.2f}")
    print(f"   Desviación estándar: {np.std(datos):.2f}")
    print(f"   Mínimo: {np.min(datos):.2f}")
    print(f"   Máximo: {np.max(datos):.2f}")

def ejemplo_numpy_avanzado():
    """Ejemplos más avanzados con numpy"""
    
    print("\n" + "=" * 50)
    print("🚀 Ejemplos avanzados con numpy")
    print("=" * 50)
    
    # Ejemplo 1: Indexado y slicing
    print("\n1. Indexado y slicing:")
    
    matriz = np.random.randint(1, 100, (5, 5))
    print(f"   Matriz 5x5:\n{matriz}")
    print(f"   Primera fila: {matriz[0]}")
    print(f"   Primera columna: {matriz[:, 0]}")
    print(f"   Submatriz 2x2 (esquina superior izquierda):\n{matriz[:2, :2]}")
    
    # Ejemplo 2: Operaciones con matrices
    print("\n2. Operaciones con matrices:")
    
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print(f"   Matriz A:\n{A}")
    print(f"   Matriz B:\n{B}")
    print(f"   Multiplicación de matrices (A @ B):\n{A @ B}")
    print(f"   Transpuesta de A:\n{A.T}")
    print(f"   Determinante de A: {np.linalg.det(A):.2f}")
    
    # Ejemplo 3: Broadcasting
    print("\n3. Broadcasting:")
    
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    vector = np.array([10, 20, 30])
    
    print(f"   Array original:\n{arr}")
    print(f"   Vector: {vector}")
    print(f"   Suma con broadcasting:\n{arr + vector}")
    
    # Ejemplo 4: Filtrado con condiciones
    print("\n4. Filtrado con condiciones:")
    
    numeros = np.random.randint(1, 50, 20)
    print(f"   Números: {numeros}")
    
    pares = numeros[numeros % 2 == 0]
    mayores_25 = numeros[numeros > 25]
    
    print(f"   Números pares: {pares}")
    print(f"   Números > 25: {mayores_25}")
    
    # Ejemplo 5: Reshape y manipulación de formas
    print("\n5. Manipulación de formas:")
    
    original = np.arange(12)
    print(f"   Array original: {original}")
    
    reshaped_2d = original.reshape(3, 4)
    print(f"   Reshape a 3x4:\n{reshaped_2d}")
    
    reshaped_3d = original.reshape(2, 2, 3)
    print(f"   Reshape a 2x2x3:\n{reshaped_3d}")
    
    flattened = reshaped_2d.flatten()
    print(f"   Aplanado: {flattened}")

if __name__ == "__main__":
    ejemplo_numpy()
    ejemplo_numpy_avanzado()