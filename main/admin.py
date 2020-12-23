from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'age', 'is_studying']
    list_display_links = ['name', 'surname']
    list_editable = ['is_studying']
    list_filter = ['is_studying']
# Register your m
# odels here.
