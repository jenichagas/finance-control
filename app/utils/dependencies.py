from fastapi import Request
from app.utils.security import decode_token
from bson import ObjectId
from app.config.mongodb import db

async def get_current_user(request: Request):
    token = request.cookies.get("session_token")
    if not token:
        return None

    payload = decode_token(token)
    if not payload:
        return None

    user_id = payload.get("sub")
    if not user_id:
        return None

    return await db.users.find_one({"_id": ObjectId(user_id)})
