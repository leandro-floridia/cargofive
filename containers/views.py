from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Contract

def index (request):
    return render(request, 'containers/index.html')

class ContractList(ListView):
    model = Contract


class ContractDetail(DetailView):
    model = Contract


class ContractCreate(CreateView):
    model = Contract
    # Field must be same as the model attribute
    fields = ['name', 'date']
    success_url = reverse_lazy('contract_list')


class ContractUpdate(UpdateView):
    model = Contract
    # Field must be same as the model attribute
    fields = ['name', 'date']
    success_url = reverse_lazy('contract_list')


class ContractDelete(DeleteView):
    model = Contract
    success_url = reverse_lazy('contract_list')
