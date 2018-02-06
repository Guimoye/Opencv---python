
import numpy as np
import cv2

#cargamos la imagen
original = cv2.imread("moneda.jpg")


# cambiar tamaño de la imagen
r = 250.0 / original.shape[1]
dim = (250, int(original.shape[0] * r))
resized = cv2.resize(original, dim, interpolation=cv2.INTER_AREA)

cv2.imshow("resized", resized)




#convertimos a escala de grises
imagen = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)

#aplicar suavizado a guassiano
imagen = cv2.GaussianBlur(imagen,(5,5),0)

cv2.imshow("suavizado",imagen)

#detectamos los bordes con canny
canny = cv2.Canny(imagen,20,150)

cv2.imshow("canny",canny)

#buscamos los contornos
(_,contornos,_)= cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#mostramos el numero de monedas
print("He encontrado {} monedas".format(len(contornos)))

#dibujar contornos
cv2.drawContours(resized,contornos, -1,(0,255,0),3)
cv2.imshow("original",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
