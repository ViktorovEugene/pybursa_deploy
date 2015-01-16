from django.core.urlresolvers import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from address.models import Address


class AddressListView(ListView):
  model = Address
  template_name = 'address/address_list.html'
  context_object_name = 'address'


class AddressDetailView(DetailView):
  model = Address
  template_name = 'address/address_item.html'
  context_object_name = 'address'

def get_context_data(self, **kwargs):
  context = super(AddressDetailView, self).get_context_data(**kwargs)
  context['course'] = u'; '.join(self.get_object().course_venue.values_list('name', 
                                                        flat=True))
  return context



class AddressCreateView(CreateView):
  model = Address
  template_name = 'address/address_edit.html'
  success_url = reverse_lazy('address_list')


class AddressUpdateView(UpdateView):
  model = Address
  template_name  = 'address/address_edit.html'


class AddressDeleteView(DeleteView):
  model = Address
  success_url = reverse_lazy('address_list')