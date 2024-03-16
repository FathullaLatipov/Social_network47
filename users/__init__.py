from pydantic import BaseModel


# Валидатор для регистрации
class RegisterValidator(BaseModel):
    username: str
    surname: str
    phone_number: str
    city: str
    password: str


# Валидатор для логина
class LoginValidator(BaseModel):
    phone_number: str
    password: str
