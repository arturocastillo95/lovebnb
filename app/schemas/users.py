from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    username: str
    password: str
    email: EmailStr
    first_name: str
    last_name: str
    is_admin: bool = False