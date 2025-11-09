from django.urls import path
from . import views

urlpatterns = [
    # Home & Dashboard
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),

    # Students CRUD
    path("students/", views.student_list, name="student_list"),
    path("students/add/", views.student_create, name="student_create"),
    path("students/<int:pk>/", views.student_detail, name="student_detail"),
    path("students/<int:pk>/edit/", views.student_update, name="student_update"),
    path("students/<int:pk>/delete/", views.student_delete, name="student_delete"),

    # Courses CRUD
    path("courses/", views.course_list, name="course_list"),
    path("courses/add/", views.course_create, name="course_create"),
    path("courses/<int:pk>/edit/", views.course_update, name="course_update"),
    path("courses/<int:pk>/delete/", views.course_delete, name="course_delete"),
]
