import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create an image with a white background and a sinc function square

# Define the image dimensions
width, height = 512, 512

# Create a white background image
white_image = np.ones((height, width), dtype=np.uint8) * 255

# Create a grid of coordinates
x, y = np.meshgrid(np.linspace(-1, 1, width), np.linspace(-1, 1, height))

# Calculate the sinc function
sinc_function = np.sinc(10 * np.sqrt(x**2 + y**2))

# Scale the sinc function to the range [0, 255]
scaled_sinc = (
    (sinc_function - np.min(sinc_function)) / np.ptp(sinc_function) * 255
).astype(np.uint8)

# Place the scaled sinc function in the center of the white image
x_offset = (width - scaled_sinc.shape[1]) // 2
y_offset = (height - scaled_sinc.shape[0]) // 2
white_image[
    y_offset : y_offset + scaled_sinc.shape[0],
    x_offset : x_offset + scaled_sinc.shape[1],
] = scaled_sinc

# Display the sinc function image
cv2.imshow("Sinc Function Image", white_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the sinc function image
cv2.imwrite("sinc_image.png", white_image)

# Perform Fourier Transform and visualize the 3D spectrum

# Load the image
image = cv2.imread("sinc_image.png", cv2.IMREAD_GRAYSCALE)

# Perform Fourier Transform
f_transform = np.fft.fft2(image)
f_transform_shifted = np.fft.fftshift(f_transform)

# Compute the magnitude of the Fourier Transform
magnitude_spectrum = np.log(np.abs(f_transform_shifted) + 1)

# Create a 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

# Create a grid of coordinates
x, y = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))

# Plot the 3D surface
ax.plot_surface(x, y, magnitude_spectrum, cmap="viridis")

# Set labels for the axes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Magnitude Spectrum")

plt.show()
