from user.infrastructure.repositories.MYSQL_db_repository import Repository as MySQLRepository
from user.infrastructure.repositories.SQLite_db_repository import Repository as SQLiteRepository

class RepositoryFactory:
    def __init__(self):
        self.repositories = {
            "mysql": MySQLRepository(),
            "sqlite": SQLiteRepository()
        }

    def get_repository(self, db_type):
        return self.repositories.get(db_type, None)
    