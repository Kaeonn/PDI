import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fftshift, fft2


# Função para criar uma imagem com um quadrado branco
def create_square_image(size, square_size):
    image = np.zeros(size, dtype=np.uint8)
    y, x = size
    x_center, y_center = x // 2, y // 2
    x_start, x_end = x_center - square_size // 2, x_center + square_size // 2
    y_start, y_end = y_center - square_size // 2, y_center + square_size // 2
    image[y_start:y_end, x_start:x_end] = 255
    return image


# Tamanho da imagem (512x512 pixels)
image_size = (512, 512)

# Tamanho do quadrado branco
square_size = 100

# Crie uma imagem com um quadrado branco
image = create_square_image(image_size, square_size)

# Aplicar uma rotação de 40 graus
angle = 40
rotation_matrix = cv2.getRotationMatrix2D(
    (image_size[0] / 2, image_size[1] / 2), angle, 1
)
image_rotated = cv2.warpAffine(image, rotation_matrix, image_size)

# Aplicar uma translação nos eixos x e y
translation_x, translation_y = 50, 50
translation_matrix = np.float32([[1, 0, translation_x], [0, 1, translation_y]])
image_translated = cv2.warpAffine(image, translation_matrix, image_size)

# Aplicar um zoom na imagem
zoom_factor = 2
zoomed_image = cv2.resize(
    image, (image_size[0] * zoom_factor, image_size[1] * zoom_factor)
)

# Calcule e visualize o espectro de Fourier das imagens após as transformações
images = [image, image_rotated, image_translated, zoomed_image]
titles = ["Original", "Rotated", "Translated", "Zoomed"]

for i, img in enumerate(images):
    fft_result = fft2(img)
    fft_magnitude = np.abs(fftshift(fft_result))
    fft_phase = np.angle(fftshift(fft_result))

    plt.subplot(2, 4, i + 1), plt.imshow(img, cmap="gray"), plt.title(titles[i])
    plt.subplot(2, 4, i + 5), plt.imshow(
        np.log(fft_magnitude + 1), cmap="gray"
    ), plt.title("Espectro de Fourier (Amplitudes)")

plt.show()
