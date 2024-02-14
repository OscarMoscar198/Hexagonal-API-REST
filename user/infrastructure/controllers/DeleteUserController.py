from fastapi import APIRouter, HTTPException
from user.application.UserDeleteUseCase import deleteUserUseCase

delete_user_router = APIRouter()

def initialize_endpoints(repository):
    deleteUserUseCaseById = deleteUserUseCase(repository)

    @delete_user_router.delete("/")
    async def delete_user(user_id: str):
        if not deleteUserUseCaseById.delete_user(user_id):
            raise HTTPException(status_code=404, detail="User not found")
        return {"msj" : "User deleted"}
    