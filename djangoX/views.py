
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Snack
from django.shortcuts import render

class SnackListView(ListView):
    template_name = "snack_pages/snack_list.html"
    model = Snack

class SnackDetailView(DetailView):
    template_name = "snack_pages/snack_detail.html"
    model = Snack

class SnackUpdateView(UpdateView):
    template_name = "snack_pages/snack_update.html"
    model = Snack
    fields = ["name", "purchaser", "description"]


class SnackCreateView(CreateView):
    template_name = "snack_pages/snack_create.html"
    model = Snack
    fields = ["name", "purchaser", "description"]

class SnackDeleteView(DeleteView):
    template_name = "snack_pages/snack_delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")