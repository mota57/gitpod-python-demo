from enum import Enum
from typing import Annotated
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel, Field 

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world"}

# example using BaseModel
class ItemBase(BaseModel):
    name: str
    description: str | None = Field(
        default=None, 
        title="The description of the item", 
        description="Description length(0, 300)",
        max_length=300,
        min_length=10
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = 0.0

class User(BaseModel):
    username: str
    full_name: str | None = None



@app.put("/items/update_item/{item_id}")
async def update_item_v1(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: ItemBase | None = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

@app.put("/items/update_item/v2/{item_id}")
async def update_item_v2(item_id: int, item: ItemBase, user: User, importance: Annotated[int, Body()]):
    results = {"item_id": item_id, "item": item, "user": user, 'importance': importance}
    return results

@app.put("/items/update_item/v3/")
async def update_item_v3(item: ItemBase):
    results = {**item.model_dump()}
    return results

@app.post("/items/test-post-request/{item_id}")
def test_post_request(item_id:int, item: ItemBase, q : str | None = None):
    """
    Basically this is a test of post method, which accepts a object of type ItemBase and a path parameter. <br/>
    <ul>
    <li>If the parameter is also declared in the path, it will be used as a path parameter. </li><br/>
    <li>If the parameter is of a singular type (like int, float, str, bool, etc) it will be interpreted as a query parameter.</li> <br/>
    <li>If the parameter is declared to be of the type of a Pydantic model, it will be interpreted as a request body</li>
    </ul>
    """
    result = {'item_id': item_id, **item.model_dump(), 'q': q}
    item.name += " [appending from the server]"
    total = item.price + item.tax
    result.update({'total': total})
    if q:
        result.update({'q', q})
    return result

# example of using enum
class FileStatus(str, Enum):
    PROGRESS = "progres" 
    PENDING =  "pending" 

@app.get("/test_enum_option")
def test_enum_option(option: FileStatus):
    
    match option:
        case FileStatus.PROGRESS:
            return {"message": "your file is in progress."}
        case FileStatus.PENDING:
            return {"message": "your file is in pending."}
        case _:
            return {"message": "error"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return {"total": len(fake_items_db), "items": fake_items_db[skip : skip + limit], 'skip': skip, 'limit': limit}


@app.get("/items/v2/{item_id}")
async def read_item_v2(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/items/v3/{item_id}")
async def read_item_v3(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get('/test_required_query_parameters/{faa}/test')
async def test_required_query_parameters(faa:str, foo:str):
    return {'query': {'faa': faa, 'foo': foo}}