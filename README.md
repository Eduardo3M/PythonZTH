# PythonZTH - Las 5 Librerías Más Famosas de Python 🐍

Prácticas de Python con las 5 librerías más populares para iniciarse en el mundo de la programación.

## 📚 Librerías Incluidas

Este repositorio incluye ejemplos y configuración para las siguientes librerías esenciales:

1. **🌐 requests** - Para realizar peticiones HTTP y trabajar con APIs
2. **📊 matplotlib** - Para crear gráficos y visualizaciones de datos
3. **🐼 pandas** - Para manipulación y análisis de datos
4. **🔢 numpy** - Para computación numérica y trabajo con arrays
5. **🕷️ beautifulsoup4** - Para web scraping y análisis de HTML

## 🚀 Instalación Rápida

### Opción 1: Script Automático (Recomendado)
```bash
python instalar_librerias.py
```

### Opción 2: Instalación Manual
```bash
pip install -r requirements.txt
```

### Opción 3: Instalación Individual
```bash
pip install requests matplotlib pandas numpy beautifulsoup4 lxml
```

## 🎯 Uso

### Ejecutar Todos los Ejemplos
```bash
python ejecutar_ejemplos.py
```

### Ejecutar Ejemplos Individuales
```bash
# Ejemplo de requests
python ejemplos/ejemplo_requests.py

# Ejemplo de matplotlib
python ejemplos/ejemplo_matplotlib.py

# Ejemplo de pandas
python ejemplos/ejemplo_pandas.py

# Ejemplo de numpy
python ejemplos/ejemplo_numpy.py

# Ejemplo de beautifulsoup4
python ejemplos/ejemplo_beautifulsoup.py
```

## 📁 Estructura del Proyecto

```
PythonZTH/
├── README.md                    # Este archivo
├── requirements.txt             # Dependencias del proyecto
├── instalar_librerias.py       # Script de instalación automática
├── ejecutar_ejemplos.py         # Ejecutor principal de ejemplos
└── ejemplos/                    # Carpeta con ejemplos
    ├── ejemplo_requests.py      # Ejemplos de peticiones HTTP
    ├── ejemplo_matplotlib.py    # Ejemplos de gráficos
    ├── ejemplo_pandas.py        # Ejemplos de análisis de datos
    ├── ejemplo_numpy.py         # Ejemplos de computación numérica
    └── ejemplo_beautifulsoup.py # Ejemplos de web scraping
```

## 🔧 Requisitos del Sistema

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Conexión a internet (para algunos ejemplos)

## 💡 ¿Por Qué Estas Librerías?

### requests 🌐
- **Propósito**: Simplifica las peticiones HTTP
- **Ideal para**: APIs, servicios web, descarga de archivos
- **Ejemplo de uso**: Obtener datos de una API REST

### matplotlib 📊
- **Propósito**: Creación de gráficos y visualizaciones
- **Ideal para**: Análisis de datos, reportes, presentaciones
- **Ejemplo de uso**: Crear gráficos de barras, líneas, histogramas

### pandas 🐼
- **Propósito**: Manipulación y análisis de datos
- **Ideal para**: Procesar archivos CSV, análisis estadístico
- **Ejemplo de uso**: Leer Excel, filtrar datos, crear reportes

### numpy 🔢
- **Propósito**: Computación numérica eficiente
- **Ideal para**: Operaciones matemáticas, arrays multidimensionales
- **Ejemplo de uso**: Cálculos matriciales, estadísticas

### beautifulsoup4 🕷️
- **Propósito**: Análisis y extracción de datos HTML/XML
- **Ideal para**: Web scraping, procesamiento de documentos
- **Ejemplo de uso**: Extraer datos de páginas web

## 🏁 Primeros Pasos

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/Eduardo3M/PythonZTH.git
   cd PythonZTH
   ```

2. **Instala las dependencias**:
   ```bash
   python instalar_librerias.py
   ```

3. **Ejecuta los ejemplos**:
   ```bash
   python ejecutar_ejemplos.py
   ```

4. **Explora los archivos de ejemplo** en la carpeta `ejemplos/`

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar los ejemplos o agregar nuevas funcionalidades, no dudes en crear un pull request.

## 📝 Licencia

Este proyecto está destinado a fines educativos y de aprendizaje.

## 🆘 Solución de Problemas

### Error de instalación
```bash
# Actualizar pip
python -m pip install --upgrade pip

# Instalar con permisos de usuario
pip install --user -r requirements.txt
```

### Error de permisos
```bash
# En Windows
python -m pip install --user -r requirements.txt

# En Linux/Mac
sudo pip install -r requirements.txt
```

### Problemas con matplotlib en servidores
```bash
# Instalar backend adicional
pip install matplotlib[agg]
```

---
💻 **¡Feliz programación con Python!** 🐍
