import requests
import json
from PIL import Image
from io import BytesIO

def testpull():
    key = '5998310773c9fe494ecf3450e1d3e604'
    payload = {
        'key': key
    }
    response = requests.get('https://rebrickable.com/api/v3/lego/parts/51066/?key=' + key)  # Send request for part
    url = json.loads(response.text)['part_img_url']  # Get request back and parse link to image from JSON
    print('Image URL is: ' + url)  # Confirm good link

    img_response = requests.get(url)  # Get image FROM link
    print('Image type: ' + str(type(img_response)))
    print('Image data: ' + str(img_response.content))

    img = Image.open(BytesIO(img_response.content))  # Open image as image obect
    img.show()  # Show image
    print("Image should be shown")

def main():
    pass

if __name__ == "__main__":
    main()
else:
    print("Running from import")