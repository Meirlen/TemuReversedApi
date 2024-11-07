from ApiService import *


def main():
    """
    Main function that orchestrates the process of:
    1. Loading the image from the file system.
    2. Getting the image bytes.
    3. Fetching similar products based on the image via Temu API.
    """
    # Load the image and get its byte representation
    imgSearchBytes = get_result("images/test_photo.jpg")

    # Fetch similar products based on the image data through Temu API
    get_similar_products_by_image(imgSearchBytes)


if __name__ == "__main__":
    main()
