from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Entry
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView,UpdateView




# Create your views here.

class HomeView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'entries/index.html'
    context_object_name ="blog_entries"
    ordering = ['-entry_date']
    paginate_by = 5


class EntryView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'entries/entry_detail.html'

class CreateEntryView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = ['entry_title', 'entry_text','img']
    
   
    
    def form_valid(self,form):
         form.instance.entry_author = self.request.user
         return super().form_valid(form)

from django.urls import reverse_lazy



class YDeleteView(  DeleteView,):
    model = Entry
    success_url = reverse_lazy('blog-home')


class EditPost(UpdateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = ['entry_title','entry_text']
    success_url = reverse_lazy('blog-home')
    
   
    