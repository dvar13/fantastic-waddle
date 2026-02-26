from fastapi import FastAPI
from sqlalchemy import text
from database import engine

app = FastAPI()

@app.get("/film")
def get_films():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM film LIMIT 5"))
        return [dict(row._mapping) for row in result]


@app.get("/actors")
def get_actors():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM actor LIMIT 10"))
        return [dict(row._mapping) for row in result]


@app.get("/inventory")
def get_inventory():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM inventory LIMIT 10"))
        return [dict(row._mapping) for row in result]