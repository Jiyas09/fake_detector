from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

@app.post("/verify")
async def verify():
    return {"status": "Verification logic not yet implemented"}
from fastapi.staticfiles import StaticFiles

# Serve files from the uploads folder
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
import os

@app.get("/files")
def list_uploaded_files():
    files = []
    upload_dir = "uploads"
    if os.path.exists(upload_dir):
        files = os.listdir(upload_dir)
    return {"files": files}
from fastapi.responses import JSONResponse
import os

@app.get("/files")
def list_uploaded_files():
    upload_folder = "uploads"
    if not os.path.exists(upload_folder):
        return JSONResponse(content={"files": []})
    files = os.listdir(upload_folder)
    return JSONResponse(content={"files": files})

