import cv2
import numpy as np

class Config:
    def __init__(self):
        self.path_archivoEntrenado = "haarcascade_frontalface_default.xml"  # Archivo clasificador
        self.path_imagenVerificar = "personas.jpg"

faceClassif = cv2.CascadeClassifier(Config().path_archivoEntrenado)
#Obtiene imagen
image = cv2.imread(Config().path_imagenVerificar)
# Convierte la imagen en tonos grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceClassif.detectMultiScale(gray,              # imagen en escala de grises
                                     scaleFactor=1.1,   # Reducción de imagen
                                     minNeighbors=5,    # Espeficica el número mínimo de cuadros delimitadores
                                     minSize=(30, 30),  # Recuadro mínimo de rostro.
                                     maxSize=(200, 200))# Recuadro maximo por rostro.

for x,y,w,h in faces:
    cv2.rectangle(image,
                  (x, y),
                  (x + w, y + h),
                  (0, 255, 0),
                  2)




cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

