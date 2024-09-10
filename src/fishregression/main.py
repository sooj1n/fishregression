from typing import Union
from fastapi import FastAPI
import pickle

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello", "world"}

@app.get("/items/{item_id}")
def read_time(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fish")
def fisth(length:float):
    """
    물고기 무게 예측

    Args:
        length (float): 물고기 길이(cm)

    Returns:
        weight (float): 물고기 무게(kg)
    """

    ### 모델 불러오기
    with open("/home/sujin/code/fishregression/linear_model.pkl", "rb") as f:
        lr_model = pickle.load(f)

    prediction = lr_model.predict([[length **2, length]])
    print(f"*************************************** {prediction}")
    return { "preiction": float(prediction[0]) }
