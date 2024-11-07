# Image Similarity Temu API Integration

This project demonstrates how to use the Temu API service to find similar products by image. It leverages image processing techniques to compress and resize images, convert them to a suitable byte format, and then sends these byte arrays to the API for similar product search.

## Requirements

Before running the project, make sure you have the following:

- Python 3.6 or higher
- Virtual environment (recommended)

## Installation

### 1. Clone the repository
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/image-similarity-api.git
   ```


###  2. Set up the virtual environment
#### On Windows:


```bash
python -m venv venv
venv\Scripts\activate

   ```

#### On macOS/Linux:


```bash
python3 -m venv venv
source venv/bin/activate
   ```


###  3.  Install dependencies

Install the required dependencies using the requirements.txt file:

```bash
pip install -r requirements.txt

   ```


###  4.  Usage

1. Prepare your image: Place the image that you want to search for similar products in the images folder, e.g., images/test_photo.jpg.

2. Run the script: Run the Python script to search for similar products by the image:

```bash
python main.py

   ```


###  5.  Console Output
The script will output a list of similar products retrieved via the Temu API based on the input image.

Example:

```bash
Result: [Product 1, Product 2, Product 3, ...]

   ```

This result shows similar products based on the uploaded image.

