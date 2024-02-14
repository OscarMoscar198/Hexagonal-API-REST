class VerificationUserUseCase:
    def __init__(self, repository):
        self.repository = repository
    
    def verify_user(self, token_uuid):
        user = self.repository.get_by_uuid(token_uuid)
        if user is not None:
            self.repository.verify_user(token_uuid)
            return True
        return False