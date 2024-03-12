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


# Логин
def login_user_db(phone_number, password):
    db = next(get_db())
    login = db.query(User).filter_by(phone_number=phone_number, password=password).first()
    if login:
        return f'Вход выполнен успешно для пользователя {login.user_id}'
    else:
        return 'Неверный номер телефона или пароль'


#  Удаления пользователя
def delete_user_db(user_id):
    db = next(get_db())
    user = db.query(User).filter_by(user_id=user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return f'Пользователь с ID {user_id} удален'
    else:
        return 'Пользователь не найден'


# Изменения данных пользователя
def edit_user_info_db(user_id, edit_info, new_info):
    db = next(get_db())

    exact_user = get_exact_user_db(user_id)  # 3

    if exact_user:
        if edit_info == 'name':
            exact_user.name = new_info
        elif edit_info == 'surname':
            exact_user.surname = new_info

        db.commit()
        return 'Данные успешно изменены!'
    else:
        return 'Пользователь не найден(('


# Мы будем делать
# Добавить фото профиля
def upload_profile_photo_db(user_id, photo_path):
    db = next(get_db())

    exact_user = get_exact_user_db(user_id)

    if exact_user:
        exact_user.profile_photo = photo_path
        db.commit()

        return 'Успешно!'
    else:
        return 'Пользователь не найден(('


# Удаления фото профиля и начнем postservice.py
def delete_profile_photo_db(user_id):
    db = next(get_db())

    exact_user = get_exact_user_db(user_id)

    if exact_user:
        exact_user.profile_photo = 'None'
        db.commit()

        return 'Фото профиля удален'
    else:
        return 'Пользователь не найден(('
