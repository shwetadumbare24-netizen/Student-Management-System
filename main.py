from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Routes.studentroutes import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://studentmangsys.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def Homepage():
    return {"message": "Student Management System"}