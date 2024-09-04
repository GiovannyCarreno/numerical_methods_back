# Usar una imagen base de Python 3.12.3
FROM python:3.12.4

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copiar los archivos de tu proyecto al directorio de trabajo en la imagen
COPY . .

# Instalar las dependencias de tu proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000 para que Flask pueda recibir solicitudes
EXPOSE 5000

# Definir el comando por defecto para ejecutar tu aplicación Flask
CMD ["python", "servicios.py"]
