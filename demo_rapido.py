#!/usr/bin/env python3
"""
Demostración rápida de las 5 librerías más famosas de Python
Ejecuta ejemplos básicos de cada librería para verificar que funcionan
"""

def demo_requests():
    """Demostración básica de requests"""
    print("🌐 Demostración de requests:")
    try:
        import requests
        print("✅ requests importado correctamente")
        # Demo sin red para evitar problemas de conectividad
        print("   Librería lista para hacer peticiones HTTP y trabajar con APIs")
        return True
    except ImportError:
        print("❌ Error al importar requests")
        return False

def demo_matplotlib():
    """Demostración básica de matplotlib"""
    print("\n📊 Demostración de matplotlib:")
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        print("✅ matplotlib importado correctamente")
        
        # Crear un gráfico simple
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        plt.figure(figsize=(6, 4))
        plt.plot(x, y, 'b-o')
        plt.title('Gráfico de Demostración')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.savefig('/tmp/demo_plot.png', dpi=150, bbox_inches='tight')
        plt.close()
        print("   ✅ Gráfico creado y guardado en /tmp/demo_plot.png")
        return True
    except ImportError:
        print("❌ Error al importar matplotlib")
        return False

def demo_pandas():
    """Demostración básica de pandas"""
    print("\n🐼 Demostración de pandas:")
    try:
        import pandas as pd
        print("✅ pandas importado correctamente")
        
        # Crear un DataFrame simple
        data = {
            'Nombre': ['Ana', 'Luis', 'María'],
            'Edad': [25, 30, 22],
            'Puntuación': [95, 87, 92]
        }
        df = pd.DataFrame(data)
        print("   ✅ DataFrame creado:")
        print(df.to_string(index=False))
        print(f"   📊 Estadísticas: Edad promedio = {df['Edad'].mean():.1f}")
        return True
    except ImportError:
        print("❌ Error al importar pandas")
        return False

def demo_numpy():
    """Demostración básica de numpy"""
    print("\n🔢 Demostración de numpy:")
    try:
        import numpy as np
        print("✅ numpy importado correctamente")
        
        # Operaciones básicas
        arr = np.array([1, 2, 3, 4, 5])
        print(f"   Array: {arr}")
        print(f"   Suma: {np.sum(arr)}")
        print(f"   Media: {np.mean(arr)}")
        print(f"   Matriz 2x3:\n{np.arange(6).reshape(2, 3)}")
        return True
    except ImportError:
        print("❌ Error al importar numpy")
        return False

def demo_beautifulsoup():
    """Demostración básica de beautifulsoup4"""
    print("\n🕷️ Demostración de beautifulsoup4:")
    try:
        from bs4 import BeautifulSoup
        print("✅ beautifulsoup4 importado correctamente")
        
        # Analizar HTML simple
        html = "<html><body><h1>¡Hola Mundo!</h1><p>Texto de ejemplo</p></body></html>"
        soup = BeautifulSoup(html, 'html.parser')
        titulo = soup.find('h1').text
        parrafo = soup.find('p').text
        print(f"   ✅ HTML analizado - Título: '{titulo}', Párrafo: '{parrafo}'")
        return True
    except ImportError:
        print("❌ Error al importar beautifulsoup4")
        return False

def main():
    """Función principal de demostración"""
    print("=" * 60)
    print("🐍 DEMOSTRACIÓN DE LAS 5 LIBRERÍAS MÁS FAMOSAS DE PYTHON")
    print("=" * 60)
    
    demos = [
        demo_requests,
        demo_matplotlib, 
        demo_pandas,
        demo_numpy,
        demo_beautifulsoup
    ]
    
    resultados = []
    for demo in demos:
        try:
            resultado = demo()
            resultados.append(resultado)
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            resultados.append(False)
    
    # Resumen
    print("\n" + "=" * 60)
    print("📋 RESUMEN DE LA DEMOSTRACIÓN")
    print("=" * 60)
    
    libreras = ["requests", "matplotlib", "pandas", "numpy", "beautifulsoup4"]
    exitosos = 0
    
    for i, (libreria, resultado) in enumerate(zip(libreras, resultados)):
        estado = "✅ FUNCIONANDO" if resultado else "❌ ERROR"
        print(f"{libreria:15} - {estado}")
        if resultado:
            exitosos += 1
    
    print(f"\n📊 Librerías funcionando: {exitosos}/{len(libreras)}")
    
    if exitosos == len(libreras):
        print("\n🎉 ¡Todas las librerías están instaladas y funcionando!")
        print("💡 Ejecuta 'python ejecutar_ejemplos.py' para ver ejemplos detallados")
        print("📚 Consulta el README.md para más información")
    else:
        print("\n⚠️ Algunas librerías tienen problemas.")
        print("💡 Ejecuta 'python instalar_librerias.py' para intentar solucionarlos")

if __name__ == "__main__":
    main()