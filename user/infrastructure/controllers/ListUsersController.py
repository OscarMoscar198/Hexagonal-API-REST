from fastapi import APIRouter
from user.application.UsersListUseCase import GetUsersUseCase

get_list_user_router = APIRouter()

def initialize_endpoints(repository):
    listUsersUseCase = GetUsersUseCase(repository)
    
    @get_list_user_router.get("/")
    async def get_users():
        return listUsersUseCase.get_users()
