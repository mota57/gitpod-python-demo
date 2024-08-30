
### SH Commands

* run fast api

    ```fastapi dev main.py```

* pip install libraries for this project

    ```pip install "fastapi[standard]"``` <br/>
    ```pip install sqlalchemy ```


### Directory  small project

```
|-my_super_project
    ├── main.py     
    ├── requierments.txt
    ├── .venv 
    ├── .gitignore 
    └── sql_app
        ├── __init__.py
        ├── crud.py
        ├── database.py     -- database context, SessionLocal, engine 
        ├── models.py       -- database models
        └── dto.py      -- pydantic models
```

### Directory for big projects
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py

### TODO

[x] Request Body
[skip] Query Parameters and String Validations
[skip] Path Parameters and Numeric Validations
[x] Body - Multiple Parameters
[x] Body - Fields
[x] Body - Nested Models
[pending] Declare Request Example Data
[pending] Extra Data Types
[pending] Cookie Parameters
[pending] Header Parameters
* [pending] Response Model - Return Type
[pending] Extra Models
[pending] Response Status Code
* [pending] Form Data
* [pending] Request Files
* [pending] Request Forms and Files
* [pending] Handling Errors
[pending] Path Operation Configuration
[pending] JSON Compatible Encoder
* [pending] Body - Updates
*[pending] Dependencies
*[pending] Security
*[pending] Middleware
* [pending] CORS (Cross-Origin Resource Sharing)
*[x] SQL (Relational) Databases
*[working] Bigger Applications - Multiple Files
*[pending] Background Tasks
[pending] Metadata and Docs URLs
* [pending] Static Files
* [pending] Testing
* [pending] Debugging