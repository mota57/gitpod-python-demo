from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session

from .sql_app import crud, dto, models
from .sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

"""
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response
"""

# order of run is from bottom definition to top definiton
@app.middleware('http')
async def middleware_2(request: Request, call_next):
    response = Response('Internal server error', status_code=500)
    try:
        print('mid2')
        print(request.state.current_user_id)
        response = await call_next(request)
    finally:
        # request.state.db.close()
        print('end of the request pipeline 2')
    return response

@app.middleware('http')
async def middleware_1(request: Request, call_next):
    response = Response('Internal server error', status_code=500)
    try:
        print('mid1')
        request.state.current_user_id = "hector.mota123"
        response = await call_next(request)
    finally:
        # request.state.db.close()
        print('end of the request pipeline 1')
    return response



# Dependency
def get_request_context_data(request: Request):
    return request.state.current_user_id


def get_db():
    """
    https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/
    FastAPI supports dependencies that do some extra steps after finishing.  <br/>
    To do this, use yield instead of return, and write the extra steps (code) after.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=dto.User)
def create_user(user: dto.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[dto.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), user_id: str = Depends(get_request_context_data)):
    print(user_id)
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=dto.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=dto.Item)
def create_item_for_user(
    user_id: int, item: dto.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[dto.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items