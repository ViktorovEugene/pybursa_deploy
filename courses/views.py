from django.core.urlresolvers import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from courses.models import Course


class CoursesListView(ListView):
	model = Course
	template_name = 'courses/courses_list.html'
	context_object_name = 'courses'


class CoursesDetailView(DetailView):
	model = Course
	template_name = 'courses/courses_item.html'
	context_object_name = 'course'


class CoursesCreateView(CreateView):
	model = Course
	template_name = 'courses/courses_edit.html'
	success_url = reverse_lazy('courses_list')


class CoursesUpdateView(UpdateView):
	model = Course
	template_name  = 'courses/courses_edit.html'

class CoursesDeleteView(DeleteView):
	model = Course
	success_url = reverse_lazy('courses_list')