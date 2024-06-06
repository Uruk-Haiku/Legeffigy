import requests

def main():
    key = '5998310773c9fe494ecf3450e1d3e604'
    payload = {
        'key': key
        'part_nums': 
    }
    r = requests.get('https://rebrickable.com/api/v3/lego/parts')

if __name__ == "__main__":
    main()
else:
    print("Running from import")