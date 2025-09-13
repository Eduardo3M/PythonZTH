#!/usr/bin/env python3
"""
Script de instalación para las 5 librerías más famosas de Python para principiantes
"""

import subprocess
import sys
import os

def install_requirements():
    """Instala las dependencias desde requirements.txt"""
    print("🐍 Instalando las 5 librerías más famosas de Python para principiantes...")
    print("=" * 60)
    
    try:
        # Verificar si pip está disponible
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
        
        # Actualizar pip
        print("📦 Actualizando pip...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        
        # Instalar dependencias
        print("📚 Instalando librerías desde requirements.txt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        
        print("\n✅ ¡Instalación completada exitosamente!")
        print("\nLibrerías instaladas:")
        print("1. 🌐 requests - Para peticiones HTTP")
        print("2. 📊 matplotlib - Para gráficos y visualizaciones")
        print("3. 🐼 pandas - Para análisis de datos")
        print("4. 🔢 numpy - Para computación numérica")
        print("5. 🕷️ beautifulsoup4 - Para web scraping")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error durante la instalación: {e}")
        return False
    except FileNotFoundError:
        print("❌ Error: No se pudo encontrar pip. Asegúrate de que Python esté instalado correctamente.")
        return False

def verify_installation():
    """Verifica que las librerías se hayan instalado correctamente"""
    print("\n🔍 Verificando instalación...")
    
    libraries = [
        ("requests", "requests"),
        ("matplotlib", "matplotlib"),
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("beautifulsoup4", "bs4")
    ]
    
    all_installed = True
    
    for lib_name, import_name in libraries:
        try:
            # Use subprocess to test imports in clean environment
            result = subprocess.run([sys.executable, "-c", f"import {import_name}"], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"✅ {lib_name} - Instalada correctamente")
            else:
                print(f"❌ {lib_name} - Error en la instalación: {result.stderr.strip()}")
                all_installed = False
        except Exception as e:
            print(f"❌ {lib_name} - Error verificando instalación: {e}")
            all_installed = False
    
    return all_installed

if __name__ == "__main__":
    print("🚀 Script de instalación de librerías Python para principiantes")
    print("Este script instalará las 5 librerías más populares para comenzar en Python\n")
    
    # Cambiar al directorio del script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Instalar dependencias
    if install_requirements():
        # Verificar instalación
        if verify_installation():
            print("\n🎉 ¡Todo listo! Puedes comenzar a usar las librerías.")
            print("💡 Consulta los archivos de ejemplo para aprender cómo usarlas.")
        else:
            print("\n⚠️ Algunas librerías no se instalaron correctamente.")
            sys.exit(1)
    else:
        print("\n❌ La instalación falló.")
        sys.exit(1)