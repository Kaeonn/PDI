import cv2
import numpy as np

# Load the image
image = cv2.imread(
    r"C:\Users\rapha\OneDrive\Área de Trabalho\PDI\lena.png", cv2.IMREAD_GRAYSCALE
)

# Define various convolution kernels
kernels = {
    "Average": np.ones((3, 3), np.float32) / 9,
    "Gaussian": cv2.getGaussianKernel(3, 0),
    "Laplacian": np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], np.float32),
    "SobelX": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32),
    "SobelY": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], np.float32),
}

# Apply convolution for each kernel
convolutions = {}
for kernel_name, kernel in kernels.items():
    convolved_image = cv2.filter2D(image, -1, kernel)
    convolutions[kernel_name] = convolved_image

# Display the original and convolved images
cv2.imshow("Original Image", image)

for kernel_name, convolved_image in convolutions.items():
    cv2.imshow(f"Convolved Image ({kernel_name} Kernel)", convolved_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
