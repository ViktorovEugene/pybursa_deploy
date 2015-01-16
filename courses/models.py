from django.db import models


class Course(models.Model):
    TECNOLOGY_CHOISE = (
        ('python', 'Python'),
        ('rubby', 'Ruby'),
        ('javascript', 'JavaScript'),
    )
    name = models.CharField(max_length=225)
    description= models.TextField()
    coach = models.ForeignKey('coaches.Coach')
    assistant = models.ForeignKey('coaches.Coach', blank=True, null=True,
                                  related_name='course_assistant')
    start_date = models.DateField()
    end_date = models.DateField()
    tecnology = models.CharField(max_length=11, choices=TECNOLOGY_CHOISE)
    venue = models.ForeignKey('address.Address', related_name='course_venue')
    slug = models.SlugField()

    def get_absolute_url(self):
        return "/courses/%i/" % self.id

    def __unicode__(self):
        return '%s (%s) - %s' % (self.name, self.coach, self.tecnology)
