"""
Ejemplo básico de la librería beautifulsoup4
Para web scraping y análisis de HTML
"""

from bs4 import BeautifulSoup
import requests

def ejemplo_beautifulsoup():
    """Ejemplos básicos de uso de la librería beautifulsoup4"""
    
    print("🕷️ Ejemplos con la librería beautifulsoup4")
    print("=" * 40)
    
    # Ejemplo 1: Analizar HTML básico
    print("\n1. Analizando HTML básico:")
    
    html_basico = """
    <html>
        <head>
            <title>Mi Primera Página</title>
        </head>
        <body>
            <h1>¡Bienvenido!</h1>
            <p class="descripcion">Esta es una página de ejemplo.</p>
            <p>Aquí hay otro párrafo.</p>
            <ul>
                <li>Elemento 1</li>
                <li>Elemento 2</li>
                <li>Elemento 3</li>
            </ul>
            <a href="https://python.org">Enlace a Python</a>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_basico, 'html.parser')
    
    print(f"   Título: {soup.title.string}")
    print(f"   Encabezado H1: {soup.h1.string}")
    
    # Encontrar todos los párrafos
    parrafos = soup.find_all('p')
    print(f"   Párrafos encontrados: {len(parrafos)}")
    for i, p in enumerate(parrafos, 1):
        print(f"     {i}. {p.get_text()}")
    
    # Encontrar elementos por clase
    descripcion = soup.find('p', class_='descripcion')
    print(f"   Párrafo con clase 'descripcion': {descripcion.get_text()}")
    
    # Encontrar enlaces
    enlaces = soup.find_all('a')
    print(f"   Enlaces encontrados:")
    for enlace in enlaces:
        print(f"     Texto: {enlace.get_text()}")
        print(f"     URL: {enlace.get('href')}")
    
    # Ejemplo 2: Extraer elementos de una lista
    print("\n2. Extrayendo elementos de lista:")
    
    elementos_lista = soup.find_all('li')
    print(f"   Elementos de lista:")
    for i, elemento in enumerate(elementos_lista, 1):
        print(f"     {i}. {elemento.get_text()}")

def ejemplo_web_scraping():
    """Ejemplo de web scraping real (con precaución)"""
    
    print("\n" + "=" * 50)
    print("🌐 Ejemplo de web scraping")
    print("=" * 50)
    
    print("\n⚠️ Nota: Este ejemplo usa httpbin.org, un servicio de prueba.")
    print("Siempre respeta los términos de servicio y robots.txt de los sitios web.")
    
    try:
        # Usar httpbin.org para obtener HTML de prueba
        url = "https://httpbin.org/html"
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            print(f"\n✅ Página cargada exitosamente")
            print(f"   URL: {url}")
            print(f"   Código de estado: {response.status_code}")
            
            # Extraer título
            titulo = soup.find('title')
            if titulo:
                print(f"   Título de la página: {titulo.get_text()}")
            
            # Extraer encabezados
            encabezados = soup.find_all(['h1', 'h2', 'h3'])
            if encabezados:
                print(f"   Encabezados encontrados:")
                for h in encabezados:
                    print(f"     {h.name.upper()}: {h.get_text()}")
            
            # Extraer párrafos
            parrafos = soup.find_all('p')
            if parrafos:
                print(f"   Párrafos encontrados: {len(parrafos)}")
                for i, p in enumerate(parrafos[:3], 1):  # Solo los primeros 3
                    print(f"     {i}. {p.get_text()[:100]}...")
            
        else:
            print(f"❌ Error al cargar la página: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")

def ejemplo_parsing_avanzado():
    """Ejemplos más avanzados de parsing HTML"""
    
    print("\n" + "=" * 50)
    print("🔍 Parsing avanzado con BeautifulSoup")
    print("=" * 50)
    
    html_complejo = """
    <html>
        <body>
            <div class="contenedor">
                <article id="articulo1" data-categoria="tecnologia">
                    <h2>Título del Artículo 1</h2>
                    <p class="autor">Por: Juan Pérez</p>
                    <p class="fecha">2023-12-01</p>
                    <div class="contenido">
                        <p>Contenido del artículo sobre tecnología...</p>
                    </div>
                    <div class="tags">
                        <span class="tag">Python</span>
                        <span class="tag">Web Scraping</span>
                    </div>
                </article>
                
                <article id="articulo2" data-categoria="ciencia">
                    <h2>Título del Artículo 2</h2>
                    <p class="autor">Por: María García</p>
                    <p class="fecha">2023-12-02</p>
                    <div class="contenido">
                        <p>Contenido del artículo sobre ciencia...</p>
                    </div>
                    <div class="tags">
                        <span class="tag">Investigación</span>
                        <span class="tag">Datos</span>
                    </div>
                </article>
            </div>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html_complejo, 'html.parser')
    
    print("\n1. Extrayendo información de artículos:")
    
    articulos = soup.find_all('article')
    for i, articulo in enumerate(articulos, 1):
        titulo = articulo.find('h2').get_text()
        autor = articulo.find('p', class_='autor').get_text()
        fecha = articulo.find('p', class_='fecha').get_text()
        categoria = articulo.get('data-categoria')
        
        print(f"\n   Artículo {i}:")
        print(f"     Título: {titulo}")
        print(f"     Autor: {autor}")
        print(f"     Fecha: {fecha}")
        print(f"     Categoría: {categoria}")
        
        # Extraer tags
        tags = articulo.find_all('span', class_='tag')
        if tags:
            tags_texto = [tag.get_text() for tag in tags]
            print(f"     Tags: {', '.join(tags_texto)}")
    
    print("\n2. Búsqueda con selectores CSS:")
    
    # Usar selectores CSS
    titulos_css = soup.select('article h2')
    print(f"   Títulos encontrados con CSS selector:")
    for titulo in titulos_css:
        print(f"     - {titulo.get_text()}")
    
    # Encontrar artículos de tecnología
    tech_articles = soup.select('article[data-categoria="tecnologia"]')
    print(f"   Artículos de tecnología: {len(tech_articles)}")
    
    print("\n3. Navegación por el árbol HTML:")
    
    primer_articulo = soup.find('article')
    if primer_articulo:
        print(f"   Primer artículo ID: {primer_articulo.get('id')}")
        
        # Encontrar el siguiente hermano
        siguiente = primer_articulo.find_next_sibling('article')
        if siguiente:
            print(f"   Siguiente artículo ID: {siguiente.get('id')}")
        
        # Encontrar elementos padre
        contenedor = primer_articulo.parent
        print(f"   Clase del contenedor padre: {contenedor.get('class')}")

if __name__ == "__main__":
    ejemplo_beautifulsoup()
    ejemplo_web_scraping()
    ejemplo_parsing_avanzado()