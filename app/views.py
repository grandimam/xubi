from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from app.models import CloudProvider


class ConnectorCreateView(CreateView):
    model = CloudProvider
    fields = '__all__'
    template_name = 'connector.html'
    success_url = '/app/success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ConnectorUpdateView(UpdateView):
    model = CloudProvider
    fields = '__all__'
    template_name = 'connector.html'
    success_url = '/app/success'


class ConnectorDeleteView(DeleteView):
    model = CloudProvider
    fields = '__all__'
    template_name = 'connector.html'
    success_url = '/app/success'


class ConnectorPageFormSuccessView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Successfully saved connector details')
