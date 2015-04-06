from django.db import models
import datetime


class Group(models.Model):
    name = models.CharField(max_length=30, null=True,
        blank=True)
    protect = models.BooleanField(
        default=False,
        help_text='protection from removal anonymous user',
    )
    start_date = models.DateField(default=datetime.date.today())
    end_date = models.DateField(null=True, blank=True)
    number_of_students = models.IntegerField(default=5)
    course = models.ForeignKey('courses.Course', null=True)
    
    def __init__(self, *args, **kwargs):
        super(Group, self).__init__(*args, **kwargs)
        self.end_date = (self.start_date + datetime.timedelta(days=61))
        try:
            self.name = ('%s %s-%s' % (
                        self.course.name,
                        self.start_date.strftime('%Y %b'),
                        self.end_date.strftime('%b'),
                        ))
        except AttributeError:
            pass

    def __unicode__(self):
        return '%s' % (self.name)

    def get_absolute_url(self):
        return "/courses/groups/%i/" % self.id


class Course(models.Model):
    TECNOLOGY_CHOISE = (
        ('python', 'Python'),
        ('ruby', 'Ruby'),
        ('javascript', 'JavaScript'),
    )
    LABEL_IMG = {
        'python': 'python label.png',
        'ruby': 'shiny_red_ruby.png',
        'javascript': 'js.png',
    }
    protect = models.BooleanField(
        default=False,
        help_text='protection from removal anonymous user',
    )
    name = models.CharField(max_length=15)
    description= models.TextField()
    coach = models.ForeignKey('coaches.Coach',  limit_choices_to={'status': 'coach'})
    assistant = models.ForeignKey('coaches.Coach', limit_choices_to={'status': 'assistant'}, blank=True, null=True,
                                  related_name='course_assistant')
    tecnology = models.CharField(max_length=11, choices=TECNOLOGY_CHOISE, default='')
    venue = models.ForeignKey('address.Address', related_name='course_venue', null=True, blank=True, on_delete=models.SET_NULL,
        default=None)

    def get_img(self):
        tec = self.tecnology
        return self.LABEL_IMG[tec]

    def get_absolute_url(self):
        return "/courses/%i/" % self.id

    def __unicode__(self):
        return '%s (%s) - %s' % (self.name, self.coach, self.tecnology)

