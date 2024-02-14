from user.infrastructure.security.utils import verify_password, create_access_token

class AuthenticationUserUseCase:
    def __init__(self, repository):
        self.repository = repository

    def auth_user(self, email: str, password: str):
        user = self.repository.get_by_email(email)
        if user is not None:
            if not user.verified:
                return {"error": "User not verified."}
            if isinstance(user, dict):
                valid_password = verify_password(password, user['password'])
            else:
                valid_password = verify_password(password, user.password)
            if valid_password:
                access_token = create_access_token(subject=user.id)
                return {"access_token": access_token, "token_type": "bearer"}
        return None