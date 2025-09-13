"""
Ejecutor principal de todos los ejemplos
Demuestra el uso de las 5 librerías más famosas de Python para principiantes
"""

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "="*60)
    print("🐍 EJEMPLOS DE LAS 5 LIBRERÍAS MÁS FAMOSAS DE PYTHON")
    print("="*60)
    print("1. 🌐 requests - Peticiones HTTP y APIs")
    print("2. 📊 matplotlib - Gráficos y visualizaciones")
    print("3. 🐼 pandas - Manipulación y análisis de datos")
    print("4. 🔢 numpy - Computación numérica")
    print("5. 🕷️ beautifulsoup4 - Web scraping y HTML")
    print("6. 🚀 Ejecutar todos los ejemplos")
    print("0. ❌ Salir")
    print("="*60)

def ejecutar_ejemplo_requests():
    """Ejecuta el ejemplo de requests"""
    try:
        from ejemplos.ejemplo_requests import ejemplo_requests
        ejemplo_requests()
        return True
    except ImportError as e:
        print(f"❌ Error: La librería requests no está instalada. {e}")
        return False
    except Exception as e:
        print(f"❌ Error ejecutando ejemplo de requests: {e}")
        return False

def ejecutar_ejemplo_matplotlib():
    """Ejecuta el ejemplo de matplotlib"""
    try:
        from ejemplos.ejemplo_matplotlib import ejemplo_matplotlib, ejemplo_grafico_avanzado
        ejemplo_matplotlib()
        ejemplo_grafico_avanzado()
        return True
    except ImportError as e:
        print(f"❌ Error: La librería matplotlib no está instalada. {e}")
        return False
    except Exception as e:
        print(f"❌ Error ejecutando ejemplo de matplotlib: {e}")
        return False

def ejecutar_ejemplo_pandas():
    """Ejecuta el ejemplo de pandas"""
    try:
        from ejemplos.ejemplo_pandas import ejemplo_pandas, ejemplo_pandas_avanzado
        ejemplo_pandas()
        ejemplo_pandas_avanzado()
        return True
    except ImportError as e:
        print(f"❌ Error: La librería pandas no está instalada. {e}")
        return False
    except Exception as e:
        print(f"❌ Error ejecutando ejemplo de pandas: {e}")
        return False

def ejecutar_ejemplo_numpy():
    """Ejecuta el ejemplo de numpy"""
    try:
        from ejemplos.ejemplo_numpy import ejemplo_numpy, ejemplo_numpy_avanzado
        ejemplo_numpy()
        ejemplo_numpy_avanzado()
        return True
    except ImportError as e:
        print(f"❌ Error: La librería numpy no está instalada. {e}")
        return False
    except Exception as e:
        print(f"❌ Error ejecutando ejemplo de numpy: {e}")
        return False

def ejecutar_ejemplo_beautifulsoup():
    """Ejecuta el ejemplo de beautifulsoup4"""
    try:
        from ejemplos.ejemplo_beautifulsoup import ejemplo_beautifulsoup, ejemplo_web_scraping, ejemplo_parsing_avanzado
        ejemplo_beautifulsoup()
        ejemplo_web_scraping()
        ejemplo_parsing_avanzado()
        return True
    except ImportError as e:
        print(f"❌ Error: La librería beautifulsoup4 no está instalada. {e}")
        return False
    except Exception as e:
        print(f"❌ Error ejecutando ejemplo de beautifulsoup4: {e}")
        return False

def ejecutar_todos_ejemplos():
    """Ejecuta todos los ejemplos"""
    print("\n🚀 Ejecutando todos los ejemplos...")
    
    ejemplos = [
        ("requests", ejecutar_ejemplo_requests),
        ("matplotlib", ejecutar_ejemplo_matplotlib),
        ("pandas", ejecutar_ejemplo_pandas),
        ("numpy", ejecutar_ejemplo_numpy),
        ("beautifulsoup4", ejecutar_ejemplo_beautifulsoup)
    ]
    
    resultados = []
    
    for nombre, funcion in ejemplos:
        print(f"\n📦 Ejecutando ejemplo de {nombre}...")
        try:
            exito = funcion()
            resultados.append((nombre, exito))
            if exito:
                print(f"✅ {nombre} - Completado exitosamente")
            else:
                print(f"❌ {nombre} - Error en la ejecución")
        except Exception as e:
            print(f"❌ {nombre} - Error inesperado: {e}")
            resultados.append((nombre, False))
    
    # Resumen final
    print("\n" + "="*50)
    print("📋 RESUMEN DE EJECUCIÓN")
    print("="*50)
    
    exitosos = 0
    for nombre, exito in resultados:
        estado = "✅ ÉXITO" if exito else "❌ ERROR"
        print(f"{nombre:15} - {estado}")
        if exito:
            exitosos += 1
    
    print(f"\n📊 Ejemplos ejecutados exitosamente: {exitosos}/{len(resultados)}")
    
    if exitosos == len(resultados):
        print("🎉 ¡Todas las librerías funcionan correctamente!")
    else:
        print("⚠️ Algunas librerías tienen problemas. Verifica la instalación.")

def verificar_instalacion():
    """Verifica que todas las librerías estén instaladas"""
    print("\n🔍 Verificando instalación de librerías...")
    
    librerias = [
        ("requests", "requests"),
        ("matplotlib", "matplotlib"),
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("beautifulsoup4", "bs4")
    ]
    
    todas_instaladas = True
    
    for nombre, modulo in librerias:
        try:
            __import__(modulo)
            print(f"✅ {nombre} - Instalada")
        except ImportError:
            print(f"❌ {nombre} - No instalada")
            todas_instaladas = False
    
    if not todas_instaladas:
        print("\n💡 Para instalar las librerías faltantes, ejecuta:")
        print("   python instalar_librerias.py")
        print("   o")
        print("   pip install -r requirements.txt")
    
    return todas_instaladas

def main():
    """Función principal"""
    print("🎯 Iniciando demostración de librerías Python...")
    
    # Verificar instalación al inicio
    if not verificar_instalacion():
        print("\n⚠️ Algunas librerías no están instaladas.")
        respuesta = input("¿Deseas continuar de todas formas? (s/n): ").lower()
        if respuesta != 's':
            print("👋 ¡Hasta luego!")
            return
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\n👉 Selecciona una opción: ").strip()
            
            if opcion == "0":
                print("👋 ¡Gracias por probar las librerías Python!")
                break
            elif opcion == "1":
                ejecutar_ejemplo_requests()
            elif opcion == "2":
                ejecutar_ejemplo_matplotlib()
            elif opcion == "3":
                ejecutar_ejemplo_pandas()
            elif opcion == "4":
                ejecutar_ejemplo_numpy()
            elif opcion == "5":
                ejecutar_ejemplo_beautifulsoup()
            elif opcion == "6":
                ejecutar_todos_ejemplos()
            else:
                print("❌ Opción no válida. Por favor, selecciona un número del 0 al 6.")
            
            input("\n⏸️ Presiona Enter para continuar...")
            
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()