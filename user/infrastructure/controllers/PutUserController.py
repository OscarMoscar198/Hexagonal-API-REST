from fastapi import APIRouter
from user.application.UserUpadateUseCase import updateUserUseCase
from user.domain.Entity.Client import Contact
from user.domain.Entity.Accreditation import Credential

update_user_router = APIRouter()

def initialize_endpoints(repository):
    updateUserUseCaseById = updateUserUseCase(repository)

    @update_user_router.put("/")
    async def update_user(user_id: str, contact: Contact, credentials: Credential):
        updated_user = updateUserUseCaseById.update_user(user_id, contact, credentials)
        return updated_user