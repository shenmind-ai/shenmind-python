import shenmind
from shenmind.upload import UploadFile
import time



if __name__ == '__main__':
    import shenmind
    modelId = "yP1jM07UrYuQ6xHZ-lqYSQ=="
    files = dict(
        # image_path="test.png"
        image_path="https://pic.rmb.bdstatic.com/bjh/240205/dump/00fc2ba00e4e97174fce6378c7ee399a.jpeg"
    )
    params = dict(
        prompt="bottle on table for Christmas"
    )
    prediction = shenmind.run(modelId, files, params, waitResult=True)
    print(prediction)
  

    import pdb; pdb.set_trace()

