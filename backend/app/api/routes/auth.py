from typing import List
from fastapi import APIRouter

auth = APIRouter()

@auth.get("/")
async def get_all_auth() -> List[dict]:
	users = [{"id": 1, "name": "Kona"}]
	return users
