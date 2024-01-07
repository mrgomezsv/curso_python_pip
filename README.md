# Game Project

Para correr el juego debes seguir las siguintes instrucciones en la terminal:

```sh
cd game
python3 main.py
```

# App Project
```sh
git clone https://github.com/mrgomezsv/curso_python_pip.git
cd app
python -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

# App Project in Docker
```sh
Para crear el contenedor
docker compose build

Para Correr el contenedor
docker compose up -d

Para verificar el contenedor
docker compose ps

Para ingresar al contenedor
docker compose exec app-csv bash

Para bajar la aplicacion
docker compose down
```

# Use API in Python
```sh
python -m venv env
.\env\Scripts\activate
pip3 install -r requirements.txt
python main.py
```