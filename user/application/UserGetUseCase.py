class GetUserUseCase:
    def __init__(self, repository):
        self.repository = repository

    def get_user(self, user_id: str):
        return self.repository.get(user_id)