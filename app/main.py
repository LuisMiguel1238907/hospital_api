from fastapi import FastAPI
from app.infrastructure.database import init_db
from app.interfaces.routes import router

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
