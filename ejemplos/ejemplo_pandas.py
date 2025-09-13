"""
Ejemplo básico de la librería pandas
Para manipulación y análisis de datos
"""

import pandas as pd
import numpy as np

def ejemplo_pandas():
    """Ejemplos básicos de uso de la librería pandas"""
    
    print("🐼 Ejemplos con la librería pandas")
    print("=" * 40)
    
    # Ejemplo 1: Crear un DataFrame desde un diccionario
    print("\n1. Creando un DataFrame desde un diccionario:")
    datos = {
        'Nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Elena'],
        'Edad': [25, 30, 22, 35, 28],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao'],
        'Salario': [35000, 45000, 30000, 50000, 40000]
    }
    
    df = pd.DataFrame(datos)
    print("   DataFrame creado:")
    print(df)
    
    # Ejemplo 2: Información básica del DataFrame
    print("\n2. Información básica del DataFrame:")
    print(f"   Forma (filas, columnas): {df.shape}")
    print(f"   Columnas: {list(df.columns)}")
    print(f"   Tipos de datos:")
    print(f"   {df.dtypes}")
    
    # Ejemplo 3: Estadísticas descriptivas
    print("\n3. Estadísticas descriptivas:")
    print(df.describe())
    
    # Ejemplo 4: Filtrado de datos
    print("\n4. Filtrado de datos (personas mayores de 25 años):")
    filtro_edad = df[df['Edad'] > 25]
    print(filtro_edad)
    
    # Ejemplo 5: Agrupación y agregación
    print("\n5. Salario promedio por ciudad:")
    if len(df) > 0:
        # Crear datos adicionales para mejor ejemplo de agrupación
        datos_extendidos = {
            'Nombre': ['Ana', 'Luis', 'María', 'Carlos', 'Elena', 'Pablo', 'Laura'],
            'Edad': [25, 30, 22, 35, 28, 32, 26],
            'Ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Barcelona', 'Madrid', 'Barcelona', 'Valencia'],
            'Salario': [35000, 45000, 30000, 50000, 40000, 48000, 32000]
        }
        df_ext = pd.DataFrame(datos_extendidos)
        salario_por_ciudad = df_ext.groupby('Ciudad')['Salario'].mean()
        print(salario_por_ciudad)
    
    # Ejemplo 6: Añadir nueva columna
    print("\n6. Añadiendo una nueva columna (Salario en miles):")
    df['Salario_Miles'] = df['Salario'] / 1000
    print(df[['Nombre', 'Salario', 'Salario_Miles']])
    
    # Ejemplo 7: Guardar datos
    print("\n7. Guardando datos en CSV:")
    df.to_csv('ejemplos/datos_empleados.csv', index=False)
    print("   ✅ Datos guardados en 'ejemplos/datos_empleados.csv'")

def ejemplo_pandas_avanzado():
    """Ejemplos más avanzados con pandas"""
    
    print("\n" + "=" * 50)
    print("📈 Ejemplos avanzados con pandas")
    print("=" * 50)
    
    # Crear un dataset más grande
    np.random.seed(42)
    n_registros = 100
    
    datos_ventas = {
        'Fecha': pd.date_range('2023-01-01', periods=n_registros, freq='D'),
        'Producto': np.random.choice(['Laptop', 'Mouse', 'Teclado', 'Monitor'], n_registros),
        'Ventas': np.random.randint(10, 100, n_registros),
        'Precio': np.random.uniform(20, 1000, n_registros).round(2),
        'Región': np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], n_registros)
    }
    
    df_ventas = pd.DataFrame(datos_ventas)
    df_ventas['Ingresos'] = df_ventas['Ventas'] * df_ventas['Precio']
    
    print("\n1. Análisis de ventas por producto:")
    ventas_producto = df_ventas.groupby('Producto').agg({
        'Ventas': 'sum',
        'Ingresos': 'sum',
        'Precio': 'mean'
    }).round(2)
    print(ventas_producto)
    
    print("\n2. Top 5 días con mayores ingresos:")
    top_dias = df_ventas.nlargest(5, 'Ingresos')[['Fecha', 'Producto', 'Ingresos']]
    print(top_dias)
    
    print("\n3. Ventas por mes:")
    df_ventas['Mes'] = df_ventas['Fecha'].dt.month
    ventas_mes = df_ventas.groupby('Mes')['Ingresos'].sum()
    print(ventas_mes)
    
    # Guardar análisis
    ventas_producto.to_csv('ejemplos/analisis_ventas.csv')
    print("\n   ✅ Análisis guardado en 'ejemplos/analisis_ventas.csv'")

if __name__ == "__main__":
    ejemplo_pandas()
    ejemplo_pandas_avanzado()