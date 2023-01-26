# Esta libreria se debe instalar en el entorno virtual en la carpeta env. Nombre de la libreria: requests
import requests

def get_categories():
  r = requests.get("https://api.escuelajs.co/api/v1/categories")
  print(r.status_code)
  print(r.text)
  print(type(r.text))
  categories = r.json()
  print(categories)
  print(type(categories))

  for category in categories:
    print(category["name"])