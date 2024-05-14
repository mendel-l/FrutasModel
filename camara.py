import cv2

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

            cv2.imshow('Camera Feed', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

# camera_capture()  # Uncomment to run the function
