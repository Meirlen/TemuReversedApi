import requests
from ImageProcessor import get_result

# URL to send the request to
url = "https://eu.temu.com/api/poppy/v1/search?scene=image_search_result"

def show_similar_products_in_console(data):
    """
    Prints the list of similar products based on the search results.

    Parameters:
        data (dict): The response data containing the list of products.
    """
    # Extract the list of products
    goods_list = data['result']['data']['goods_list']

    # Print the title and thumb_url for each product
    for idx, product in enumerate(goods_list, 1):
        print(f"Product {idx}:")
        print(f"  Title: {product['title']}")
        print(f"  Image: {product['thumb_url']}")
        print()  # Empty line to separate products

def get_similar_products_by_image(img_search_bytes):
    """
    Sends a POST request to the image search API with the provided image bytes and prints the result.

    Parameters:
        img_search_bytes (str): The base64-encoded bytes of the image to be used for searching.

    Returns:
        None
    """
    # Request headers
    headers = {
        "Host": "eu.temu.com",
        "Cookie": "install_token=95E2BF77-9D44-4990-B4C9-D0AA73386B02; api_uid=CnC092ck87tDQwBYUkOEAg==",
        "Content-Type": "application/json",
        "Abc-Ver": "V5:198.031000",
        "Ta-Token": "1acGB+AhFNcwfIronubUSGFmnkJ6ueCb20P1lQKlQEIEaDV7cY2HEnZ3Jh1klXfBp36Ek8FFwI+foe8P9cpjqSPZbHhKPYkKRmjNw7Bk0Xj9qvvrVIWv2OkJkK3EgiZBT0QrPYITALg11idqfSa1hXie6JM1RvIYM8NotGF63LfETpvbfiwFWbr8goxRMLh+JH+/53rh01a4ErKmf9Otd9LJT+OnvtNnYa5GbPUiTBuZ8apGO44iluK1ZkKxwGDr2VCxIb0zOy6TlKnBo2JuuMCrlJSK+Otjcw4/S028eawVwdq5DxkLK1woCHDuUCAOdsSl8eU+o0LKP863FXcsdODwJ/9X/OgBbHeaHJjhHCSMw/1AF8KYniDNPYRhWwe/MXknNVo49ONBEGjQ3Ml3vTTVlEe4to9m9ZoIluGx5uzBz055FPxsI3w++OKcBFmwPgb",
        "Accept": "*/*",
        "X-User-Info": "rgn=102; lang=en; ccy=KZT; tz=Asia/Almaty",
        "Accesstoken": "",
        "Accept-Language": "en",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 temu_ios_version/3.10.0 temu_ios_build/1730387100675 pversion/0",
        "X-App-Info": "front=1;version=1",
        "Volantis-Config": "V4:198.031000",
        "Etag": "WIfB1UtVygre"
    }

    # Request body in JSON format
    data = {
        "listId": "D71D79B628B042069F411082ED612B40",
        "query": "",
        "scene": "image_search_result",
        "imgSearchType": "camera_local_focus",
        "source": "10085",
        "pageSn": 10436,
        "searchMethod": "",
        "offset": 0,
        "imgSearchBytes": img_search_bytes,
        "installToken": "95E2BF77-9D44-4990-B4C9-D0AA73386B02",
        "srchEnterSource": "10005200010",
        "pageElSn": "206861",
        "pageSize": 20
    }

    # Send POST request
    response = requests.post(url, headers=headers, json=data)

    # Check the response status code
    if response.status_code == 200:
        show_similar_products_in_console(response.json())
    else:
        print("Error! Status Code:", response.status_code)
        print("Response:", response.text)
