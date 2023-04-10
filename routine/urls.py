from django.urls import path

from . import views

app_name = 'routine'

urlpatterns = [
    path('building/create/', views.BuildingCreateView.as_view(), name='building_create'),

    path('rooms/', views.RoomListView.as_view(), name='room_list'),
    path('room/create/', views.RoomCreateView.as_view(), name='room_create'),
    path('room/update/', views.RoomUpdateView.as_view(), name='room_update'),
    path('room/<int:pk>/delete/', views.RoomDeleteView, name='room_delete'),

    path('slots/', views.SlotListView.as_view(), name='slot_list'),

    path('slot/master/create/', views.SlotMasterCreateView.as_view(), name='slot_master_create'),
    path('slot/master/update/', views.SlotMasterUpdateView.as_view(), name='slot_master_update'),

    path('slot/create/', views.SlotDetailCreateView.as_view(), name='slot_create'),
    path('slot/update/', views.SlotDetailUpdateView.as_view(), name='slot_update'),
    path('slot/<int:pk>/delete/', views.SlotDeleteView, name='slot_delete'),


    path('routines/', views.RoutineListView.as_view(), name='routine_list'),
    path('routine/create/', views.RoutineCreateView.as_view(), name='routine-create'),
    path('routine/update/', views.RoutineUpdateView.as_view(), name='routine-update'),
    path('routine/<int:pk>/delete/', views.RoutineDeleteView, name='routine-delete'),
    

    path('routine/check/', views.getRoutineSuggestion, name='routine-check'),
    path('routine/getRoom/', views.getRoom, name='room-check'),
    path('routine/checkCourse/', views.getCourseContactHour, name='course-check'),
    path('routine/checkroom/', views.getCheckRoom, name='checkroom'),
    path('routine/checkteacher/', views.getCheckTeacher, name='checkteacher'),
    path('routine/checkstudent/', views.getCheckStudent, name='checkstudent'),

    path('routine/pdf/', views.render_pdf_view, name='gen_routine'),
    path('routine_batch/pdf/<int:batch>/<slug:section>/', views.render_pdf_view_batchwise, name='gen_routine_batch'),

    path('routine_teacher/pdf/<int:teacher_id>/', views.render_pdf_view_teacher, name='gen_routine_teacher'),

    path('batchwiseroutine', views.BatchwiseRoutine.as_view(), name='batchwiseroutine'),

    path('my_list_view/<int:batch>/<slug:section>/', views.MyListView.as_view(), name='my_list_view'),

    path('teacherlist_view/<int:teacher_id>', views.TeacherListView.as_view(), name='teacher_routine_list'),

    
]
