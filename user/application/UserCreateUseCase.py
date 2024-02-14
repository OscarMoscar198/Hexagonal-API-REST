import os
from dotenv import load_dotenv
from user.domain.Entity.user import User
from email.message import EmailMessage
import smtplib
from user.infrastructure.security.utils import get_hashed_password


class CreateUserUseCase:
    def __init__(self, repository):
        self.repository = repository
        load_dotenv()
        

    def create_user(self, user: User):
        existent_user = self.repository.get_by_email(user.credentials.email)
        if existent_user is not None:
            return {"error": "Email already in use."}
        user.credentials.password = get_hashed_password(user.credentials.password)
        self.repository.save(user)
        self.send_email(user.credentials.email, user)
        return user
    
    def send_email(self, email, usuario):
        remitent = os.getenv("REMITENTE.EMAIL")
        destiny = email
        mesage = f"Click on the link to confirm your email: http://localhost:8001/verificar/{usuario.status.token_uuid}"
        
        email = EmailMessage()
        email["From"] = remitent
        email["To"] = destiny
        email["Subject"] = "Email confirmation"
        email.set_content(mesage)
        
        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
        smtp.login(remitent, os.getenv("PASS.GMAIL"))
        smtp.send_message(email)
        smtp.quit()