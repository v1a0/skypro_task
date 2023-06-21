from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

PHONE_REGEX = RegexValidator(r'^\+?1?\d{9,15}$', "Номер должен быть представлен в международном формате: +79998887766")


class Resume(models.Model):
    class Conf:
        phone = 12
        short_text = 32
        long_text = 128
        lange_text = 2048

    class Status(models.TextChoices):
        ACTIVE = ('active', _("Активно"))
        INACTIVE = ('inactive', _("Неактивно"))

    class Grade(models.TextChoices):
        INTERN = ('intern', _("Начинающий"))
        JUNIOR = ('junior', _("Младший специалист"))
        MIDDLE = ('middle', _("Средний специалист"))
        SENIOR = ('senior', _("Старший специалист"))

    class Specialty(models.TextChoices):
        QA = ('qa', _("Тестирование"))
        FRONTEND_DEV = ('frontend', _("Front-end"))
        BACKEND_DEV = ('backend', _("Back-end"))

    owner = models.OneToOneField(
        verbose_name=_("Автор"), to=User, on_delete=models.CASCADE)
    status = models.CharField(
        _('Статус'), choices=Status.choices, max_length=Conf.short_text, default=Status.INACTIVE, null=False)
    grade = models.CharField(
        _('Грэйд'), choices=Grade.choices, max_length=Conf.short_text, default=Grade.INTERN, null=False)
    specialty = models.CharField(
        _('Специальность'), choices=Specialty.choices, max_length=Conf.short_text, default=None, null=True)
    salary = models.IntegerField(
        _('Зарплатные ожидания (руб)'), default=100_000, null=False)
    education = models.CharField(
        _("Образование"), max_length=Conf.lange_text, default=None, null=True)
    experience = models.CharField(
        _("Профессиональный опыт"), max_length=Conf.lange_text, default=None, null=True)
    portfolio = models.CharField(
        _("Ссылка на портфолио"), max_length=Conf.lange_text, default=None, null=True)
    title = models.CharField(
        _("Название"), max_length=Conf.long_text, default='', null=False, blank=True)
    phone = models.CharField(
        _("Номер телефона"), max_length=Conf.phone, default=None, null=True, validators=[PHONE_REGEX])
    email = models.CharField(
        _("Электронная почта"), max_length=Conf.long_text, default=None, null=True, blank=False)
