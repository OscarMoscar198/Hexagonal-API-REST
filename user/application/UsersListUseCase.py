class GetUsersUseCase:
    def __init__(self, repository):
        self.repository = repository

    def get_users(self):
        return self.repository.get_all()