from fastapi import FastAPI
import uvicorn
from utils.database import Base, engine
from routers import book, user, address,user_book

app = FastAPI(title="Books & Users API")
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(book.router)
app.include_router(user.router)
app.include_router(address.router)
app.include_router(user_book.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
