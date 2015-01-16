# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from students.models import Student


class StudentsListView(ListView):
	model = Student
	template_name = 'students/students_list.html'
	context_object_name = 'students'


class StudentsDetailView(DetailView):
	model = Student
	template_name = 'students/students_item.html'


class StudentsCreateView(CreateView):
	model = Student
	template_name = 'students/students_edit.html'
	success_url = reverse_lazy('students_list')


class StudentsUpdateView(UpdateView):
	model = Student
	template_name  = 'students/students_edit.html'


class StudentsDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students_list')