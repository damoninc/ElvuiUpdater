import os
import requests
import json
import zipfile

def main():
    ELVUI_URL = "https://api.tukui.org/v1/addon/elvui"
    
    # Load configuration
    with open('config.json', 'r') as config_file:
        config_json = json.load(config_file)
        wow_path = config_json.get('wow_path', '')
    
    # Download ELVUI
    download_response = requests.get(ELVUI_URL)
    if download_response.status_code == 200:
        download_url = download_response.json().get('url')
        
        downloaded_file = requests.get(download_url)
        if downloaded_file.status_code == 200:
            # Save downloaded file
            elvui_zip_path = os.path.join(wow_path, 'elvui.zip')
            with open(elvui_zip_path, 'wb') as file:
                file.write(downloaded_file.content)
            print('ELVUI downloaded successfully.')

            # Extract files
            with zipfile.ZipFile(elvui_zip_path, 'r') as zip_ref:
                zip_ref.extractall(wow_path)
            print('ELVUI files extracted.')
            
            # Remove downloaded zip file
            os.remove(elvui_zip_path)
        else:
            print('Failed to download ELVUI.')
    else:
        print('Failed to reach ELVUI API.')

if __name__ == "__main__":
    main()