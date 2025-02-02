from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from typing import List

app = FastAPI()

# Allow CORS from any origin (adjust if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict this to specific domains if necessary)
    allow_credentials=True,
    allow_methods=["GET"],  # Allow only GET requests
    allow_headers=["*"],  # Allow all headers
)

# Load data from q-vercel-python.json
def load_marks_data():
    file_path = "q-vercel-python.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return {}

marks_data = load_marks_data()

@app.get("/api")
async def get_marks(name: List[str]):
    marks = [marks_data.get(n, "Not Found") for n in name]
    return JSONResponse(content={"marks": marks})
