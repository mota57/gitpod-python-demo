from fastapi import FastAPI

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get('/items/{item}')
async def items(item:int):
    return {"message": "route: /items/" + str(item)}