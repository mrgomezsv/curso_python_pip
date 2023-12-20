import requests

# Definir la función get_categories
def get_categories():

   # Realizar una solicitud GET a la URL proporcionada y guardar la respuesta en la variable r
   #https://fakeapi.platzi.com/
   r = requests.get('https://api.escuelajs.co/api/v1/users')

   # Imprimir el código de estado HTTP de la respuesta
   print(r.status_code)

   # Imprimir el cuerpo de la respuesta como una cadena de texto
   print(r.text)

   # Imprimir el tipo de datos del cuerpo de la respuesta
   print(type(r.text))

   # Convertir el cuerpo de la respuesta en un objeto JSON y guardarlo en la variable category
   category = r.json()

   # Iterar sobre cada elemento en el objeto JSON category
   for category in category:

       # Imprimir el valor del campo 'name' de cada categoría en el objeto JSON
       print(category['email'])
