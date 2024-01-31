## 深迈 API 的 Python 客户端


### 简介
本项目是深迈 API 的 Python 客户端，以让用户更加方便地使用深迈API，更好地探索和使用AI模型，以及开发自己的应用产品。


### 安装
您可以直接通过 pip 安装：
```
pip install shenmind==0.1.0 -i https://pypi.org/simple/
```
或者 clone 本仓库
```
git clone https://github.com/shenmind-ai/shenmind-python
python setup.py install

```

### 使用样例

#### 1. 设置个人 Api Token

您可以在[个人中心](https://mmdatong.com/dashboard?dashboardTab=userinfo) 查看自己的 Api Token，并进行配置。
```
 export SHENMIND_API_TOKEN=xxxxxxxxxxxxxxxxxxxx
```

#### 2. 创建预测
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


#### 3. 查询预测结果


```python
import shenmind
prediction = shenmind.getPredictionOutput(predictionId)

````


