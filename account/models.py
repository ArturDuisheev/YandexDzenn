from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    """
    OneToOneField по сути такой же, как ForeignKey, за исключением
    что он всегда несет с собой «уникальное» ограничение и наоборот
    отношение всегда возвращает объект.
    
    """
    password = models.CharField(max_length=18)
    email = models.EmailField(blank=True)


