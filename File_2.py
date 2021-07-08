import requests
from pprint import pprint
import os

path = os.getcwd()

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': ''
        }

    def upload_link(self):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": 'test/test', "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()['href']


    def upload(self, filename):
        href = self.upload_link()
        response = requests.put(href, data=open(filename, 'rb'))
        pprint(response)


if __name__ == '__main__':
    uploader = YaUploader(path)
    result = uploader.upload(path + '\\test')