from django.db import models
from utils.file_upload import university_path, professor_path
from utils import constants
from django.db.models import Avg
from django.utils import timezone


class University(models.Model):
    class Meta:
        verbose_name = 'Университет'
        verbose_name_plural = 'Университеты'

    name = models.CharField(max_length=500, verbose_name='Название')
    abbreviation = models.CharField(max_length=300, verbose_name='Аббревиатура', blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Описание')
    logo = models.ImageField(upload_to=university_path, verbose_name='Лого', null=True, default=constants.NO_IMAGE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.abbreviation:
            self.abbreviation = "".join(w[0].upper() for w in self.name.split())
        super(University, self).save(*args, **kwargs)


class Professor(models.Model):
    class Meta:
        verbose_name = 'Преподователь'
        verbose_name_plural = 'Преподаватели'

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(default='', blank=True, max_length=50, verbose_name='Отчество')
    full_name = models.CharField(blank=True, null=True, max_length=200, verbose_name='ФИО')
    universities = models.ManyToManyField(University, verbose_name='Университеты в котором он преподает')
    average_rating = models.PositiveIntegerField(default=0, verbose_name='Средний рейтинг')
    rating_count = models.PositiveIntegerField(default=0, verbose_name='Количество оценок')
    avatar = models.ImageField(upload_to=professor_path, verbose_name='Аватар', null=True, default=constants.NO_AVATAR)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.full_name = '{} {} {}'.format(self.first_name, self.last_name, self.patronymic)
        super(Professor, self).save(*args, **kwargs)

    def recalculate_average_rating(self):
        if self.ratings.exists():
            self.average_rating = self.ratings.aggregate(avg=Avg('value'))['avg']
            self.rating_count = self.ratings.count()
            self.save()


class ProfessorRatingManager(models.Manager):

    @staticmethod
    def last_review_in_week(email, professor):
        professor_ratings = ProfessorRating.objects.filter(professor=professor,
                                                           email=email)
        if professor_ratings.exists():
            last_rating = professor_ratings.order_by('-created_at', ).first()
            if (timezone.now() - last_rating.created_at).days < 7:
                return True
        return False


class ProfessorRating(models.Model):
    class Meta:
        verbose_name = 'Оценка преподавателя'
        verbose_name_plural = 'Оценки преподавателя'
        ordering = ['-created_at']

    email = models.EmailField(max_length=50, verbose_name='Email')
    review = models.TextField(verbose_name='Отзыв', default='')
    value = models.PositiveSmallIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    professor = models.ForeignKey(Professor,
                                  on_delete=models.CASCADE,
                                  related_name='ratings',
                                  verbose_name='Преподаватель')
    objects = ProfessorRatingManager()

    def save(self, *args, **kwargs):
        super(ProfessorRating, self).save(*args, **kwargs)
        self.professor.recalculate_average_rating()


class Subject(models.Model):
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    name = models.CharField(max_length=300, verbose_name='Название предмета')
    abbreviation = models.CharField(max_length=300, verbose_name='Аббревиатура', blank=True, null=True)
    professors = models.ManyToManyField(Professor, related_name='subjects', verbose_name='Преподаватели этого предмета')
    university = models.ForeignKey(University, related_name='subjects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if len(self.name.split()) != 1:
            self.abbreviation = "".join(w[0].upper() for w in self.name.split())
        else:
            self.abbreviation = self.name
        super(Subject, self).save(*args, **kwargs)
