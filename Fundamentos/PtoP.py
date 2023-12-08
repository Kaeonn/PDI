# Import libs
import numpy as np
from PIL import Image
from numpy import asarray, negative
import matplotlib.pyplot as plt


# Function to turn neg
def negative():
    # Open Img Lena
    imageLena = Image.open(r"C:\Users\rapha\OneDrive\Área de Trabalho\PDI\lena.png")

    # Convert the image to an numpy array

    npImageLena = np.array(imageLena)

    # subtract the maximum pixel value from each pixel
    negativeImageLena = 255 - npImageLena

    # Open Img Cameraman
    imageCameraman = Image.open(
        r"C:\Users\rapha\OneDrive\Área de Trabalho\PDI\cameraman.tif"
    )

    # Convert the image to an numpy array
    npImageCameraman = np.array(imageCameraman)

    # subtract the maximum pixel value from each pixel
    negativeCameraman = 255 - npImageCameraman

    # Open image house
    imageHouse = Image.open(r"C:\Users\rapha\OneDrive\Área de Trabalho\PDI\house.tif")

    # Convert image house to an numpy array
    npImageHouse = np.array(imageHouse)

    # Subtract pixels
    negativeImageHouse = 255 - npImageHouse

    # Plot all three images
    fig = plt.figure()
    ax1 = plt.subplot(4, 2, 1)
    ax2 = plt.subplot(4, 2, 2)
    ax3 = plt.subplot(3, 2, 3)
    ax4 = plt.subplot(3, 2, 4)
    ax5 = plt.subplot(3, 2, 5)
    ax6 = plt.subplot(3, 2, 6)

    ax1.title.set_text("Original image")
    ax2.title.set_text("Negative Image")
    ax3.title.set_text("Original image")
    ax4.title.set_text("Negative Image")
    ax5.title.set_text("Original image")
    ax6.title.set_text("Negative Image")

    im1 = ax1.imshow(npImageLena, cmap="gray")
    im2 = ax2.imshow(negativeImageLena, cmap="gray")
    im3 = ax3.imshow(imageCameraman, cmap="gray")
    im4 = ax4.imshow(negativeCameraman, cmap="gray")
    im5 = ax5.imshow(npImageHouse, cmap="gray")
    im6 = ax6.imshow(negativeImageHouse, cmap="gray")
    plt.show()


def intensity():
    # Open Lena
    imageLena = Image.open(r"C:\Users\rapha\OneDrive\Área de Trabalho\PDI\lena.png")

    # Transform it to an numpy array
    npImageLena = np.array(imageLena)

    # Divide the array and assignt it to the new variable
    npImageLenaLowPixel = (npImageLena / 2).astype(int)

    # Open Img Cameraman
    imageCameraman = Image.open(
        r"C:\Users\rapha\OneDrive\Área de Trabalho\PDI\cameraman.tif"
    )

    # Convert the image to an numpy array
    npImageCameraman = np.array(imageCameraman)

    # Divide the array and assignt it to the new variable
    npImageCameramanLowPixel = (npImageCameraman / 2).astype(int)

    # Open image house
    imageHouse = Image.open(r"C:\Users\rapha\OneDrive\Área de Trabalho\PDI\house.tif")

    # Convert image house to an numpy array
    npImageHouse = np.array(imageHouse)

    # Divide the array and assignt it to the new variable
    npImageHouseLowPixel = (npImageHouse / 2).astype(int)

    fig = plt.figure()
    ax1 = plt.subplot(4, 2, 1)
    ax2 = plt.subplot(4, 2, 2)
    ax3 = plt.subplot(3, 2, 3)
    ax4 = plt.subplot(3, 2, 4)
    ax5 = plt.subplot(3, 2, 5)
    ax6 = plt.subplot(3, 2, 6)

    ax1.title.set_text("Original image")
    ax2.title.set_text("Low Intensity Image")
    ax3.title.set_text("Original image")
    ax4.title.set_text("Low Intensity Image")
    ax5.title.set_text("Original image")
    ax6.title.set_text("Low Intensity Image")

    im1 = ax1.imshow(npImageLena, cmap="gray")
    im2 = ax2.imshow(npImageLenaLowPixel, cmap="gray")
    im3 = ax3.imshow(npImageCameraman, cmap="gray")
    im4 = ax4.imshow(npImageCameramanLowPixel, cmap="gray")
    im5 = ax5.imshow(npImageHouse, cmap="gray")
    im6 = ax6.imshow(npImageHouseLowPixel, cmap="gray")
    plt.show()


def bSquare():
    # Open Lena
    # Abrir as images
    imageLena = Image.open(r"C:\Users\rapha\OneDrive\Área de Trabalho\PDI\lena.png")
    imageCameraman = Image.open(
        r"C:\Users\rapha\OneDrive\Área de Trabalho\PDI\cameraman.tif"
    )
    imageHouse = Image.open(r"C:\Users\rapha\OneDrive\Área de Trabalho\PDI\house.tif")

    # Converter as imagens para numpy array
    # e tranforma-las em negativa
    # Lena
    npImageLena = np.array(imageLena)
    npImageLena[0:10, 0:10] = 255
    npImageLena[0:10, 290:301] = 255
    npImageLena[290:301, 0:10] = 255
    npImageLena[290:301, 290:301] = 255

    # Cameraman
    npImageCameraman = np.array(imageCameraman)
    npImageCameraman[0:10, 0:10] = 255
    npImageCameraman[0:10, 503:513] = 255
    npImageCameraman[503:513, 0:10] = 255
    npImageCameraman[503:513, 503:513] = 255

    # House
    npImageHouse = np.array(imageHouse)
    npImageHouse[0:10, 0:10] = 255
    npImageHouse[0:10, 590:601] = 255
    npImageHouse[590:601, 0:10] = 255
    npImageHouse[590:601, 590:601] = 255

    # Plotar imagens
    fig3 = plt.figure()
    ax1 = plt.subplot(1, 3, 1)
    ax3 = plt.subplot(1, 3, 2)
    ax5 = plt.subplot(1, 3, 3)

    ax1.title.set_text("whiteSquare image")
    ax3.title.set_text("whiteSquare image")
    ax5.title.set_text("whiteSquare image")

    im1 = ax1.imshow(npImageLena, cmap="gray")
    im3 = ax3.imshow(npImageCameraman, cmap="gray")
    im5 = ax5.imshow(npImageHouse, cmap="gray")
    plt.show()


def wSquare():
    # Abrir as images
    imageLena = Image.open(r"C:\Users\rapha\OneDrive\Área de Trabalho\PDI\lena.png")
    imageCameraman = Image.open(
        r"C:\Users\rapha\OneDrive\Área de Trabalho\PDI\cameraman.tif"
    )
    imageHouse = Image.open(r"C:\Users\rapha\OneDrive\Área de Trabalho\PDI\house.tif")

    # Converter as imagens para numpy array
    # e tranforma-las em negativa
    # Lena
    npImageLena = np.array(imageLena)
    npImageLena[144:159, 144:159] = 0

    # Cameraman
    npImageCameraman = np.array(imageCameraman)
    npImageCameraman[249:264, 249:264] = 0

    # House
    npImageHouse = np.array(imageHouse)
    npImageHouse[293:308, 293:308] = 0

    # Plotar imagens
    fig4 = plt.figure()
    ax1 = plt.subplot(1, 3, 1)
    ax3 = plt.subplot(1, 3, 2)
    ax5 = plt.subplot(1, 3, 3)

    ax1.title.set_text("blackSquare image")
    ax3.title.set_text("blackSquare image")
    ax5.title.set_text("blackSquare image")

    im1 = ax1.imshow(npImageLena, cmap="gray")
    im3 = ax3.imshow(npImageCameraman, cmap="gray")
    im5 = ax5.imshow(npImageHouse, cmap="gray")
    plt.show()


if __name__ == "__main__":
    negative()
    intensity()
    bSquare()
    wSquare()
