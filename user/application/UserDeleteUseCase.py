class deleteUserUseCase:
    def __init__(self, repository):
        self.repository = repository
    
    def delete_user(self, user_id: str):
        return self.repository.delete(user_id)