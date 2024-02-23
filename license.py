import requests


def check_license(key):
    url = 'https://nopaste.net/0a7pyhBS6B'
    response = requests.get(url)
    data = response.json()

    for el in data:
        if key == el['LicenseKey']:
            return True
    return False
