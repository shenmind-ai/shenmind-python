import shenmind
from shenmind.upload import UploadFile
import time



if __name__ == '__main__':
    # upload file
    # filePath = '/mnt/d/apps/TencenMeeting/WeMeet/3.21.3.430/resources/raw/emoji_2.png'
    # storageId = UploadFile(filePath)
    # print(storageId)


    prediction = shenmind.run(
        modelId="yP1jM07UrYuQ6xHZ-lqYSQ==",
        files=dict(
            image_path='/mnt/d/apps/TencenMeeting/WeMeet/3.21.3.430/resources/raw/emoji_2.png'
        ),
        params=dict(
            prompt="the product is for sale"
        )
    )

    import pdb; pdb.set_trace()

    # while True:
    #     prediction = shenmind.getPredictionOutput(predictionId)
    #     import pdb; pdb.set_trace()
    #     if prediction['status'] == 'succeeded':
    #         import pdb; pdb.set_trace()
    #         break
    #     else:
    #         time.sleep(1)

