from flask import Flask, request, jsonify, render_template
from tensorflow.python.keras.models import load_model
from tensorflow import keras
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Cargar el modelo .keras
model = keras.models.load_model("my_model.keras")

@app.route('/')
def home():
    return render_template('index.html')  # Interfaz web para subir imágenes

@app.route('/predict', methods=['POST'])
def predict():
    # Verificar si se envió una imagen
    if 'file' not in request.files:
        return jsonify({'error': 'No se proporcionó ninguna imagen'}), 400
    
    file = request.files['file']
    
    # Leer la imagen y convertirla a escala de grises
    image = Image.open(file.stream).convert('L')
    
    # Redimensionar la imagen a 28x28 píxeles (tamaño de MNIST)
    image = image.resize((28, 28))
    
    # Convertir la imagen a un array de numpy y normalizarla
    image_array = np.array(image) / 255.0
    image_array = image_array.reshape(1, 28, 28, 1)  # Ajustar la forma para el modelo
    
    # Hacer la predicción
    prediction = model.predict(image_array)
    predicted_class = np.argmax(prediction, axis=1)[0]
    confidence = float(np.max(prediction))
    
    # Devolver la predicción como respuesta
    return jsonify({
        'predicted_class': int(predicted_class),
        'confidence': confidence
    })

if __name__ == '__main__':
    app.run(debug=True)