from jose import jwt, JWTError
from fastapi import HTTPException
from passlib.context import CryptContext
from datetime import datetime, timedelta

# from datetime import datetime, timedelta
# from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from db.models.users import User
from core.config import SECRET_KEY

ALGORITHM = "HS256"

class AuthHandler():
    secret = SECRET_KEY
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password_hash(self, password: str):
        return self.pwd_context.hash(password)

    def verify_password(self, password: str, password_hash: str):
        return self.pwd_context.verify(password, password_hash)

    def encode_token(self, data: dict, expires_delta: timedelta = None):
        if expires_delta:
            expires = datetime.utcnow() + expires_delta
        else:
            expires = datetime.utcnow() + timedelta(minutes=5)
        token = jwt.encode({**data, "exp": expires}, self.secret, algorithm=ALGORITHM)
        return token.decode("utf-8")
    
    def decode_token(self, token: str):
        try:
            payload = jwt.decode(token, self.secret, algorithms=[ALGORITHM])
            return payload
        except JWTError:
            raise HTTPException(status_code=400, detail="Invalid token")

    def authenticate_user(self, db: Session, email: str, password: str):
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect email or password")
        if not self.verify_password(password, user.password):
            raise HTTPException(status_code=400, detail="Incorrect email or password")
        return user
