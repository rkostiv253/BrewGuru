from fastapi import FastAPI

from cafe_service.routes import cafe_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_version_prefix = "/api/v1"


app.include_router(cafe_router, prefix=f"{api_version_prefix}/cinema", tags=["brewguru"])
