import os
import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_url(self, file_name, overwrite='true'):
        url =' https://cloud-api.yandex.net/v1/disk/resources/upload'
        url += '?path=' + file_name + '&overwrite=' + overwrite
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        return response.json()

    def get_name_from_path(self, file_path):
        name = file_path.split('/')
        return name[-1]

    def upload(self, file_path: str):
        file_name = self.get_name_from_path(file_path)
        upload_url = self.get_upload_url(file_name)['href']
        response = requests.put(upload_url, data=open(file_path, 'rb'))
        response.raise_for_status()
        return response.status_code


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ''
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)