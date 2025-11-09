from django.contrib import admin
from .models import Course, Student

# Inline student view inside Course admin
class StudentInline(admin.TabularInline):
    model = Student
    extra = 1   # how many empty forms to show


# Course Admin Settings
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    inlines = [StudentInline]


# Student Admin Settings
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'gender', 'course', 'created_at')
    list_filter = ('gender', 'course')
    search_fields = ('name', 'email', 'phone')
    list_per_page = 20
