from database.models import User

from database import get_db


# Получить всех пользователей
def get_all_users_db():
    db = next(get_db())
    get_all_users = db.query(User).all()
    return get_all_users


# Получить определенного пользователя
def get_exact_user_db(user_id):
    db = next(get_db())
    checker = db.query(User).filter_by(id=user_id).first()
    if checker:
        return f'Пользователь найден {checker.user_id}'
    else:
        return 'Пользователь не обнаружен'


# Регистрация пользователя
def register_user_db(name, surname, phone_number, city, password):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number).first()
    if checker:
        return 'Такой номер телефона уже есть в базу'
    else:
        new_user = User(name=name, surname=surname, phone_number=phone_number, city=city, password=password)
        db.add(new_user)
        db.commit()
        return f'Успешно зарегистрированы {new_user.user_id}'

# ДЗ
# Логин def login_user_db(phone_number, password)
# Delete user in db def delete_user_db(user_id)

# Мы будем делать
# Изменения информации о пользователее
# Добавить фото профиля
# Удаления фото профиля и начнем postservice.py

