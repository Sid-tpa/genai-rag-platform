from jose import jwt
from datetime import datetime, timedelta
def create_jwt_token(data: dict):
    expire = datetime.utcnow() + timedelta(hours=8)
    data.update({"exp": expire})
    return jwt.encode(data, "genesis10-secret", algorithm="HS256")
def verify_token(token: str):
    return jwt.decode(token, "genesis10-secret", algorithms=["HS256"])
