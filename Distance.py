import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):

    d = 0.1
    centers = []

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Se obtiene un histograma basada en las saturaciones de colores.

    lower_orange = np.array([1, 100, 100])
    upper_orange = np.array([21, 255, 255])

    mask = cv2.inRange(hsv, lower_orange, upper_orange) #Se crea una mascara utilizando intervalos de color naranja.
    res = cv2.bitwise_and(frame, frame, mask=mask) #se obtiene el resultado.

    kernel = np.ones((5, 5), np.uint8)   #Crea una matriz de 5x5 la cual recorrera el video,

    erosion = cv2.erode(mask, kernel, iterations=1)  #Se erosiona utilizando el kernel sobre la mascar
    dilation = cv2.dilate(mask, kernel, iterations=1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    (_, contours, hierarchy) = cv2.findContours(erosion, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Encuentra los contornos de los objetos que se ven en el filtro

    cv2.imshow('Original', frame)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)  # funcion de opencv que obtiene los contornos
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)  # Encuentra coordenadas de los contornos.
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, "Marcador", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))

            M = cv2.moments(contour)  # Se obtiene el centro de masa de los marcadores enconrados.
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            centers.append([cx, cy])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)

        if len(centers) == 2:
            D = np.linalg.norm(
                cx - cy)  # Se aplica distancia euclidiana para encontrar la distancia entre los centros de masa.
            print(D)

    cv2.imshow("Color Tracking", frame)

    cv2.imshow('Mask', mask)
    #cv2.imshow('Erosion', erosion)
    cv2.imshow('Dilation', dilation)
    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)

    # It is the difference between input image and Opening of the image
    #cv2.imshow('Tophat', tophat)
    #cv2.imshow('Blackhat', blackhat)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()