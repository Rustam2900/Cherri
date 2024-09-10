from django.db import IntegrityError

from account.models import User, TelegramUser
from bot.keyboards import user_types


def create_user(user_data, user_type):
    try:
        if user_type == User.UserType.INDIVIDUAL:
            new_user, created = User.objects.get_or_create(
                username=user_data['username'],
                full_name=user_data['full_name'],
                phone_number=user_data['phone_number'],
            )
        else:
            new_user, created = User.objects.get_or_create(
                username=user_data['username'],
                phone_number=user_data['phone_number'],
                company_name=user_data['company_name'],
                full_name=user_data['employee_name'],
            )

        TelegramUser.objects.create(
            user=new_user,
            telegram_id=user_data['telegram_id'],
            telegram_username=user_data['username'],
        )
        new_user.user_type = user_type
        new_user.set_password(user_data['password'])
        new_user.save()
        return new_user
    except IntegrityError:
        raise Exception('User already exists')



def get_user_db(username):
    user = TelegramUser.objects.filter(telegram_username=username).first()
    return user
