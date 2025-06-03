from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from src.auth.sucurity import authenticate_user, create_access_token
from src.auth.schemas import Token
from src.api.endpoints import tasks

api_router = APIRouter()

# Inclui roteadores de tarefas
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])


# Endpoint para login
@api_router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"username": user.username, "access_token": access_token}
