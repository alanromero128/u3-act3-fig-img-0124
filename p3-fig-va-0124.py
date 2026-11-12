import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Alan Romero NC 0124
print("Alan Romero NC 0124")
print("UIII Act 3 colocar puntos a una imagen en blanco y negro")
mi_imagendr= cv2.imread('don.png')
plt.imshow(mi_imagendr)
plt.title('Don Ramon y Alan Romero')
plt.show()
print("-+-+-+- Puntos en la imagen-+-+-+-+-")
plt.imshow(mi_imagendr)
plt.title('Don Ramon y Alan Romero')
x=[100,200,50,120,113]
y=[250,200,250,120,104]
plt.scatter(x,y,s=20,c='red')
plt.show()

print("-+-+-+-+ Cuadro azul en la imagen+-+-+-+")
img_Ramon = cv2.imread('don.png')
plt.imshow(img_Ramon)
x = [50, 230, 230, 50, 50]
y = [40, 40, 220, 220, 40]
plt.plot(x, y, c='blue')
plt.show()
print("-+-+-+-+ Circulo verde en la imagen ")
I = cv2.imread('don.png')
plt.imshow(I)
N = 30
x = np.zeros((N + 1,))
y = np.zeros((N + 1,))
(xc, yc) = (145, 130)
r = 95
for i in range(N + 1):
    t = 2 * np.pi / N * i
    x[i] = xc + r * np.cos(t)
    y[i] = yc + r * np.sin(t)
plt.plot(x, y, c='green')
plt.show()

