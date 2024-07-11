import requests
import os
import time
import json
from .upload import UploadFile
from .constant import createPredictionUrl, queryPredictionUrl, cancelPredictionUrl


def run(
    modelId,
    files,
    params,
    waitResult=True
):
    data = dict()
    for key, filepath in files.items():
        if filepath.startswith('http'):
            data[key] = filepath
        else:
            storageId = UploadFile(filepath)
            data[key] = storageId
        
    # run 
    apiToken = os.environ.get('SHENMIND_API_TOKEN')
    headers = {
        'Authorization': f'Bearer {apiToken}',
        'Content-Type': 'application/json'
    }

    data['modelID'] = modelId
    data.update(params)
    response = requests.post(createPredictionUrl, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        if not waitResult:
            return response.json()['data']['predictionID']
        else:
            predictionId = response.json()['data']['predictionID']
            while True:
                prediction = getPredictionOutput(predictionId)
                if prediction['status'] in ['succeeded', 'failed', 'canceled']:
                    return prediction
                else:
                    time.sleep(1)
    else:
        raise Exception('fail to create prediction: {}'.format(response.text))

def getPredictionOutput(predictionId):
    apiToken = os.environ.get('SHENMIND_API_TOKEN')
    headers = {
        'Authorization': f'Bearer {apiToken}'
    }
    data = {
        'predictionID': predictionId
    }
    response = requests.get(queryPredictionUrl, params=data, headers=headers)

    if response.status_code == 200:
        return response.json()['data']
    else:
        raise Exception('fail to get prediction: {}'.format(response.text))


def cancelPrediction(predictionId):
    apiToken = os.environ.get('SHENMIND_API_TOKEN')
    headers = {
        'Authorization': f'Bearer {apiToken}'
    }
    data = {
        'predictionID': predictionId
    }


    response = requests.post(cancelPredictionUrl, data=data, headers=headers)


    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('fail to cancel prediction: {}'.format(response.text))
