from enum import Enum
from typing import Optional, Union
from pydantic import EmailStr
import datetime

from pydantic import BaseModel

class User(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    surname: Optional[str]
    birthday_date: Optional[datetime.date]
    is_admin: bool = False
