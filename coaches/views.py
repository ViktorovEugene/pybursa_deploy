from django.core.urlresolvers import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from coaches.models import Coach


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


class CoachesDeleteView(DeleteView):
	model = Coach
	success_url = reverse_lazy('coaches_list')
		
		