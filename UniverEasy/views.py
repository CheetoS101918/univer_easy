from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView
from .forms import UploadFileForm
from .models import Univer, Faculty, FileWork


class HomePage(TemplateView):
     template_name = 'index.html'


class AboutPage(TemplateView):
    template_name = 'about.html'


class Univers(ListView):
    template_name = 'univers.html'
    model = Univer
    context_object_name = 'univers'
    queryset = Univer.objects.all()


class UniverFaculties(DetailView):
    template_name = 'faculties.html'
    model = Univer
    context_object_name = 'unik'
    slug_url_kwarg = 'univer_slug'
    slug_field = 'slug'


class FacultiesFiles(DetailView):
    template_name = 'faculty_files.html'
    model = Faculty
    context_object_name = 'faculty'
    slug_url_kwarg = 'faculty_slug'
    slug_field = 'slug'


class UploadFileView(FormView):
    template_name = 'file_upload.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('success_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SuccessPage(TemplateView):
    template_name = 'success.html'


def page_not_found(request, exception):
    return render(request, '404.html', status=404)
