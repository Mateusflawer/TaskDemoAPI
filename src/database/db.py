from src.auth.models import UserInDB
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Banco de dados simulado
tasks_db = []
users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("mateus123"),
        "disabled": False
    }
}