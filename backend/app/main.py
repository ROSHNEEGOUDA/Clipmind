from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.upload import router as upload_router
from app.routers import results
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="CLIPMIND API")

BASE_DIR = os.getcwd()

app.mount("/clips", StaticFiles(directory=os.path.join(BASE_DIR, "clips")), name="clips")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TEMP: allow all for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(results.router)

@app.get("/")
def root():
    return {"message": "CLIPMIND backend running"}
