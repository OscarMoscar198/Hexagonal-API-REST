from fastapi import APIRouter, HTTPException
from user.application.SignInserUseCase import AuthenticationUserUseCase
from user.domain.Models.SignIn import Login

login_router = APIRouter()

def initialize_endpoints(repository): 
    authenticationUserUseCase = AuthenticationUserUseCase(repository)
    
    @login_router.post("/")
    async def login(login: Login):
        user = authenticationUserUseCase.auth_user(login.email, login.password)
        if user is None:
            raise HTTPException(status_code=400, detail="Wrong email or password")
        return {"user": user}