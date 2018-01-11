from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                  ListView, DetailView,
                                  CreateView,UpdateView, DeleteView)
from django.http import HttpResponse
from cbvapp.models import School,Student
from django.core.urlresolvers import reverse_lazy
# Create your views here.
#   FUNCTION BASED VIEWS
# -----------------------
# def index(request):
#     return render(request, 'index.html')

#  Basic class based view example
# -----------------------
# class CBView(View):
#     def get(self, request):
#         return HttpResponse("this is the index page using class based view")
#  Template view example
# -----------------------
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injecting'] = "this content will be injected"
        return context

class SchoolListView(ListView):
    context_object_name = 'schoollist'
    model = School

class SchoolDetailsView(DetailView):
    context_object_name = 'school_details'
    model = School
    template_name = 'cbvapp/school_details.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = School

class StudentCreateView(CreateView):
    fields = ('name', 'age', 'school')
    model = Student

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = School

class StudentUpdateView(UpdateView):
    fields = ('name', 'age', 'school')
    model = Student

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('cbvapp:list')
