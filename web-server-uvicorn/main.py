import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list_one():
  return [1,2,3]

# @app.get('/contact')
# def get_list_two():
#   return {'name' : 'Platzi'}

@app.get('/contact', response_class=HTMLResponse)
def get_list():
  return """
   <h1>Aja</h1>
   <p>Y usted que piensa Full Stack</p>
   <p>Porque no se conecto a la Dayli</p>
   <p>Las horas no las has actualizado Cristian, <br>
   Mario te va poner una accion de personal...</p>
"""

def run():
  store.get_categories()

if __name__=='__main__':
   run()
