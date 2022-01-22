from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = ("User",)


class MyUserManager(UserManager):
    """
    Создание и сохранение пользователя с указанным именем пользователя и паролем.
    """

    def _create_user(self, username, password, **extra_fields):

        if not username:
            raise ValueError('Имя пользователя должно быть установлено')
        if not password:
            raise ValueError('Пароль должен быть установлен')

        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class User(AbstractUser):
    """
    Переопределенная модель пользователя
    """

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=128,
        unique=True,
        help_text=_("Требуется 128 символов или меньше. Только буквы, цифры и @/./+/-/_ "),
        validators=[username_validator]
    )
    password = models.CharField(_('password'), max_length=128)
    is_superuser = models.BooleanField(
        _('superuser status'), default=False, help_text=_('У этого пользователя есть все разрешения '),
    )
    first_name = models.CharField(_("first name"), max_length=15)
    last_name = models.CharField(_("last name"), max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Определение пользователя как активного.'
            'Отмените выбор этого параметра вместо удаления учетных записей.'
        ),
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
