import os


def create_superuser():
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_common_objects.settings')
    django.setup()

    from django.contrib.auth.models import User
    username = 'cone'
    password = '3.1415926'
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = User(
            username=username,
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()


if __name__ == '__main__':
    os.system('python manage.py makemigrations')
    os.system('python manage.py migrate')
    create_superuser()
