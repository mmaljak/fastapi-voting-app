from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

### We don't need this anymore since we use alembic now.
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Security best practices - Narrow down the scope of origins
origins = ["https://www.google.com", "https://www.youtube.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# We don't need this route anymore. This is just used as an example for documentation purposes.
@app.get("/")
def root():
    return {"message": "Welcome to my API!!!"}
