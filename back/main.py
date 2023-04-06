from fastapi import FastAPI, Request
from utils.middleware import add_middlewares

app = FastAPI()
add_middlewares(app)

@app.get("/")
async def read_item(request: Request):
    return {
        'locale': request.headers.get('accept-language'),
    }

if __name__ == "__main__":
    from utils.comands import Comands
    Comands()