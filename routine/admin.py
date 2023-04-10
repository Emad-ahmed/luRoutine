from django.contrib import admin
from .models import Room, Building, SlotMaster, SlotDetail, Routine
from import_export.admin import ImportExportModelAdmin


@admin.register(Room)
class RoomAdmin(ImportExportModelAdmin):
    pass

@admin.register(Building)
class BuildingAdmin(ImportExportModelAdmin):
    pass



@admin.register(SlotMaster)
class SlotMasterAdmin(ImportExportModelAdmin):
    pass


@admin.register(SlotDetail)
class SlotDetailAdmin(ImportExportModelAdmin):
    pass


@admin.register(Routine)
class RoutineAdmin(ImportExportModelAdmin):
    pass




