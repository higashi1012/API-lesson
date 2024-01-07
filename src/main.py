from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "test用APIです get"}

@app.get("/sample")
def read_root():
    return {"message": "sampleAPIです"}

@app.get("/items/{item_id}")
def get_item(item_id):
    items = {
        100: "Tシャツ",
        101: "ジュース",
        102: "パン",
        103: "靴下"
    }
    return {"message": items.get(int(item_id))}

@app.delete("/")
def read_root():
    return {"message": "delete用APIです"}