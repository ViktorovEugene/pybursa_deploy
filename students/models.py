from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=225)

    def __unicode__(self):
        return self.name


class Student(models.Model):
    PACKAGE_CHOISES = (
        ('standart', 'Standart'),
        ('gold', 'Glod'),
        ('platimun', 'Platinum'),
    )
    name = models.CharField(max_length=225)
    surname = models.CharField(max_length=225)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(default='example@mail.com')
    phone = models.CharField(max_length=15, blank=True)
    courses = models.ManyToManyField('courses.Course')
    package = models.CharField(max_length=8, choices=PACKAGE_CHOISES,
                               default='standart')
    group = models.ForeignKey(Group, related_name = 'students', default="", blank=True)

    def get_absolute_url(self):
        return "/students/%i/" % self.id

    def __unicode__(self):
        return u"%s %s" % (self.surname, self.name)
