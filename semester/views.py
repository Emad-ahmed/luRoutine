from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import get_object_or_404
from faculty.models import Course, Teacher
from semester.models import Semester, CourseOffered, CourseDistribution
from student.models import Batch, Section
from .forms import SemesterForm, CourseOfferingForm, CourseDistributionForm, CourseDistributionUpdateForm
from django.contrib import messages
from django.shortcuts import redirect

# from django.shortcuts import get_object_or_404
@method_decorator(login_required, name='dispatch')
class SemesterListView(ListView):
    model = Semester
    template_name = 'semester_list.html'
    context_object_name = 'semesters'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class SemesterCreateView(CreateView):
    model = Semester
    template_name = 'semester_form.html'
    form_class = SemesterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get_success_url(self):
        return reverse('semester:semester_list')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(**({'form': form})))


@method_decorator(login_required, name='dispatch')
class SemesterUpdateView(UpdateView):
    model = Section
    template_name = 'semester_form.html'
    form_class = SemesterForm
    context_object_name = 'semesters'

    def get_object(self):
        return get_object_or_404(Semester, id=self.request.GET.get('id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
    def get_success_url(self):
        return reverse('semester:semester_list')
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(**({'form': form})))



def SemesterDeleteView(request, pk):
    try:
        parent = Section.objects.get(id=pk)
        parent.delete()
        messages.success(request, 'Successfully Deleted')
    except:
        messages.success(request, 'Please First Delete The Child Model')
        return redirect('/semesters')

    return redirect('/semesters')



@method_decorator(login_required, name='dispatch')
class CourseOfferingListView(ListView):
    model = CourseOffered
    template_name = 'course_offering_list.html'
    context_object_name = 'offers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class CourseOfferingCreateView(CreateView):
    model = CourseOffered
    template_name = 'course_offering_form.html'
    form_class = CourseOfferingForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['semesters'] = Semester.objects.all()
        context['batches'] = Batch.objects.all()
        context['courses'] = Course.objects.all()
        return context

    def get_success_url(self):
        return reverse('semester:offer_list')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(**({'form': form})))


@method_decorator(login_required, name='dispatch')
class CourseOfferUpdateView(UpdateView):
    model = CourseOffered
    template_name = 'course_offering_form.html'
    form_class = CourseOfferingForm
    context_object_name = 'offers'

    def get_object(self):
        return get_object_or_404(CourseOffered, id=self.request.GET.get('id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['semesters'] = Semester.objects.all()
        context['batches'] = Batch.objects.all()
        context['courses'] = Course.objects.all()
        return context

    def get_success_url(self):
        return reverse('semester:offer_list')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(**({'form': form})))




def CourseOfferDeleteView(request, pk):
    try:
        parent = CourseOffered.objects.get(id=pk)
        parent.delete()
        messages.success(request, 'Successfully Deleted')
    except:
        messages.success(request, 'Please First Delete The Child Model')
        return redirect('/offers')

    return redirect('/offers')





@method_decorator(login_required, name='dispatch')
class CourseDistributionList(ListView):
    model = CourseDistribution
    template_name = 'course_distribution_list.html'
    context_object_name = 'dists'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class CourseDistributionCreateView(CreateView):
    model = CourseDistribution
    template_name = 'course_distribution_form.html'
    form_class = CourseDistributionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['teachers'] = Teacher.objects.all()
        context['offers'] = CourseOffered.objects.all()
        return context

    def get_success_url(self):
        return reverse('semester:dist_list')

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(**({'form': form})))



@method_decorator(login_required, name='dispatch')
class CourseDistributionUpdateView(UpdateView):
    model = CourseDistribution
    template_name = 'course_update_distribution_form.html'
    form_class = CourseDistributionUpdateForm
    context_object_name = 'dists'

    def get_object(self):
        return get_object_or_404(CourseDistribution, id=self.request.GET.get('id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['teachers'] = Teacher.objects.all()
        context['offers'] = CourseOffered.objects.all()
        return context

    def get_success_url(self):
        return reverse('semester:dist_list')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(**({'form': form})))



def  CourseDistributionDeleteView(request, pk):
    try:
        parent = CourseDistribution.objects.get(id=pk)
        parent.delete()
        messages.success(request, 'Successfully Deleted')
    except:
        messages.success(request, 'Please First Delete The Child Model')
        return redirect('/offers')

    return redirect('/offers')

    
   

def getBatchCourses(request):
    batch = request.GET.get('batch')

    response = {}

    qs = Course.objects.filter(curriculum__batches=batch)
    courses = []
    for d in qs:
        courses.append((d.id, d.course_code, d.title))
    response['courses'] = courses

    return JsonResponse(response)


def getOfferedSection(request):
    offered = request.GET.get('offered')
    response = {}
    qs = Section.objects.filter(batch=CourseOffered.objects.get(id=offered).batch)
    sections = []
    for d in qs:
        sections.append((d.id, d.section))
    response['sections'] = sections
    return JsonResponse(response)


def getOfferedParent(request):
    offered = request.GET.get('offered')
    response = {}
    qs = CourseDistribution.objects.filter(offered__course=CourseOffered.objects.get(id=offered).course)
    print(qs)
    parents = []
    for d in qs:
        print(d)
        parents.append((d.id, d.offered.batch.batch, d.section.section, d.teacher.name_initials))
    response['parents'] = parents

    return JsonResponse(response)
