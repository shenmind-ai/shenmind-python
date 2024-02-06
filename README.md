## ShenMind AI Python Client


### Introduction
This project is a Python client for the ShenMind AI API, designed to make it easier for users to interact with the ShenMind API, explore and utilize AI models, and develop their own applications.


### Installation
You can directly install it using pip:
```
pip install shenmind==0.1.0 -i https://pypi.org/simple/
```
Alternatively, you can clone this repository:
```
git clone https://github.com/shenmind-ai/shenmind-python
python setup.py install

```

### Usage Examples

#### 1. Set Personal API Token


You can view and configure your personal API token in the [User Dashboard](https://mmdatong.com/dashboard?dashboardTab=userinfo).

```
 export SHENMIND_API_TOKEN=xxxxxxxxxxxxxxxxxxxx
```

#### 2. Create Prediction
```python
import shenmind

prediction = shenmind.run(
    modelId="yP1jM07UrYuQ6xHZ-lqYSQ==",    
    files=dict(
        image_path='/mnt/d/apps/TencenMeeting/WeMeet/3.21.3.430/resources/raw/emoji_2.png'
    ),
    params=dict(
        prompt="the product is for sale"
    ),
    waitResult=True
)


```


#### 3. Get Prediction Results


```python
import shenmind
prediction = shenmind.getPredictionOutput(predictionId)

````

#### 4. Cancel Prediction
```python
import shenmind
prediction = shenmind.cancelPrediction(predictionId)

```
