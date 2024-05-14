import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model

# Cargar el modelo entrenado
model = load_model('models/modelo_frutas.h5')

def find_working_camera_index():
    index = 0
    while True:
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            cap.release()
            return index
        index += 1
        if index > 10:  # Un número razonable de intentos
            return -1

def camera_capture():
    camera_index = find_working_camera_index()
    if camera_index == -1:
        print("No se encontró ninguna cámara funcional.")
        return

    cap = cv2.VideoCapture(camera_index)

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("No se pudo recibir el frame. Terminando...")
                break

            # Preprocesar el frame para el modelo
            processed_frame = cv2.resize(frame, (180, 180))  # Redimensionar a 180x180
            processed_frame = processed_frame / 255.0  # Normalizar los píxeles
            processed_frame = processed_frame.reshape(1, 180, 180, 3)  # Cambiar la forma para el modelo

            # Predicción del modelo
            prediction = model.predict(processed_frame)
            class_index = tf.argmax(prediction, axis=1).numpy()[0]
            classes = ['buen estado', 'mal estado', 'inmaduro']
            predicted_class = classes[class_index]

            # Mostrar la clase predicha en el feed de la cámara
            cv2.putText(frame, f"Clase: {predicted_class}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            
            cv2.imshow('Camera Feed', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

# Llamar a la función para iniciar la captura y clasificación
camera_capture()
