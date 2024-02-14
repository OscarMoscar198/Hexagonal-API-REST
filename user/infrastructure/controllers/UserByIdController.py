from fastapi import APIRouter, HTTPException
from user.application.UserGetUseCase import GetUserUseCase

get_user_by_id_router = APIRouter()

def initialize_endpoints(repository):
    getUserUseCase = GetUserUseCase(repository)

    @get_user_by_id_router.get("/")
    async def get_user(user_id: str):
        user = getUserUseCase.get_user(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user