# -*- coding: utf-8 -*-

from django.db import models

class Address(models.Model):
    DISTRICT_LIST=(
        (u'Дзержинский', u'Дзержинский район'),
        (u'Киевский', u'Киевский район'),
        (u'Коминтерновский', u'Коминтерновский район'),
        (u'Ленинский', u'Ленинский район'),
        (u'Московский', u'Московский район'),
        (u'Октябрьский', u'Октябрьский район'),
        (u'Орджоникидзевский', u'Орджоникидзевский район'),
        (u'Фрунзенский', u'Фрунзенский район'),
        (u'Холодная', u'Холодная Гора'),
        (u'Червонозаводский', u'Червонозаводский район'), 
    )
    post_index = models.IntegerField(
        max_length=5, blank=True,
        default=620000,
    )
    country = models.CharField(max_length=60, default=u'Украина')
    region = models.CharField(max_length=30, default=u'Слобожанщина')
    district = models.CharField(max_length=30, choices=DISTRICT_LIST,
                                default=u'Киевский'
    )
    street = models.CharField(max_length=30, default=u'Бейкер-стрит')
    house = models.CharField(max_length=30, default='221-b')
    new_field = models.CharField(max_length=50, blank=True)
    
    def __init__(self, *args, **kwargs):
        super(Address, self).__init__(*args, **kwargs)
        self.new_field = (self.street + self.house)
    
    def get_absolute_url(self):
        return "/address/%i/" % self.id

    def __unicode__(self):
        return '%s, %s, %s' % (self.country, self.region, self.street)