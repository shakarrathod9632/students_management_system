from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student, Course
from .forms import StudentForm, CourseForm


# Home Page
def home(request):
    return render(request, "students_app/home.html")


# Dashboard Page
def dashboard(request):
    total_students = Student.objects.count()
    total_courses = Course.objects.count()
    return render(request, "students_app/dashboard.html", {
        "total_students": total_students,
        "total_courses": total_courses,
    })


# -------------------------
# STUDENT CRUD OPERATIONS
# -------------------------

# List Students
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from .forms import StudentForm, CourseForm
from django.db.models import Q
from django.contrib import messages

# Student list with search & sort
def student_list(request):
    search = request.GET.get('search', '')
    sort = request.GET.get('sort', 'name')  # default sort by name A-Z

    students = Student.objects.all()

    # Search logic
    if search:
        students = students.filter(
            Q(name__icontains=search) |
            Q(email__icontains=search) |
            Q(phone__icontains=search)
        )

    # Sorting logic
    if sort == 'name':
        students = students.order_by('name')  # A-Z
    elif sort == '-name':
        students = students.order_by('-name')  # Z-A
    elif sort == 'new':
        students = students.order_by('-created_at')  # newest first
    elif sort == 'old':
        students = students.order_by('created_at')  # oldest first

    context = {
        'students': students,
        'search': search,
        'sort': sort,
    }

    return render(request, 'students_app/student_list.html', context)


# Create Student
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect("student_list")
        messages.error(request, "Error adding student. Check form details.")
    else:
        form = StudentForm()
    return render(request, "students_app/student_create.html", {"form": form})


# Student Detail Page
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students_app/student_detail.html", {"student": student})


# Update Student
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect("student_list")
        messages.error(request, "Error updating student.")
    else:
        form = StudentForm(instance=student)
    return render(request, "students_app/student_update.html", {"form": form})


# Delete Student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect("student_list")
    return render(request, "students_app/student_confirm_delete.html", {"student": student})


# -------------------------
# COURSE CRUD OPERATIONS
# -------------------------

def course_list(request):
    courses = Course.objects.all()
    return render(request, "students_app/course_list.html", {"courses": courses})


def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added successfully.")
            return redirect("course_list")
        messages.error(request, "Error adding course.")
    else:
        form = CourseForm()
    return render(request, "students_app/course_create.html", {"form": form})


def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully.")
            return redirect("course_list")
        messages.error(request, "Error updating course.")
    else:
        form = CourseForm(instance=course)
    return render(request, "students_app/course_update.html", {"form": form})


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course deleted successfully.")
        return redirect("course_list")
    return render(request, "students_app/course_confirm_delete.html", {"course": course})


# -------------------------
# Custom Error Pages
# -------------------------

def custom_404(request, exception):
    return render(request, "students_app/404.html", status=404)

def custom_500(request):
    return render(request, "students_app/500.html", status=500)
