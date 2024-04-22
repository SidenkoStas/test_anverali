from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse


class CustomUser(AbstractUser):
    """
    Custom user model.
    """
    experience = models.TextField(verbose_name="Опыт", blank=True)
    contacts = models.TextField(verbose_name="Контакты", blank=True)
    is_executor = models.BooleanField(verbose_name="Тип пользователя", default=False)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.username}"
