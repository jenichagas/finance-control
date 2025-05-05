from jose import jwt, JWTError
from fastapi import Request
from app.utils.security import decode_token
from bson import ObjectId
from app.config.mongodb import db
from app.config.settings import SECRET_KEY, ALGORITHM

async def get_current_user(request: Request):
    token = request.cookies.get("session_token")

    print("TOKEN ENCONTRADO:", token)  

    if not token:
        return None

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("PAYLOAD:", payload)  
        return payload
    except JWTError as e:
        print("ERRO AO DECODIFICAR TOKEN:", e)
        return None
