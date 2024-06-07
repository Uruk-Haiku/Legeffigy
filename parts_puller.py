import requests
import validators
import time
from PIL import Image
from io import BytesIO

def main():
    max_minifigures = 16468
    key = '5998310773c9fe494ecf3450e1d3e604'

    for page in range(4, 16):  # Since I was already done the first 3 page worths
        payload = {
            'key': key,
            'page': page,
            'page_size': '1000'
        }

        while True:
            try:
                response = requests.get('https://rebrickable.com/api/v3/lego/minifigs', payload)
                response.raise_for_status()
            except:
                print('Rebrickable API call failed - Retrying...')
                time.sleep(1)
                continue
            break
            
        minifig_dict_list = response.json()['results']

        for minifig_dict in minifig_dict_list:
            url = minifig_dict['set_img_url']
            if validators.url(url) != True: continue

            img_data = requests.get(url)
            img = Image.open(BytesIO(img_data.content))

            img.save('Minifigures/' + minifig_dict['set_num'] + '.png')

            # TODO Maybe add sleep here to avoid getting my IP address blocked?
            time.sleep(0.25)  # Hopefully sufficient
    
    print("[DONE]")
            

def pulltest():
    key = '5998310773c9fe494ecf3450e1d3e604'
    payload = {
        'key': key
    }
    response = requests.get('https://rebrickable.com/api/v3/lego/parts/51066/?key=' + key)  # Send request for part
    url = response.json()['part_img_url']  # Get request back and parse link to image from JSON

    img_response = requests.get(url)  # Get image FROM link

    img = Image.open(BytesIO(img_response.content))  # Open image as image obect
    img.show()  # Show image
    print("Image should be shown")

    img.save('Minifigures/new_lego_image.png')
    print('Image should be saved')

### HELPERS
def format_minifig_number(number):
    assert number <= 16468
    str_num = str(number)
    str_num = '0' * (6 - len(str_num)) + str_num
    return str_num


if __name__ == "__main__":
    main()
else:
    print("Running from import")