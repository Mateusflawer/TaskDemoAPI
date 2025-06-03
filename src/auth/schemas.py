from pydantic import BaseModel


class Token(BaseModel):
    username: str
    access_token: str
