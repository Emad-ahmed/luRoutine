from django.contrib import admin
from .models import Room, Building, SlotMaster, SlotDetail, Routine



@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    pass



@admin.register(SlotMaster)
class SlotMasterAdmin(admin.ModelAdmin):
    pass


@admin.register(SlotDetail)
class SlotDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    pass




