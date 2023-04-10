from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from accounts.models import BindAccount
from faculty.models import Faculty, Department, Program, Teacher, Course, Curriculum, FacultyDean
from .forms import FacultyForm, DepartmentForm, ProgramForm, TeacherForm, CourseForm, CurriculumForm
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .utils import link_callback
from xhtml2pdf import pisa
from django.template.loader import get_template

@method_decorator(login_required, name='dispatch')
class FacultyListView(ListView):
    model = Faculty
    template_name = 'faculty_list.html'
    context_object_name = 'faculties'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class FacultyCreateView(CreateView):
    model = Faculty
    template_name = 'faculty_form.html'
    form_class = FacultyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get_success_url(self):
        return reverse('faculty:faculty_list')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(**({'form': form})))


@method_decorator(login_required, name='dispatch')
class FacultyUpdateView(UpdateView):
    template_name = 'faculty_form.html'
    model = FacultyDean
    form_class = FacultyForm
    context_object_name = 'faculty'
    

    def get_object(self):
        return get_object_or_404(FacultyDean, id=self.request.GET.get('id'))
    def get_context_data(self, **kwargs):
        print(self.get_object)
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(**({'form': form})))
    def get_success_url(self):
        
        return reverse('faculty:faculty_list')






@method_decorator(login_required, name='dispatch')
class DepartmentListView(ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'department_form.html'
    form_class = DepartmentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['faculties'] = Faculty.objects.all()
        return context

    def get_success_url(self):
        return reverse('faculty:department_list')

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(**({'form': form})))


@method_decorator(login_required, name='dispatch')
class DepartmentUpdateView(UpdateView):
    template_name = 'department_form.html'
    model = Department
    form_class = DepartmentForm
    context_object_name = 'department'

    def get_object(self):
        return get_object_or_404(Department, id=self.request.GET.get('id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['faculties'] = Faculty.objects.all()
        return context

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(**({'form': form})))

    def get_success_url(self):
        return reverse('faculty:department_list')


@method_decorator(login_required, name='dispatch')
class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'
    context_object_name = 'programs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class ProgramCreateView(CreateView):
    model = Program
    template_name = 'program_form.html'
    form_class = ProgramForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['departments'] = Department.objects.all()
        return context

    def get_success_url(self):
        return reverse('faculty:program_list')

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(**({'form': form})))


@method_decorator(login_required, name='dispatch')
class ProgramUpdateView(UpdateView):
    template_name = 'program_form.html'
    model = Program
    form_class = ProgramForm
    context_object_name = 'program'

    def get_object(self):
        return get_object_or_404(Program, id=self.request.GET.get('id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['departments'] = Department.objects.all()
        return context

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(**({'form': form})))

    def get_success_url(self):
        return reverse('faculty:program_list')


@method_decorator(login_required, name='dispatch')
class CurriculumListView(ListView):
    model = Curriculum
    template_name = 'curriculum_list.html'
    context_object_name = 'curriculums'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class CurriculumCreateView(CreateView):
    model = Curriculum
    template_name = 'curriculum_form.html'
    form_class = CurriculumForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['programs'] = Program.objects.all()
        return context

    def get_success_url(self):
        return reverse('faculty:curriculum_list')

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(**({'form': form})))


@method_decorator(login_required, name='dispatch')
class CurriculumUpdateView(UpdateView):
    model = Curriculum
    template_name = 'curriculum_form.html'
    form_class = CurriculumForm
    context_object_name = 'curriculums'

    def get_object(self):
        return get_object_or_404(Curriculum, id=self.request.GET.get('id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['programs'] = Program.objects.all()
        return context

    def get_success_url(self):
        return reverse('faculty:curriculum_list')

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(**({'form': form})))



def CurriculumDeleteView(request, pk):
    try:
        parent = Curriculum.objects.get(id=pk)
        parent.delete()
        messages.success(request, 'Successfully Deleted')
    except:
        messages.success(request, 'Please First Delete The Child Model')
        return redirect('/curriculums')

    return redirect('/curriculums')
    



@method_decorator(login_required, name='dispatch')
class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher_list.html'
    context_object_name = 'teachers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context




@method_decorator(login_required, name='dispatch')
class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'teacher_form.html'
    form_class = TeacherForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['departments'] = Department.objects.all()
        return context

    def get_success_url(self):
        return reverse('faculty:teacher_list')

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(**({'form': form})))


@method_decorator(login_required, name='dispatch')
class TeacherUpdateView(UpdateView):
    template_name = 'teacher_form.html'
    model = Teacher
    form_class = TeacherForm
    context_object_name = 'teacher'

    def get_object(self):
        return get_object_or_404(Teacher, id=self.request.GET.get('id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['departments'] = Department.objects.all()
        return context

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(**({'form': form})))

    def get_success_url(self):
        return reverse('faculty:teacher_list')


def TeacherDeleteView(request, pk):
    try:
        parent = Teacher.objects.get(id=pk)
        parent.delete()
        messages.success(request, 'Successfully Deleted')
    except:
        messages.success(request, 'Please First Delete The Child Model')
        return redirect('/teachers')
    return redirect('/teachers')



@method_decorator(login_required, name='dispatch')
class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context




@method_decorator(login_required, name='dispatch')
class CourseCreateView(CreateView):
    model = Course
    template_name = 'course_form.html'
    form_class = CourseForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['programs'] = Program.objects.all()
        context['curriculums'] = Curriculum.objects.all()
        context['courses'] = Course.objects.all()
        return context

    def get_success_url(self):
        return reverse('faculty:course_list')

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(**({'form': form})))



@method_decorator(login_required, name='dispatch')
class CourseUpdateView(UpdateView):
    template_name = 'course_form.html'
    model = Course
    form_class = CourseForm
    context_object_name = 'course'

    def get_object(self):
        return get_object_or_404(Course, id=self.request.GET.get('id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['courses'] = Course.objects.all()
        context['programs'] = Program.objects.all()
        context['curriculums'] = Curriculum.objects.all()
        return context

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(**({'form': form})))

    def get_success_url(self):
        return reverse('faculty:course_list')
    

def CourseDeleteView(request, pk):
    try:
        parent = Course.objects.get(id=pk)
        parent.delete()
        messages.success(request, 'Successfully Deleted')
    except:
        messages.success(request, 'Please First Delete The Child Model')
        return redirect('/courses')

    return redirect('/courses')



@login_required
def teacher_account_reset(request):
    teacher_id = request.POST.get('teacher_id')
    if teacher_id:
        teacher = Teacher.objects.get(id=teacher_id)
        if not BindAccount.objects.filter(teacher=teacher):
            pwd = User.objects.make_random_password(length=10,
                                                    allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
            usr = User.objects.create(username=teacher.email, password=pwd, email=teacher.email)
            usr.save()
            BindAccount.objects.create(user=usr, teacher=teacher)

        user = BindAccount.objects.get(teacher=teacher).user
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        reset_utl = 'http://' + get_current_site(request).domain + '/account/reset/' + uid + '/' + token
        return JsonResponse({
            'reset_url': reset_utl
        })

    return None


def render_pdf_teacher_view(request):
    context = {}
    context['teachers'] = Teacher.objects.all()
    
    template_path = 'generate_teacher.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="teacher.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
