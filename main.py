from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="SteelVision AI Backend",
    description="API системы визуального контроля дефектов стального проката",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

USERS_DB = {
    "worker1": "pass123",
    "engineer": "steel2026",
    "admin": "adminroot"
}

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/api/login", tags=["Аутентификация"])
def login(credentials: LoginRequest):
    username = credentials.username
    password = credentials.password
    if username not in USERS_DB or USERS_DB[username] != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверное имя пользователя или пароль"
        )

    return {
        "status": "success",
        "message": f"Пользователь {username} успешно вошел в систему",
        "token": f"temp-token-for-{username}"
    }