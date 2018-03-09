from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from agenda.models import Contacto, Telefono, Social
from agenda.forms import ContactoForm, TelefonoForm, SocialForm
from . import views

''' def agenda_view(request):
    owner = request.user
    contactos = Contacto.objects.all()
    return render(request,'agenda_contactos_template.html', {'contactos': contactos}) '''

class AgendaLista(ListView):
    model = Contacto
    template_name = 'agenda_contactos_template.html'    

class AgregarView(CreateView):
    model = Contacto
    template_name = 'agenda_agregar_template.html'
    form_class = ContactoForm
    second_form_class = TelefonoForm
    third_form_class = SocialForm
    success_url = reverse_lazy('agenda:lista')

    def get_context_data(self, **kwargs):
        context = super(AgregarView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] =  self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)            
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            agregar = form.save(commit=False)
            agregar.towner = form2.save()
            agregar.sowner = form3.save()
            agregar.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))        


class ContactoDelete(DeleteView):
    model = Contacto
    template_name = 'contacto_delete.html'
    success_url = reverse_lazy('agenda:lista')