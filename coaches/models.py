from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):
    COACH_TYPES = (
        ('coach', 'Coach'),
        ('assistant', 'Assistant'),
    )
    name = models.CharField(max_length=225)
    surname = models.CharField(max_length=225)
    email = models.EmailField(default='example@gmail.com')
    status = models.CharField(choices=COACH_TYPES, max_length=9,)
    phone_number = models.CharField(max_length=15, default='+38000000000')
    user = models.ForeignKey(User, blank=True, default='')

    def get_absolute_url(self):
        return "/coaches/%i/" % self.id

    def __unicode__(self):
        return "%s %s %s" % (self.surname, self.name, self.status)
