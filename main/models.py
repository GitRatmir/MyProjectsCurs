from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    surname = models.CharField(max_length=150, verbose_name='Фамилия')
    age = models.IntegerField(blank=False)
    is_studying = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='students/',verbose_name='Фото', blank=True)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


    def __str__(self):
        return self.name + self.surname

# Create your models here.
