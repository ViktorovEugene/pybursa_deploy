# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from students.models import Student

from django.shortcuts import redirect
from django.contrib import messages

from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['name', 'surname', 'date_of_birth', 
			'email', 'phone', 'package', 'group', 
		]
		widgets = {
			'date_of_birth': SelectDateWidget(years=range(1900, 2001)),
        }

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
	form_class = StudentForm


class StudentsDeleteView(DeleteView):
	model = Student
	success_url = reverse_lazy('students_list')

	def render_to_response(self, context, **response_kwargs):
		if self.get_object().protect:
			messages.info(self.request, "Sory, you can't delete this object. It is protect by the administation.")
			return redirect(self.request.META.get('HTTP_REFERER','/'))
		return super(StudentsDeleteView, self).render_to_response(context, **response_kwargs)
