from django.db import IntegrityError

from account.models import User
from bot.keyboards import user_types


def create_user(user_data, user_type):
    try:
        new_user = User.objects.create(
            **user_data
        )
        new_user.user_type = user_type
        new_user.save()
        return new_user
    except IntegrityError:
        raise Exception('User already exists')

