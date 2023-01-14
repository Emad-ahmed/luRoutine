from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from student.models import Batch, Section
from faculty.models import Program, Curriculum

from .forms import BatchForm, SectionForm
from django.urls import reverse


# from django.shortcuts import get_object_or_404
@method_decorator(login_required, name='dispatch')
class BatchListView(ListView):
    model = Batch
    template_name = 'batch_list.html'
    context_object_name = 'batches'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class BatchCreateView(CreateView):
    model = Batch
    template_name = 'batch_form.html'
    form_class = BatchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['curriculums'] = Curriculum.objects.all()
        return context

    def get_success_url(self):
        return reverse('student:batch_list')

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(**({'form': form})))


@method_decorator(login_required, name='dispatch')
class SectionListView(ListView):
    model = Section
    template_name = 'section_list.html'
    context_object_name = 'sections'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class SectionCreateView(CreateView):
    model = Section
    template_name = 'section_form.html'
    form_class = SectionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['batches'] = Batch.objects.all()
        return context

    def get_success_url(self):
        return reverse('student:section_list')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(**({'form': form})))
