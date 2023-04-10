from asyncio.windows_events import NULL
from contextlib import redirect_stderr
from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from faculty.models import Teacher
from routine.models import Routine
from semester.models import CourseDistribution
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView
from routine.models import Room, Building, SlotMaster, SlotDetail, Routine
from student.models import Section
import urllib.request as urllib
from routine.utils import link_callback
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect


class HomeView(ListView):
    model = Routine
    template_name = 'home.html'
    context_object_name = 'routines'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['slots'] = SlotDetail.objects.all()
        try:
            context['teachername'] = Teacher.objects.get(
                email=self.request.user)
            context['gen_routine'] = generateRoutine(
            self.request.GET.get('day') if self.request.GET.get('day') else 'sunday', self.request.user)
            context['sc'] = [0, 1, 2, 3, 4, 5, 6]
           
        except:
            context['teachername'] = "None"
            context['gen_routine'] = generateRoutine(
            self.request.GET.get('day') if self.request.GET.get('day') else 'sunday', self.request.user)
            context['sc'] = [0, 1, 2, 3, 4, 5, 6]

        return context


def generateRoutine(day_of_week, user):
    final = {}
    slots = SlotDetail.objects.all()
    rt = Routine.objects.filter(
        course_dist__offered__semester__isnull=False,
        day_of_week=day_of_week,
        course_dist__teacher__email=user)
    
    for sec in Section.objects.all():
        temp = rt.filter(course_dist__section=sec).order_by('slot__start_time')
        if temp:
            data = []
            i = 0
            print(len(temp))
            for slot in slots:
                if i < len(temp) and temp[i].slot == slot:
                    data.append(temp[i])
                    i += 1
                else:
                    data.append(None)
            final[f'{sec.batch.batch} - {sec.section}'] = data

    return final


def render_pdf_view_teacher(request):
    context = {}
    context['slots'] = SlotDetail.objects.all()
    context['routine'] = {}
    user = request.user.username
    fname = request.user.first_name
    lname = request.user.last_name
    myuser = Teacher.objects.get(email=user)
    context['first_name'] = myuser.first_name
    context['last_name'] = myuser.last_name
    days = ['sunday', 'monday', 'tuesday',
            'wednesday', 'thursday', 'friday', 'saturday']
    for day in days:
        context['routine'][day] = generateRoutine(day, user)

    template_path = 'routine_generated_teacher.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{fname} {lname}.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)

    print(pisa_status)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
