- `app.py`: Archivo principal de la aplicación Flask.
- `my_model.keras`: Modelo de red neuronal entrenado.
- `requirements.txt`: Lista de dependencias del proyecto.
- `templates/index.html`: Plantilla HTML para la interfaz web.

## Requisitos

- Python 3.x
- Flask 3.1.0
- TensorFlow 2.18.0
- NumPy 2.0.2
- Pillow 11.1.0

## Instalación

1. Clona este repositorio.
2. Instala las dependencias utilizando `pip`:

   ```sh
   python -m venv --copies /opt/venv && . /opt/venv/bin/activate && pip install -r requirements.txt
   ```

## Uso

1. Ejecuta la aplicación Flask:

   ```sh
   python app.py
   ```

2. Abre tu navegador web y ve a `http://127.0.0.1:5000`.
3. Sube una imagen de un dígito (28x28 píxeles) para clasificarla.

## Estructura del Código

- [app.py](http://_vscodecontentref_/4): Contiene la lógica de la aplicación Flask, incluyendo las rutas para la interfaz web y la predicción.
- [index.html](http://_vscodecontentref_/5): Contiene la interfaz web para subir imágenes y mostrar los resultados de la clasificación.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
