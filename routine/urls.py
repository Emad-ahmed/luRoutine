from django.urls import path

from . import views

app_name = 'routine'

urlpatterns = [
    path('building/create/', views.BuildingCreateView.as_view(), name='building_create'),

    path('rooms/', views.RoomListView.as_view(), name='room_list'),
    path('room/create/', views.RoomCreateView.as_view(), name='room_create'),
    path('room/update/', views.RoomUpdateView.as_view(), name='room_update'),

    path('slots/', views.SlotListView.as_view(), name='slot_list'),

    path('slot/master/create/', views.SlotMasterCreateView.as_view(), name='slot_master_create'),
    path('slot/master/update/', views.SlotMasterUpdateView.as_view(), name='slot_master_update'),

    path('slot/create/', views.SlotDetailCreateView.as_view(), name='slot_create'),
    path('slot/update/', views.SlotDetailUpdateView.as_view(), name='slot_update'),

    path('routines/', views.RoutineListView.as_view(), name='routine_list'),
    path('routine/create/', views.RoutineCreateView.as_view(), name='routine-create'),
    path('routine/update/', views.RoutineUpdateView.as_view(), name='routine-update'),

    path('routine/check/', views.getRoutineSuggestion, name='routine-check'),
    path('routine/getRoom/', views.getRoom, name='room-check'),
    path('routine/checkCourse/', views.getCourseContactHour, name='course-check'),

    path('routine/pdf/', views.render_pdf_view, name='gen_routine'),
]
