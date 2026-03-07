import os
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


def filepath(instance, filename):
    return os.path.join(
        instance.faculty.univer.name,
        instance.faculty.name,
        filename
    )


class Base(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, blank=True, unique=True)

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['slug'])
        ]

    def __str__(self):
        return self.name


class Univer(Base):
    pass


class Faculty(Base):
    univer = models.ForeignKey(
        'Univer',
        on_delete=models.PROTECT,
        related_name='faculties',
        blank=True,
        null=True
    )


class FileWork(models.Model):

    class Degree(models.TextChoices):
        BACHELOR = 'bachelor', 'бакалавр'
        MASTER = 'master', 'магистратура'
        SPECIALTY = 'specialty', 'специалитет'
        MIDDLE_PROFESSIONAL_EDUCATION = 'mid_prof_edu', 'среднее профессиональное образование'

    class Education_form(models.TextChoices):
        DISTANT = 'distant', 'заочная'
        FULL_TIME = 'full-time', 'очная'

    class Course(models.IntegerChoices):
        FIRST = 1, '1 курс'
        SECOND = 2, '2 курс'
        THIRD = 3, '3 курс'
        FOURTH = 4, '4 курс'
        FIFTH = 5, '5 курс'


    faculty = models.ForeignKey(
        'Faculty',
        on_delete=models.PROTECT,
        related_name='files',
        blank=True,
        null=True
    )

    theme = models.CharField(max_length=200)
    degree = models.CharField(choices=Degree.choices)
    course = models.IntegerField(choices=Course.choices)
    discipline = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=filepath, null=True)
    edu_form = models.CharField(choices=Education_form.choices)
    variant = models.IntegerField(validators=[MinValueValidator(1)], blank=True, default='')

    def __str__(self):
       return self.theme
