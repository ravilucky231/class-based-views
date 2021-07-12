from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from django.urls import reverse_lazy

# Create your views here.
from .models import *
from django.contrib.auth.decorators import login_required


class Firstclassbased_View(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)

class Read_Teachers(ListView):
    model=Teachers
    template_name = 'teachers_list.html'


class Detail_Teachers(DetailView):
    model = Teachers
    template_name = 'teachers_detail.html'


class Create_Teachers(CreateView):
    model=Teachers
    fields=['name','subject','address','contact']
    template_name = 'teachers_form.html'



class Update_Teachers(UpdateView):
    model=Teachers
    fields=['name','address','contact']
    template_name = 'teachers_form.html'



class Delete_Teachers(DeleteView):
    model=Teachers
    template_name='teachers_confirm_delete.html'
    success_url = reverse_lazy('teachers_index')

# Create your views here.
