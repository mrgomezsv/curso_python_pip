# Usar la imagen oficial de Python 3.9 como imagen base
FROM python:3.9

# Establecer /app como el directorio de trabajo
WORKDIR /app

# Copiar el archivo requirements.txt al directorio de trabajo
COPY requirements.txt /app/requirements.txt

# Instalar las dependencias de Python especificadas en requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiar el resto de los archivos de la aplicación al directorio de trabajo
COPY . app/

# Ejecutar un bucle infinito para mantener el contenedor en ejecución
CMD bash -c "while true; do sleep 1; done"
