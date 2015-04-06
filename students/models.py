# coding: utf8
# -*- coding: utf_8 -*-
from django.db import models
from courses.models import Course

class Student(models.Model):
    PACKAGE_CHOISES = (
        ('standart', 'Standart'),
        ('gold', 'Glod'),
        ('platimun', 'Platinum'),
    )
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(default='example@mail.com')
    phone = models.CharField(max_length=15, blank=True)
    package = models.CharField(max_length=8, choices=PACKAGE_CHOISES,
                        blank=True, null=True)
    group = models.ManyToManyField('courses.Group', blank=True, null=True)
    courses = models.ManyToManyField('courses.Course', null=True, blank=True, editable=False)
    protect = models.BooleanField(
        default=False, 
        help_text='protection from removal anonymous user',
    )
     
    def __setattr__(self, *args, **kwargs):
        super(Student, self).__setattr__(*args, **kwargs)
        if 'group' in args[0]:
            courses_id = [course_id[0] for course_id in self.group.values_list('course_id').distinct()]
            super(Student, self).__setattr__('courses', Course.objects.filter(id__in=courses_id))


    def __init__(self, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)
        
    def get_absolute_url(self):
        return "/students/%i/" % self.id


    def __unicode__(self):
        return u"%s %s" % (self.surname, self.name)
