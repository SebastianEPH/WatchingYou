import cv2
import numpy as np

class Config:
    def __init__(self):
        self.path_archivoEntrenado = "haarcascade_frontalface_default.xml"  # Archivo clasificador
        self.path_imagenVerificar = "persons.png"

cap = cv2.VideoCapture(0)
faceClassif = cv2.CascadeClassifier(Config().path_archivoEntrenado)

while True:
    ret, frame = cap.read() #Obtiene frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceClassif.detectMultiScale(gray,
                                         scaleFactor=1.3,  # Reducción de imagen
                                         minNeighbors=5  # Espeficica el número mínimo de cuadros delimitadores
                                         )
    for x,y,w,h in faces:
        cv2.rectangle(frame,
                      (x, y),
                      (x + w, y + h),
                      (0, 255, 0),
                      2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
