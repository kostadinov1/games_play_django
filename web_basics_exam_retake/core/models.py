from django.core.exceptions import ValidationError
from django.db import models

def min_age_validator(value):
    if value < 12:
        raise ValidationError('Age cannot be below 12!')


def rating_validator(value):
    if not 0.5 <= value <= 5:
        raise ValidationError('The rating can be between 0.1 and 5.0!')

class Profile(models.Model):
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30
    email = models.EmailField(blank=False, null=False)
    age = models.IntegerField(blank=False, null=False,
                              validators=(min_age_validator,))
    password = models.CharField(max_length=PASSWORD_MAX_LEN, blank=False, null=False)
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LEN, blank=True, null=True)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LEN, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        if self.first_name:
            return f'{self.first_name}'
        if self.last_name:
            return f'{self.last_name}'


    def has_profile(self):
        if Profile.objects.first():
            return True


class Game(models.Model):
    TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15


    GAME_CHOICES = (('Action', 'Action'), ('Adventure', 'Adventure'), ('Puzzle', 'Puzzle'),
                    ('Strategy', 'Strategy'), ('Sports', 'Sports'),
                    ('Board/Card Game', 'Board/Card Game'), ('Other', 'Other'))

    title = models.CharField(max_length=TITLE_MAX_LEN, blank=False, null=False, unique=True)
    category = models.CharField(max_length=CATEGORY_MAX_LEN, choices=GAME_CHOICES)
    rating = models.FloatField(blank=False, null=False)
    max_level = models.IntegerField(blank=True, null=True,
                                    validators=(rating_validator,))
    image = models.URLField(blank=False, null=False)
    summary = models.TextField(blank=True, null=True)
