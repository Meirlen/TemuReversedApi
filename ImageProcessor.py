from PIL import Image, ExifTags
import base64
import io
import os


class ImageProcessor:
    """
    A class to handle image processing tasks such as compression, resizing, and rotation based on EXIF data.
    """

    @staticmethod
    def compress_image(image: Image.Image, quality: int, max_size: int) -> bytes:
        """
        Compresses the provided image to a target quality and ensures that the image size does not exceed the specified max_size.

        Parameters:
            image (Image.Image): The image object to be compressed.
            quality (int): The initial quality for compression (1 to 100).
            max_size (int): The maximum allowed size in bytes for the compressed image.

        Returns:
            bytes: The compressed image as a byte string.
        """
        if image is None:
            return None

        # Set default quality if the provided quality is invalid
        if quality <= 0:
            quality = 100

        # Create a BytesIO object to store the compressed image
        output_stream = io.BytesIO()
        image.save(output_stream, format='JPEG', quality=quality)

        # Gradually decrease the quality until the size is under the max_size
        while quality > 0 and output_stream.tell() > max_size:
            output_stream.seek(0)
            output_stream.truncate()
            quality -= 10
            image.save(output_stream, format='JPEG', quality=quality)

        return output_stream.getvalue()

    def load_and_resize_image(self, file_path: str) -> Image.Image:
        """
        Loads an image from the provided file path, resizes it if needed, and applies rotation based on EXIF data.

        Parameters:
            file_path (str): The file path of the image to load.

        Returns:
            Image.Image: The processed image object.
        """
        if not os.path.exists(file_path):
            return None

        # Open the image using PIL
        image = Image.open(file_path)
        width, height = image.size

        # Resize the image if its dimensions exceed 800x800 pixels
        if width > 800 or height > 800:
            max_dimension = max(width, height)
            scale_ratio = 800 / max_dimension
            new_size = (int(width * scale_ratio), int(height * scale_ratio))
            image = image.resize(new_size, Image.LANCZOS)

        # Apply rotation based on EXIF data
        exif = image.getexif()
        if exif:
            orientation_key = next((key for key, val in ExifTags.TAGS.items() if val == 'Orientation'), None)
            if orientation_key and orientation_key in exif:
                orientation = exif[orientation_key]
                rotation_angle = {3: 180, 6: 270, 8: 90}.get(orientation, 0)
                if rotation_angle:
                    image = image.rotate(rotation_angle, expand=True)

        return image


class Base64Converter:
    """
    A class to handle base64 encoding and decoding of binary data.
    """

    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    @staticmethod
    def to_base64(data: bytes) -> str:
        """
        Converts binary data to a base64-encoded string.

        Parameters:
            data (bytes): The binary data to encode.

        Returns:
            str: The base64 encoded string.
        """
        if data is None:
            return None

        # Encode the data and replace the padding character with the last character in the base64 character set
        encoded = base64.b64encode(data).decode('utf-8')
        return encoded.replace("=", Base64Converter.base64_chars[
            -1])  # Replaces "=" with the last character in the base64 set


# Example usage
def get_result(image_path):
    """
    Processes an image by loading, resizing, compressing, and encoding it into a base64 string.

    Parameters:
        image_path (str): The path to the image to process.

    Returns:
        str: The base64 encoded compressed image.
    """
    processor = ImageProcessor()
    loaded_image = processor.load_and_resize_image(image_path)
    compressed_data = processor.compress_image(loaded_image, quality=90, max_size=1048576)  # 1 MB

    if compressed_data:
        img_search_bytes = Base64Converter.to_base64(compressed_data)
        return img_search_bytes
