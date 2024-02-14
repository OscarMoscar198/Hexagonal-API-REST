from user.domain.Entity.Client import Contact
from user.domain.Entity.Accreditation import Credential
from user.infrastructure.security.utils import get_hashed_password

class updateUserUseCase:
    def __init__(self, repository):
        self.repository = repository

    def update_user(self, user_id: str, contact: Contact, credentials: Credential):
        user = self.repository.get(user_id)
        if user is None:
            return {"error": "User not found."}

        user.contact = contact
        user.credentials = Credential(email=credentials.email, password=get_hashed_password(credentials.password))

        contact = user.contact
        credentials = user.credentials

        return self.repository.update(user_id, contact, credentials)