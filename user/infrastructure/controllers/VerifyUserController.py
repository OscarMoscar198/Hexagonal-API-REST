from fastapi import APIRouter
from user.application.UserVerificationUseCase import VerificationUserUseCase

verify_user_router = APIRouter()

def initialize_endpoints(repository):
    verificationUserUseCase = VerificationUserUseCase(repository)


    @verify_user_router.put("/")
    async def verificar(uuid: str):
            if verificationUserUseCase.verify_user(uuid):
                return {"msj": "Verified account"}
            else:
                return {"msj": "User not found"}