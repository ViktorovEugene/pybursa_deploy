from django.core.urlresolvers import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from coaches.models import Coach

from django.shortcuts import redirect
from django.contrib import messages

from django.forms import ModelForm

class CoachForm(ModelForm):
	class Meta:
		model = Coach
		fields = ['name', 'surname', 'email', 
			'status', 'phone_number', 'user',
		]
		widgets = {
            # 'start_date': SelectDateWidget(years=range(2014, 2020)),
        }


class CoachesListView(ListView):
	model = Coach
	template_name = 'coaches/coaches_list.html'
	context_object_name = 'coaches'


class CoachesDetailView(DetailView):
	model = Coach
	template_name = 'coaches/coaches_item.html'


class CoachesCreateView(CreateView):
	model = Coach
	template_name = 'coaches/coaches_edit.html'
	success_url = reverse_lazy('coaches_list')


class CoachesUpdateView(UpdateView):
	model = Coach
	template_name  = 'coaches/coaches_edit.html'
	form_class = CoachForm


class CoachesDeleteView(DeleteView):
	model = Coach
	success_url = reverse_lazy('coaches_list')

	def render_to_response(self, context, **response_kwargs):
		if self.get_object().course_set.all() and self.get_object().status == 'coach':
			course_tuple = tuple(course.name for course in self.get_object().course_set.all())
			deny_reason = 'Sory, you can\'t delete this coach. He is teacing on "' + "\", \"".join(course_tuple) + "\"."
			messages.info(self.request, deny_reason)
			return redirect(self.request.META.get('HTTP_REFERER','/'))
			
		if self.get_object().protect:
			messages.info(self.request, "Sory, you can't delete this object. It is protect by the administation.")
			return redirect(self.request.META.get('HTTP_REFERER','/'))


		return super(CoachesDeleteView, self).render_to_response(context, **response_kwargs)

		
		