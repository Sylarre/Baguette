from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Reteta

def acasa(request):
    context = {
        'retete': Reteta.objects.all()
    }
    return render(request, 'retete/acasa.html', context)

class RetetaListView(ListView):
    model = Reteta
    template_name = 'retete/acasa.html'
    context_object_name = 'retete'
    ordering = ['-data_adaugare']

class RetetaDetailView(DetailView):
    model = Reteta

class RetetaCreateView(LoginRequiredMixin, CreateView):
    model = Reteta
    fields = ['titlu', 'continut']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class RetetaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reteta
    fields = ['titlu', 'continut']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        reteta = self.get_object()
        if self.request.user == reteta.autor:
            return True
        return False

class RetetaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reteta
    success_url = '/'

    def test_func(self):
        reteta = self.get_object()
        if self.request.user == reteta.autor:
            return True
        return False

def despre(request):
    return render(request, 'retete/despre.html', {'titlu': 'Despre'})
