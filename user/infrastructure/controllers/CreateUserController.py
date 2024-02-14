from fastapi import APIRouter, Body
from user.application.UserCreateUseCase import CreateUserUseCase
from user.domain.Entity.user import User

create_user_router = APIRouter()

def initialize_endpoints(repository):
    createUserUsercase = CreateUserUseCase(repository)

    @create_user_router.post("/")
    async def create_user(user: User = Body(...)):
        user_created = createUserUsercase.create_user(user)
        return {"m": "Please verify your email to enable your account", "\nuser": user_created}