from datetime import datetime
from databases.SQLite.db_connection import DBConnection, User
from user.domain.Entity.Client import Contact
from user.domain.Entity.Accreditation import Credential
from user.domain.Entity.user import User as UserDomain
from databases.SQLite.db_connection import DBConnection

class Repository:
    def __init__(self):
        self.connection = DBConnection()
        self.session = self.connection.Session()

    def save(self, user_domain: UserDomain):
        user = User(
            name=user_domain.contact.name,
            last_name=user_domain.contact.last_name,
            cellphone=str(user_domain.contact.cellphone),
            email=user_domain.credentials.email,
            password=user_domain.credentials.password,
            token_uuid=user_domain.status.token_uuid,
            verified=user_domain.status.verified,
        )
        self.session.add(user)
        self.session.commit()
        return user

    def get_all(self):
        return self.session.query(User).all()

    def get(self, user_id: str):
        user = self.session.query(User).get(user_id)
        return user

    def update(self, user_id: str, contact: Contact, credentials: Credential):
        user = self.session.query(User).get(user_id)
        if user:
            user.name = contact.name
            user.last_name = contact.last_name
            user.cellphone = str(contact.cellphone)
            user.email = credentials.email
            user.password = credentials.password
            self.session.commit()
            self.session.refresh(user)
        return user

    def delete(self, user_id: str):
        user = self.session.query(User).get(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False

    def get_by_email(self, email):
        user = self.session.query(User).filter_by(email=email).first()
        return user
    
    def get_by_uuid(self, token_uuid):
        user = self.session.query(User).filter_by(token_uuid=token_uuid).first()
        return user

    def verify_user(self, token_uuid):
        try:
            user = self.session.query(User).filter_by(token_uuid=token_uuid).one()
            self.session.query(User).filter_by(id=user.id).update({User.verified: True,  User.verified_at: datetime.now()})
            self.session.commit()
            return user
        except:
            print ("Error")
            return None