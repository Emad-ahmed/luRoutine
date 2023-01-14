from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import get_template
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from xhtml2pdf import pisa

from faculty.models import Department
from routine.models import Room, Building, SlotMaster, SlotDetail, Routine
from semester.models import CourseDistribution
from student.models import Section
from .forms import RoomForm, BuildingForm, SlotMasterForm, SlotDetailForm, RoutineForm, DummyRoutineForm
from .utils import link_callback


@method_decorator(login_required, name='dispatch')
class BuildingCreateView(CreateView):
    model = Building
    form_class = BuildingForm

    def get(self, request, *args, **kwargs):
        return redirect('routine:room_create')

    def get_success_url(self):
        return reverse('routine:room_create')

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(**({'form': form})))


@method_decorator(login_required, name='dispatch')
class RoomListView(ListView):
    model = Room
    template_name = 'room_list.html'
    context_object_name = 'rooms'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class RoomCreateView(CreateView):
    model = Room
    template_name = 'room_form.html'
    form_class = RoomForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['departments'] = Department.objects.all()
        context['buildings'] = Building.objects.all()
        context['form'] = self.get_form()
        return context

    def get_success_url(self):
        return reverse('routine:room_list')

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(**({'room_form': form})))


@method_decorator(login_required, name='dispatch')
class RoomUpdateView(UpdateView):
    template_name = 'room_form.html'
    model = Room
    form_class = RoomForm
    context_object_name = 'room'

    def get_object(self):
        return get_object_or_404(Room, id=self.request.GET.get('id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['departments'] = Department.objects.all()
        return context

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(**({'room_form': form})))

    def get_success_url(self):
        return reverse('routine:room_list')


@method_decorator(login_required, name='dispatch')
class SlotListView(ListView):
    model = SlotDetail
    template_name = 'slot_list.html'
    context_object_name = 'slots'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class SlotMasterCreateView(CreateView):
    model = SlotMaster
    form_class = SlotMasterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get(self, request, *args, **kwargs):
        return redirect('routine:slot_create')

    def get_success_url(self):
        return reverse('routine:slot_create')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(**({'form': form})))


@method_decorator(login_required, name='dispatch')
class SlotMasterUpdateView(UpdateView):
    model = SlotMaster
    form_class = SlotMasterForm
    context_object_name = 'slot'

    def get_object(self):
        return get_object_or_404(SlotMaster, id=self.request.GET.get('id'))

    def get(self, request, *args, **kwargs):
        return redirect('routine:slot_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(**({'form': form})))

    def get_success_url(self):
        return reverse('routine:slot_create')


@method_decorator(login_required, name='dispatch')
class SlotDetailCreateView(CreateView):
    model = SlotDetail
    template_name = 'slot_form.html'
    form_class = SlotDetailForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['slots'] = SlotMaster.objects.all()
        return context

    def get_success_url(self):
        return reverse('routine:slot_list')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(**({'form': form})))


@method_decorator(login_required, name='dispatch')
class SlotDetailUpdateView(UpdateView):
    template_name = 'slot_form.html'
    model = SlotDetail
    form_class = SlotDetailForm
    context_object_name = 'slot'

    def get_object(self):
        return get_object_or_404(SlotDetail, id=self.request.GET.get('id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(**({'form': form})))

    def get_success_url(self):
        return reverse('routine:slot_list')


@method_decorator(login_required, name='dispatch')
class RoutineListView(ListView):
    model = Routine
    template_name = 'routine_list.html'
    context_object_name = 'routines'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['slots'] = SlotDetail.objects.all()
        context['gen_routine'] = generateRoutine(
            self.request.GET.get('day') if self.request.GET.get('day') else 'sunday')
        context['sc'] = [0, 1, 2, 3, 4, 5, 6]
        return context


@method_decorator(login_required, name='dispatch')
class RoutineCreateView(CreateView):
    model = Routine
    template_name = 'routine_form.html'

    def get_form_class(self):
        if self.request.GET.get('dummy'):
            return DummyRoutineForm
        return RoutineForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['dists'] = CourseDistribution.objects.all()
        context['slots'] = SlotDetail.objects.all().order_by('start_time')
        context['rooms'] = Room.objects.all()
        context['form'] = self.get_form()
        return context

    def get_success_url(self):
        return reverse('routine:routine_list')

    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(**({'form': form})))


def getRoutineSuggestion(request):
    dist = request.GET.get('course_dist')
    slot = request.GET.get('slot')
    day = request.GET.get('day_of_week')
    room = request.GET.get('room')

    response = {
        'err': -1
    }

    if dist:
        response['err'] = 1
        qs = Routine.objects.filter(course_dist=dist).count()
        response['dist_class_per_week'] = qs
        response['dist_contact_hour'] = CourseDistribution.objects.get(id=dist).offered.course.contact_hour

    if slot and room:
        response['err'] = 1
        available_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        qs = Routine.objects.filter(slot=slot, room=room).values_list('day_of_week')
        for d in qs:
            if str(d[0]) in available_days:
                available_days.remove(str(d[0]))
        response['available_days'] = available_days

    if day and room:
        response['err'] = 1
        qs = SlotDetail.objects.filter(slot__status='active').exclude(
            id__in=Routine.objects.filter(day_of_week=day, room=room)).values_list('start_time', 'end_time')

        available_slots = []
        for d in qs:
            available_slots.append(str(d[0])[:-3] + "-" + str(d[1])[:-3])
        response['available_slots'] = available_slots

    if slot and day:
        response['err'] = 1
        qs = Room.objects.all().exclude(id__in=Routine.objects.filter(slot=slot, day_of_week=day)).values_list(
            'room_number')
        available_rooms = []
        for d in qs:
            available_rooms.append(d[0])
        response['available_rooms'] = available_rooms

    if dist and slot and day:
        if not Routine.objects.filter(course_dist=dist, slot=slot, day_of_week=day):
            response['err'] = 0
            response['message'] = 'Slot Available'
        else:
            response['err'] = 2

    return JsonResponse(response)


def getRoom(request):
    dist = request.GET.get('course_dist')
    slot = request.GET.get('slot')
    day = request.GET.get('day')
    response = {}

    qs = Room.objects.all().exclude(id__in=Routine.objects.filter(slot=slot, day_of_week=day).values_list('room__id')) \
        .values_list('id', 'room_number')
    rooms = []
    for d in qs:
        rooms.append((d[0], d[1]))
    response['rooms'] = rooms

    return JsonResponse(response)


def getCourseContactHour(request):
    dist = request.GET.get('course')
    response = {}

    qs = Routine.objects.filter(course_dist=dist).count()
    response['weekly'] = qs
    response['contactHour'] = CourseDistribution.objects.get(id=dist).offered.course.contact_hour

    return JsonResponse(response)


def generateRoutine(day_of_week):
    final = {}
    slots = SlotDetail.objects.all()
    rt = Routine.objects.filter(
        course_dist__offered__semester=True,
        day_of_week=day_of_week,
        dummy_department__isnull=True

    )
    print(rt)
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


def render_pdf_view(request):
    context = {}
    context['slots'] = SlotDetail.objects.all()
    context['routine'] = {}
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    for day in days:
        context['routine'][day] = generateRoutine(day)

    template_path = 'routine_generated.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="routine.pdf"'
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
