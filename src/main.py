import requests
import shutil
import os
import json
import configparser
import zipfile

ELVUI_URL = "https://api.tukui.org/v1/addon/elvui"

WOW_PATH = ""
with open('config.json', 'r') as config:
    config_json = json.load(config)
    WOW_PATH = config_json['wow_path']
    config.close()

download_response = requests.get(ELVUI_URL)


if download_response.status_code == 200:
    download_url = download_response.json()['url']
    
    
    downloaded_file = requests.get(download_url)
    if downloaded_file.status_code == 200:

        with open(os.path.join(WOW_PATH, 'elvui.zip'), 'wb') as file:
            file.write(downloaded_file.content)
            file.close()
        
        print('File Downloaded')

        zip_file_path = os.path.join(WOW_PATH, 'elvui.zip')
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(WOW_PATH)
            zip_ref.close()
        print('Files Inserted')
        os.remove(zip_file_path)
    else:
        print('failed to download')

    
else:
    print('failed to reach api')
