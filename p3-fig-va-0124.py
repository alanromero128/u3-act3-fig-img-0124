import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Alan Romero NC 0124
print("Alan Romero NC 0124")
print("UIII Act 3 colocar puntos a una imagen en blanco y negro")
mi_imagen= cv2.imread('don.png')
plt.imshow(mi_imagen)
plt.title('Don Ramon y Alan Romero')
plt.show()
print("-+-+-+- Puntos en la imagen-+-+-+-+-")
plt.imshow(mi_imagen)
plt.title('Don Ramon y Alan Romero')
x=[100,200,50,120,113]
y=[250,200,250,120,104]
plt.scatter(x,y,s=20,c='red')
plt.show()
