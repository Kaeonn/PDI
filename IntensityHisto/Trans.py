import cv2
import numpy as np
import matplotlib.pyplot as plt


# Function to apply Logarithmic Transformation
def logarithmic_transformation(image, c):
    if image is None:
        return None

    # Ensure the image is in grayscale
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Normalize the pixel values to the range [0, 1]
    normalized_image = image.astype(np.float32) / 255.0

    # Apply the logarithmic transformation
    result = c * np.log1p(normalized_image)

    # Scale the result back to the range [0, 255]
    result = (result * 255).astype(np.uint8)

    return result


# Function to apply Power (Gamma) Transformation
def gamma_transformation(image, gamma):
    if image is None:
        return None

    # Ensure the image is in grayscale
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply the power (gamma) transformation
    result = np.power(image, gamma)

    return result


# Function to represent each bit plane
def bit_planes_representation(image):
    if image is None:
        return None

    # Ensure the image is in grayscale
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    bit_planes = [((image >> i) & 1) * 255 for i in range(8)]

    return bit_planes


# Function to implement Histogram Equalization
def histogram_equalization(image):
    if image is None:
        return None

    # Ensure the image is in grayscale
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    equalized = cv2.equalizeHist(image)

    return equalized


def main():
    # Read the image
    img = cv2.imread(
        r"C:\Users\rapha\OneDrive\Área de Trabalho\PDI\lena.png", cv2.IMREAD_GRAYSCALE
    )

    # Check if the image was loaded successfully
    if img is None:
        print("Error: Image not found or could not be loaded.")
        return

    # Define parameters
    c_log = 1
    gamma = 1.5

    # Task 1: Logarithmic Transformation
    log_transformed = logarithmic_transformation(img, c_log)

    # Task 2: Power (Gamma) Transformation
    gamma_transformed = gamma_transformation(img, gamma)

    # Task 3: Bit Planes Representation
    bit_planes = bit_planes_representation(img)

    # Task 4: Histogram Equalization
    equalized_image = histogram_equalization(img)

    # Display the results
    plt.figure(figsize=(15, 10))

    plt.subplot(4, 3, 1), plt.imshow(img, cmap="gray"), plt.title("Original Image")
    plt.subplot(4, 3, 2), plt.imshow(log_transformed, cmap="gray"), plt.title(
        "Logarithmic Transformation"
    )
    plt.subplot(4, 3, 3), plt.imshow(gamma_transformed, cmap="gray"), plt.title(
        f"Gamma Transformation (γ={gamma})"
    )

    for i, plane in enumerate(bit_planes):
        plt.subplot(4, 3, i + 4)
        plt.imshow(plane, cmap="gray")
        plt.title(f"Bit Plane {i}")

    plt.subplot(4, 3, 8), plt.imshow(equalized_image, cmap="gray"), plt.title(
        "Equalized Image"
    )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
