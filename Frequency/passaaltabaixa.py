import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fftshift, fft2, ifft2

# Carregue a imagem (substitua 'imagem.png' pelo caminho da imagem)
image = cv2.imread("imagem.png", cv2.IMREAD_GRAYSCALE)

# Calcule o espectro de Fourier da imagem
fft_result = fft2(image)
fft_magnitude = np.abs(fftshift(fft_result))


# Função para criar filtros passa-baixa (ideal, Butterworth e Gaussiano)
def create_lowpass_filter(filter_type, image_size, D0, n=1):
    rows, cols = image_size
    center_x, center_y = rows // 2, cols // 2
    x, y = np.meshgrid(np.arange(cols), np.arange(rows))
    distances = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)

    if filter_type == "ideal":
        H = (distances <= D0).astype(float)
    elif filter_type == "butterworth":
        H = 1 / (1 + (distances / D0) ** (2 * n))
    elif filter_type == "gaussian":
        H = np.exp(-(distances**2) / (2 * D0**2))

    return H


# Defina os parâmetros dos filtros
D0 = 50  # Frequência de corte
n = 2  # Parâmetro de ordem (apenas para Butterworth)

# Aplique filtros passa-baixa e visualize os resultados
filter_types = ["ideal", "butterworth", "gaussian"]
filtered_images = []

for filter_type in filter_types:
    lowpass_filter = create_lowpass_filter(filter_type, image.shape, D0, n)
    filtered_image = np.abs(ifft2(fft_result * lowpass_filter))
    filtered_images.append(filtered_image)

# Visualize as imagens (imagem original, espectro de Fourier, imagens filtradas)
titles = [
    "Original",
    "Spectrum",
    "Ideal Filter",
    "Butterworth Filter",
    "Gaussian Filter",
]
images = [image, np.log(fft_magnitude + 1)] + filtered_images

for i in range(len(images)):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], cmap="gray"), plt.title(titles[i])

plt.show()


# Função para criar filtros passa-alta (ideal, Butterworth e Gaussiano)
def create_highpass_filter(filter_type, image_size, D0, n=1):
    rows, cols = image_size
    center_x, center_y = rows // 2, cols // 2
    x, y = np.meshgrid(np.arange(cols), np.arange(rows))
    distances = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)

    if filter_type == "ideal":
        H = (distances > D0).astype(float)
    elif filter_type == "butterworth":
        H = 1 / (1 + (D0 / distances) ** (2 * n))
    elif filter_type == "gaussian":
        H = 1 - np.exp(-(distances**2) / (2 * D0**2))

    return H


# Defina os parâmetros dos filtros passa-alta
D0_highpass = 50  # Frequência de corte
n_highpass = 2  # Parâmetro de ordem (apenas para Butterworth)

# Aplique filtros passa-alta e visualize os resultados
highpass_filter_types = ["ideal", "butterworth", "gaussian"]
filtered_highpass_images = []

for filter_type in highpass_filter_types:
    highpass_filter = create_highpass_filter(
        filter_type, image.shape, D0_highpass, n_highpass
    )
    filtered_highpass_image = np.abs(ifft2(fft_result * highpass_filter))
    filtered_highpass_images.append(filtered_highpass_image)

# Visualize as imagens (imagem original, espectro de Fourier, imagens filtradas)
titles_highpass = [
    "Original",
    "Spectrum",
    "Ideal Highpass Filter",
    "Butterworth Highpass Filter",
    "Gaussian Highpass Filter",
]
images_highpass = [image, np.log(fft_magnitude + 1)] + filtered_highpass_images

for i in range(len(images_highpass)):
    plt.subplot(2, 3, i + 1), plt.imshow(images_highpass[i], cmap="gray"), plt.title(
        titles_highpass[i]
    )

plt.show()
