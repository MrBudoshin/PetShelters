from django.contrib.auth.models import User
from django.db import models


class Pet(models.Model):
    """
    Pet model create

    """
    name = models.CharField(max_length=100, null=True, verbose_name='Pets Name')
    age = models.PositiveIntegerField(db_index=True, default=0, null=True, verbose_name='Age')
    come_data = models.DateTimeField(auto_now_add=True)
    weight = models.PositiveIntegerField(db_index=True, null=True, verbose_name='Weight')
    special_signs = models.TextField(max_length=100, blank=True, null=True, verbose_name='Special signs')
    shelter = models.ForeignKey('Profile', default=None, null=True, on_delete=models.CASCADE,
                                related_name='shelter', verbose_name="Shelter")

    class Meta:
        verbose_name_plural = "Pets"
        verbose_name = "Pet"

    def __str__(self):
        return f'{self.name}, {self.age}, {self.come_data}, {self.weight}, {self.special_signs}'


class Profile(models.Model):
    """
    User model create
    """
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, db_index=True, blank=True, verbose_name='Name')
    last_name = models.CharField(max_length=50, db_index=True, blank=True, verbose_name='Surname')
    phone = models.IntegerField(db_index=True, null=True, verbose_name='Phone')
    mail = models.EmailField(db_index=True, null=True, verbose_name='Mail')

    class Meta:
        verbose_name_plural = "Profile"
        verbose_name = "Profiles"

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.phone}, {self.mail}'
