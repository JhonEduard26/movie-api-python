from fastapi import FastAPI
from dotenv import load_dotenv

from config.database import engine, SQLModel
from routers import movies, users

SQLModel.metadata.create_all(engine)

app = FastAPI()
app.title = 'FastAPI movie API'
app.include_router(movies.router)
app.include_router(users.router)

load_dotenv()


@app.get('/')
async def say_hello():
    return {
        'message': 'hello world'
    }
