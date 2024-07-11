import requests
import os
from .constant import permissionUrl

def get_upload_permission():
    """ Get upload permission from the server.
    
    Args:
        permission_url (str): URL to get upload permission.
        
    Returns:
        dict: Permission data.
        
    Raises:
        Exception: If failed to get permission or unexpected response format.
    """

    api_token = os.environ.get('SHENMIND_API_TOKEN')
    if not api_token:
        raise Exception("API token not available in environment variables.")


    headers = {
        'Authorization': f'Bearer {api_token}'
    }

    try:
        response = requests.get(permissionUrl, headers=headers)
        if response.status_code == 200:
            try:
                return response.json()['data']['permission']
            except KeyError:
                raise Exception("Unexpected response format: " + response.text)
        else:
            raise Exception("Failed to get upload permission: " + response.text)
        
    except requests.RequestException as e:
        raise Exception(f"Network-related error occurred: {e}")



def UploadFile(filepath):
    permission = get_upload_permission()
    
    url = permission['host']
    key = permission['directory'] + filepath.split('/')[-1]
    data = {
        'key': key,
        'policy': permission['policy'],
        'OSSAccessKeyId': permission['ossAccessKeyId'],
        'signature': permission['signature'],
        'callback': permission['callback']
    }
    
    # 准备文件数据
    with open(filepath, 'rb') as file:
        files = {'file': (filepath.split('/')[-1], file, 'application/octet-stream')}
        response = requests.post(url, data=data, files=files)

    if response.status_code == 200:
        return permission['fileID']
    else:
        raise Exception("Failed to upload file: " + response_body)

