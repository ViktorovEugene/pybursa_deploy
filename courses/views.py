# -*- coding: cp1251 -*-
from django.core.urlresolvers import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from courses.models import Course, Group
from coaches.models import Coach
from address.models import Address
from django.forms import ModelForm

from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from django import forms

from django.utils.decorators import classonlymethod
from django.shortcuts import redirect
from django.contrib import messages

class GroupForm(ModelForm):
	class Meta:
		model = Group
		fields = ['course', 'start_date']
		widgets = {
            'start_date': SelectDateWidget(years=range(2014, 2020)),
        }

class GroupCreateView(CreateView):
	model = Group
	template_name = 'courses/group_edit.html'
	success_url = reverse_lazy('courses_list')
	form_class = GroupForm

class GroupDeleteView(DeleteView):
	model = Group
	success_url = reverse_lazy('courses_list')
	
	def render_to_response(self, context, **response_kwargs):
		if self.get_object().protect:
			messages.info(self.request, "Sory, you can't delete this object. It is protect by the administation.")
			return redirect(self.request.META.get('HTTP_REFERER','/'))
		return super(GroupDeleteView, self).render_to_response(context, **response_kwargs)


class GroupUpdateView(UpdateView):
	model = Group
	template_name  = 'courses/group_edit.html'
	form_class = GroupForm

class CourseEditForm(ModelForm):
	class Meta:
		model = Course
		fields = ['name', 'tecnology', 'coach', 'assistant', 'venue', 'description']
		widgets = {
			'description': forms.Textarea,
			'tecnology': forms.RadioSelect,
		}


class CoursesListView(ListView):
	model = Course
	template_name = 'courses/courses_list.html'
	context_object_name = 'courses'


class CoursesDetailView(DetailView):
	model = Course
	template_name = 'courses/courses_item.html'
	context_object_name = 'course'
	def get_context_data(self, **kwargs):
  		context = super(CoursesDetailView, self).get_context_data(**kwargs)
  		# context['course'] = u'; '.join(self.get_object().course_venue.values_list('name', 
    	#                                                     flat=True))
		# print self.get_object()
		# print context['course'].student_set.all()[0].name
  		return context


class CoursesCreateView(CreateView):
	model = Course
	template_name = 'courses/courses_edit.html'
	success_url = reverse_lazy('courses_list')
	form_class = CourseEditForm

	def get_context_data(self, **kwargs):
  		context = super(CoursesCreateView, self).get_context_data(**kwargs)
  		context['coaches'] = Coach.objects.filter(status='coach')
  		context['assistants'] = Coach.objects.filter(status='assistant')
  		context['addresses'] = Address.objects.all()
  		return context

class CoursesUpdateView(UpdateView):
	model = Course
	template_name  = 'courses/courses_edit.html'
	form_class = CourseEditForm

	def get_context_data(self, **kwargs):
  		context = super(CoursesUpdateView, self).get_context_data(**kwargs)
  		context['coaches'] = Coach.objects.filter(status='coach')
  		context['assistants'] = Coach.objects.filter(status='assistant')
  		context['addresses'] = Address.objects.all()
  		return context

class CoursesDeleteView(DeleteView):
	model = Course
	success_url = reverse_lazy('courses_list')
	
	def render_to_response(self, context, **response_kwargs):
		if self.get_object().protect:
			messages.info(self.request, "Sory, you can't delete this object. It is protect by the administation.")
			return redirect(self.request.META.get('HTTP_REFERER','/'))
		return super(CoursesDeleteView, self).render_to_response(context, **response_kwargs)