import numpy as np
import matplotlib.pyplot as plt

colunas = 10
linhas = 5
image_matrix = np.zeros([linhas, colunas])
print(image_matrix.shape)

# Acessando um pixel
image_matrix[0, 0] = 255
# Acessando uma linha (Primeira linha da matrix)
image_matrix[0, :] = 255
# Acessando mais de uma linha (Quarta e quinta linha da matrix)
image_matrix[3:5, :] = 255
# Acessando uma coluna (Ultima coluna)
image_matrix[:, 9] = 120

plt.imshow(image_matrix, cmap="gray")
plt.show()
