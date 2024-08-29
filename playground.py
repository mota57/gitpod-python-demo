from playground import dump
from fastapi import FastAPI


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
skip = 0
limit = 2
item = fake_items_db[skip : skip + limit]
print(item)