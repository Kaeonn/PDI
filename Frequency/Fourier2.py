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

# Calcule e visualize o espectro de Fourier
fft_result = fft2(image)
fft_magnitude = np.abs(fftshift(fft_result))
fft_phase = np.angle(fftshift(fft_result))

# Visualize a imagem original, espectro de Fourier (amplitudes) e espectro de Fourier (fases)
plt.subplot(131), plt.imshow(image, cmap="gray"), plt.title("Imagem Original")
plt.subplot(132), plt.imshow(np.log(fft_magnitude + 1), cmap="gray"), plt.title(
    "Espectro de Fourier (Amplitudes)"
)
plt.subplot(133), plt.imshow(fft_phase, cmap="gray"), plt.title(
    "Espectro de Fourier (Fases)"
)

plt.show()
