import requests
import os
from .constant import uploadUrl



def UploadFile(filePath):
    # upload local file to server
    files = {'file': open(filePath, 'rb')}
    apiToken = os.environ.get('SHENMIND_API_TOKEN')
    headers = {
        'Authorization': apiToken
    }
    response = requests.post(uploadUrl, files=files, headers=headers)
    
    if response.status_code == 200:
        return response.json()['data'] # storage id
    else:
        raise Exception('fail to upload file: {}'.format(response.text))


