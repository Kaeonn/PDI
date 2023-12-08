import numpy as np
import matplotlib.pyplot as plt

colunas = 20
linhas = 10
image_matrix = np.zeros([linhas, colunas])
print(image_matrix.shape)

# nome: Raphael Lopes Badaró

image_matrix[1:9, 1] = 255
image_matrix[1, 2:4] = 255
image_matrix[2:4, 4] = 255
image_matrix[4, 2:4] = 255
image_matrix[7:9, 4] = 255
image_matrix[5, 2] = 255
image_matrix[6, 3] = 255

image_matrix[1:9, 6] = 255
image_matrix[8, 6:10] = 255

image_matrix[1:9, 11] = 255
image_matrix[1, 12:14] = 255
image_matrix[2:4, 14] = 255
image_matrix[4, 12:14] = 255
image_matrix[6:8, 14] = 255
image_matrix[5, 12] = 255
image_matrix[5, 13] = 255
image_matrix[8, 12:14] = 255

plt.imshow(image_matrix, cmap="nipy_spectral")
plt.show()
