from dataclasses import dataclass, field
from .Client import Contact
from .Accreditation import Credential
from .Status import Status

@dataclass
class User:
    contact: Contact
    credentials: Credential
    status: Status = field(default_factory=Status)
