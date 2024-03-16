from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from users import RegisterValidator, LoginValidator
from database.userservice import register_user_db, login_user_db

# Создать компонент
user_router = APIRouter(prefix='/users', tags=['Управления с пользователями'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


# Запрос для регистрации
@user_router.post('/register')
async def register_user(data: RegisterValidator):
    result = register_user_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Такой пользователь уже имеется'}


# Запрос для логина
# main.py
@user_router.post('/login')
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = login_user_db(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail='Неверный номер или пароль')
    else:
        return user
