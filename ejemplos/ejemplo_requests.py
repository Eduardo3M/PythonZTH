"""
Ejemplo básico de la librería requests
Para realizar peticiones HTTP y trabajar con APIs
"""

import requests

def ejemplo_requests():
    """Ejemplos básicos de uso de la librería requests"""
    
    print("🌐 Ejemplos con la librería requests")
    print("=" * 40)
    
    # Ejemplo 1: Obtener información de una API pública
    print("\n1. Obteniendo información sobre un usuario de GitHub:")
    try:
        response = requests.get("https://api.github.com/users/octocat")
        if response.status_code == 200:
            data = response.json()
            print(f"   Nombre: {data.get('name', 'N/A')}")
            print(f"   Seguidores: {data.get('followers', 0)}")
            print(f"   Repositorios públicos: {data.get('public_repos', 0)}")
        else:
            print(f"   Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"   Error de conexión: {e}")
    
    # Ejemplo 2: Verificar el estado de una página web
    print("\n2. Verificando el estado de una página web:")
    try:
        response = requests.get("https://httpbin.org/status/200")
        print(f"   Código de estado: {response.status_code}")
        print(f"   {'✅ Página accesible' if response.status_code == 200 else '❌ Página no accesible'}")
    except requests.exceptions.RequestException as e:
        print(f"   Error de conexión: {e}")
    
    # Ejemplo 3: Enviar datos con POST
    print("\n3. Enviando datos con POST:")
    try:
        data = {"mensaje": "Hola desde Python!", "usuario": "principiante"}
        response = requests.post("https://httpbin.org/post", json=data)
        if response.status_code == 200:
            print("   ✅ Datos enviados correctamente")
            resultado = response.json()
            print(f"   Datos recibidos por el servidor: {resultado.get('json', {})}")
        else:
            print(f"   Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"   Error de conexión: {e}")

if __name__ == "__main__":
    ejemplo_requests()