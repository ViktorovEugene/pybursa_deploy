from django.db import models
import datetime


class Course(models.Model):
    TECNOLOGY_CHOISE = (
        ('python', 'Python'),
        ('ruby', 'Ruby'),
        ('javascript', 'JavaScript'),
    )
    LABEL_IMG = {
        'python': 'python label.png',
        'ruby': 'shiny_red_ruby.png',
        'javascript': 'java-logo-png.png',
    }
    name = models.CharField(max_length=225)
    description= models.TextField()
    coach = models.ForeignKey('coaches.Coach')
    assistant = models.ForeignKey('coaches.Coach', blank=True, null=True,
                                  related_name='course_assistant')
    start_date = models.DateField(default=datetime.date.today())
    end_date = models.DateField()
    tecnology = models.CharField(max_length=11, choices=TECNOLOGY_CHOISE)
    venue = models.ForeignKey('address.Address', related_name='course_venue')
    slug = models.SlugField(blank=True)

    def __init__(self, *args, **kwargs):
        super(Course, self).__init__(*args, **kwargs)
        print self.start_date
        self.end_date = (self.start_date + datetime.timedelta(days=61))

    def get_img(self):
        tec = self.tecnology
        return self.LABEL_IMG[tec]

    def get_absolute_url(self):
        return "/courses/%i/" % self.id

    def __unicode__(self):
        return '%s (%s) - %s' % (self.name, self.coach, self.tecnology)
