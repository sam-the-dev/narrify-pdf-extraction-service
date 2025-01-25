from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="PDF Extraction")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, 
#         host=os.getenv("API_HOST", "127.0.0.1"),
#         port=int(os.getenv("API_PORT", 8000))
# )