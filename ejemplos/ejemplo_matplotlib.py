"""
Ejemplo básico de la librería matplotlib
Para crear gráficos y visualizaciones de datos
"""

import matplotlib.pyplot as plt
import numpy as np

def ejemplo_matplotlib():
    """Ejemplos básicos de uso de la librería matplotlib"""
    
    print("📊 Ejemplos con la librería matplotlib")
    print("=" * 40)
    
    # Ejemplo 1: Gráfico de líneas simple
    print("\n1. Creando un gráfico de líneas:")
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 2, 1)
    plt.plot(x, y, marker='o')
    plt.title('Gráfico de Líneas')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    
    # Ejemplo 2: Gráfico de barras
    print("2. Creando un gráfico de barras:")
    categorias = ['Python', 'JavaScript', 'Java', 'C++', 'C#']
    popularidad = [85, 70, 65, 60, 55]
    
    plt.subplot(2, 2, 2)
    plt.bar(categorias, popularidad, color=['blue', 'orange', 'green', 'red', 'purple'])
    plt.title('Popularidad de Lenguajes de Programación')
    plt.xlabel('Lenguajes')
    plt.ylabel('Popularidad (%)')
    plt.xticks(rotation=45)
    
    # Ejemplo 3: Histograma
    print("3. Creando un histograma:")
    datos = np.random.normal(100, 15, 1000)  # 1000 valores con media 100 y desviación 15
    
    plt.subplot(2, 2, 3)
    plt.hist(datos, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title('Distribución de Datos')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    
    # Ejemplo 4: Gráfico circular (pie chart)
    print("4. Creando un gráfico circular:")
    etiquetas = ['Trabajo', 'Estudios', 'Ocio', 'Descanso']
    tamaños = [8, 6, 4, 6]
    colores = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
    
    plt.subplot(2, 2, 4)
    plt.pie(tamaños, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=90)
    plt.title('Distribución del Tiempo Diario')
    
    plt.tight_layout()
    
    # Guardar el gráfico
    plt.savefig('ejemplos/graficos_ejemplo.png', dpi=300, bbox_inches='tight')
    print("   ✅ Gráficos guardados en 'ejemplos/graficos_ejemplo.png'")
    
    # Mostrar en pantalla (opcional, comentado para evitar problemas en servidores)
    # plt.show()
    
    plt.close()

def ejemplo_grafico_avanzado():
    """Ejemplo más avanzado con múltiples series de datos"""
    
    print("\n5. Creando un gráfico más avanzado:")
    
    # Datos de ejemplo
    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
    ventas_2022 = [120, 135, 140, 165, 180, 195]
    ventas_2023 = [130, 145, 155, 175, 190, 210]
    
    plt.figure(figsize=(10, 6))
    
    # Gráfico de líneas con dos series
    plt.plot(meses, ventas_2022, marker='o', linewidth=2, label='2022')
    plt.plot(meses, ventas_2023, marker='s', linewidth=2, label='2023')
    
    plt.title('Comparación de Ventas por Mes', fontsize=16, fontweight='bold')
    plt.xlabel('Mes', fontsize=12)
    plt.ylabel('Ventas (miles €)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Añadir anotación
    plt.annotate('Mayor crecimiento', 
                xy=('Jun', 210), 
                xytext=('Abr', 220),
                arrowprops=dict(arrowstyle='->', color='red'),
                fontsize=10)
    
    plt.tight_layout()
    plt.savefig('ejemplos/ventas_comparacion.png', dpi=300, bbox_inches='tight')
    print("   ✅ Gráfico de comparación guardado en 'ejemplos/ventas_comparacion.png'")
    plt.close()

if __name__ == "__main__":
    ejemplo_matplotlib()
    ejemplo_grafico_avanzado()