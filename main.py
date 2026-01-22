from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


app=FastAPI()

@app.get('/')
def index():
    return {'message':'Welcome to Inventory Management App. Use /docs for API Documentation'}

register_tortoise(
    app,
    db_url='sqlite://database.sqlite3',
    modules={"models":["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
@app